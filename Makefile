.PHONY: setup run test clean init-dapr setup start-app stop-app start-workflow check-workflow wait-for-app

# Application name and settings
APP_NAME=employee_onboarding_workflow
DAPR_APP_ID=employee_onboarding_workflow
APP_PORT=8308
DAPR_HTTP_PORT=3860
DAPR_GRPC_PORT=50143
API_PORT=8080

# Check if uv is installed
check-uv: ## Check if uv is installed
	@command -v uv >/dev/null 2>&1 && { echo "uv is installed"; UV_AVAILABLE=1; } || { echo "uv not found, using pip"; UV_AVAILABLE=0; }

# Setup virtual environment and install dependencies
setup: init-dapr check-uv ## Create virtual environment and install dependencies
	@echo "Creating virtual environment and installing dependencies..."
	@if command -v uv >/dev/null 2>&1; then \
		echo "Using uv for dependency management..."; \
		uv venv; \
		uv add -r requirements.txt; \
		uv pip install -e .; \
	else \
		echo "Using pip for dependency management..."; \
		python3 -m venv venv; \
		. activate_env.sh && pip install -r requirements.txt; \
		. activate_env.sh && pip install -e .; \
	fi
	@echo "Setup complete!"

# Check if Dapr is installed
check-dapr: ## Check if Dapr is installed
	@command -v dapr >/dev/null 2>&1 && { echo "Dapr CLI is installed"; exit 0; } || { echo "Dapr is not installed. Please install it from https://docs.dapr.io/getting-started/install-dapr-cli/"; exit 1; }

# Initialize Dapr if not already initialized
init-dapr: check-dapr ## Initialize Dapr
	@dapr version -o json | grep 'Runtime version":"n/a"' && dapr init --dev --runtime-version 1.15.4 || \
		{ echo "Dapr Server is installed"; dapr version; exit 0; }

# Run tests
test: ## Run tests
	@echo "Running tests..."
	@if command -v uv >/dev/null 2>&1; then \
		uv venv exec pytest; \
	else \
		. activate_env.sh && pytest; \
	fi

# Clean build artifacts
clean: ## Clean build artifacts
	@echo "Cleaning build artifacts..."
	rm -rf __pycache__ || true
	rm -rf src/__pycache__ || true
	rm -rf src/workflow/__pycache__ || true
	rm -rf tests/__pycache__ || true
	rm -rf *.egg-info || true
	rm -rf .pytest_cache || true
	rm -rf .coverage || true
	rm -rf build/ dist/ || true
	rm -rf venv/ .venv/ || true

# Wait for application to be ready
wait-for-app: ## Wait for application to initialize
	@echo "Waiting for application to initialize..."
	@echo "This may take up to 30 seconds..."
	@for i in $$(seq 1 15); do \
		HTTP_STATUS=$$(curl -s -o /dev/null -w "%{http_code}" http://localhost:$(APP_PORT)/healthz || echo "000"); \
		if [ "$$HTTP_STATUS" = "204" ] || [ "$$HTTP_STATUS" = "200" ]; then \
			echo "Application is up! (HTTP status: $$HTTP_STATUS)"; \
			break; \
		else \
			echo "Waiting for application to start... ($$i/15) Status: $$HTTP_STATUS"; \
			sleep 2; \
		fi; \
	done

# Start Dapr APP using dapr.yaml
start: setup ## Start application with Dapr
	@echo "Starting the application with Dapr..."
	@echo "Using Dapr HTTP port: $(DAPR_HTTP_PORT)"
	@echo "Using Dapr gRPC port: $(DAPR_GRPC_PORT)"
	. activate_env.sh && dapr run -f ./dapr.yaml;

# Stop Dapr APP
stop: ## Stop Dapr application
	@echo "Stopping the Dapr application..."
	dapr stop -f ./dapr.yaml

# Start a workflow via API call
start-workflow: wait-for-app ## Start a workflow with optional JSON input
	@if [ -z "$(JSON_INPUT)" ]; then \
		echo "Running workflow with empty input.\nTo provide a custom input, pass JSON_INPUT like: make start-workflow JSON_INPUT='{\"some_key\": \"some_value\"}'.\n"; \
		JSON_INPUT="{}"; \
	fi
	@echo "Starting a new workflow instance..."
	curl -X POST http://localhost:$(API_PORT)/api/workflow/start \
		-H "Content-Type: application/json" -d '$(JSON_INPUT)'

# Check the status of a workflow
check-workflow: ## Check workflow status (requires INSTANCE_ID=<workflow_id>)
	@if [ -z "$(INSTANCE_ID)" ]; then \
		echo "Error: Workflow ID is required. Usage: make check-workflow INSTANCE_ID=<workflow_id>"; \
		exit 1; \
	fi
	@curl -s -H "Accept: application/json" http://localhost:$(API_PORT)/api/workflow/$(INSTANCE_ID)

# Raise an event to a workflow
raise-event: ## Raise an event to a workflow (requires EVENT_LABEL_NAME and INSTANCE_ID and optionally EVENT_DATA)
	@if [ -z "$(EVENT_LABEL_NAME)" ] || [ -z "$(INSTANCE_ID)" ]; then \
		echo "Error: EVENT_LABEL_NAME and INSTANCE_ID are required. Usage: make raise-event EVENT_LABEL_NAME=<event> INSTANCE_ID=<instance_id> [EVENT_DATA='{\"key\":\"value\"}']"; \
		exit 1; \
	fi
	@echo "Raising event '$(EVENT_LABEL_NAME)' for workflow instance '$(INSTANCE_ID)'..."
	curl -X POST http://localhost:$(API_PORT)/api/workflow/$(INSTANCE_ID)/event/$(EVENT_LABEL_NAME) \
		-H "Content-Type: application/json" \
		-d '$(EVENT_DATA)'

# Build Python package
build: ## Build Python package
	@echo "Building Python package..."
	@if command -v uv >/dev/null 2>&1; then \
		echo "Using uv build..."; \
		uv pip install build; \
		uv build; \
	else \
		echo "Using pip build..."; \
		python3 -m pip install --upgrade pip build; \
		python3 -m build; \
	fi

# Show help
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Default target
.DEFAULT_GOAL := help