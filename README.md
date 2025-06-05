# employee_onboarding_workflow

### Handles the employee onboarding process with parallel tasks for equipment provisioning and paperwork preparation.

---

Initial Scaffold generated with Dapr [Workflow Composer](https://workflows.diagrid.io) by [<img src="https://workflows.diagrid.io/images/logo/diagrid.svg" width="80px" style="vertical-align: middle;">](https://diagrid.io)

_Version_: `development`

---

## 🧭 Workflow Diagram

[<img src="EmployeeOnboardingWorkflow.png" alt="employee_onboarding_workflow" style="display: block; margin: 0 auto; border: 2px solid #444; width: auto; max-width: 80%; max-height: 700px; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);" />](EmployeeOnboardingWorkflow.png)


---

## 🚀 Choose Your Deployment Path

> 📋 **Quick Decision Guide**  
> - **🌟 Catalyst (Recommended)**: Get started in minutes with managed infrastructure, built-in observability, and team collaboration. Perfect for production-ready workflows and rapid prototyping.
> - **🛠️ Local Development**: Choose this for offline development, learning Dapr internals, or when you need full infrastructure control.

**New to Dapr Workflows?** → Start with **Catalyst** for the smoothest experience  
**Building for production?** → **Catalyst** provides enterprise-grade reliability  
**Learning or customizing?** → **Local Dapr** gives you full control and insight

<details>
<summary><svg xmlns="http://www.w3.org/2000/svg" width="90" height="30" viewBox="0 0 215 59" fill="none" viewBox="0 0 215 59" class="productSvg_lApt" role="img" alt="Catalyst" style="vertical-align: middle;"><path fill="#fff" d="M86.094 43.184q-2.894 0-5.374-1.015a14 14 0 0 1-4.36-2.894 13.4 13.4 0 0 1-2.856-4.359q-.977-2.48-.977-5.336t.977-5.337a13 13 0 0 1 2.856-4.322 14.1 14.1 0 0 1 4.322-2.893q2.481-1.053 5.412-1.053 3.156 0 5.562 1.053a13.5 13.5 0 0 1 4.246 2.818l-3.457 3.458a7.6 7.6 0 0 0-2.668-1.88q-1.578-.675-3.683-.676-1.842 0-3.382.639a7.3 7.3 0 0 0-2.631 1.804q-1.128 1.165-1.729 2.818-.6 1.617-.601 3.57 0 1.992.601 3.608a8.3 8.3 0 0 0 1.729 2.819 7.95 7.95 0 0 0 2.63 1.804q1.542.639 3.383.639 2.217 0 3.796-.677 1.616-.676 2.705-1.916l3.458 3.457a13.1 13.1 0 0 1-4.284 2.856q-2.443 1.015-5.675 1.015m20.1 0q-2.48 0-4.472-1.24t-3.12-3.383q-1.126-2.142-1.127-4.81 0-2.706 1.128-4.848t3.119-3.382 4.472-1.24q1.954 0 3.495.789a6.15 6.15 0 0 1 2.443 2.217q.939 1.391 1.014 3.157v6.539q-.075 1.804-1.014 3.194-.903 1.39-2.443 2.218-1.54.789-3.495.789m.902-4.547q2.067 0 3.345-1.353 1.277-1.39 1.277-3.57 0-1.43-.601-2.518a4 4 0 0 0-1.616-1.73q-1.014-.638-2.405-.638-1.353 0-2.405.639-1.015.6-1.616 1.729-.564 1.089-.564 2.517 0 1.466.564 2.593a4.66 4.66 0 0 0 1.616 1.73q1.052.6 2.405.6m4.359 4.171v-4.885l.79-4.435-.79-4.36v-4.471h4.886v18.151zm11.909 0V17.103h4.923v25.705zm-4.246-13.83v-4.321h13.416v4.321zm23.336 14.206q-2.481 0-4.473-1.24-1.99-1.24-3.119-3.383-1.127-2.142-1.127-4.81 0-2.706 1.127-4.848t3.119-3.382 4.473-1.24q1.953 0 3.495.789a6.14 6.14 0 0 1 2.442 2.217q.94 1.391 1.015 3.157v6.539q-.075 1.804-1.015 3.194-.901 1.39-2.442 2.218-1.542.789-3.495.789m.902-4.547q2.066 0 3.344-1.353 1.278-1.39 1.278-3.57 0-1.43-.601-2.518a4 4 0 0 0-1.616-1.73q-1.015-.638-2.405-.638-1.353 0-2.406.639-1.014.6-1.616 1.729-.563 1.089-.563 2.517 0 1.466.563 2.593a4.67 4.67 0 0 0 1.616 1.73q1.053.6 2.406.6m4.359 4.171v-4.885l.789-4.435-.789-4.36v-4.471h4.885v18.151zm9.241 0v-27.17h4.923v27.17zm14.997.15-7.591-18.301h5.336l5.036 13.98h-1.804l5.224-13.98h5.374l-8.08 18.301zm-5.036 7.441 5.525-11.687 3.006 4.246-3.307 7.441zm24.683-7.178a11.4 11.4 0 0 1-3.044-.413 11.9 11.9 0 0 1-2.706-1.127 8.8 8.8 0 0 1-2.142-1.804l2.931-2.97a6.1 6.1 0 0 0 2.18 1.58q1.24.525 2.743.525 1.203 0 1.804-.338.639-.338.639-1.015 0-.75-.676-1.165-.639-.412-1.692-.676-1.051-.3-2.217-.639a14 14 0 0 1-2.179-.94 5.1 5.1 0 0 1-1.729-1.615q-.639-1.053-.639-2.706 0-1.73.827-3.007.864-1.277 2.442-1.992 1.58-.714 3.721-.713 2.254 0 4.059.789a7.46 7.46 0 0 1 3.044 2.367l-2.969 2.97q-.827-1.016-1.879-1.466a5.4 5.4 0 0 0-2.217-.451q-1.09 0-1.692.338-.563.337-.563.94 0 .675.639 1.052.676.376 1.728.676 1.052.263 2.18.639a8.5 8.5 0 0 1 2.18.977 5 5 0 0 1 1.691 1.691q.676 1.053.676 2.706 0 2.668-1.916 4.247-1.917 1.54-5.224 1.54m13.128-.413V17.103h4.923v25.705zm-4.246-13.83v-4.321h13.416v4.321z"></path><path fill="#41BD9B" d="M29.697 9.455a4.727 4.727 0 1 0 0-9.455 4.727 4.727 0 0 0 0 9.455M31.336 39.9c5.575-.905 9.36-6.158 8.456-11.732-.905-5.575-6.158-9.361-11.733-8.456-5.574.905-9.36 6.158-8.455 11.733.905 5.574 6.158 9.36 11.732 8.455M34.425 53.993a4.727 4.727 0 1 1-9.455 0 4.727 4.727 0 0 1 9.455 0"></path><path fill="#41BD9B" d="M44.075 3.826a4.038 4.038 0 1 0-3.915 7.064 21.66 21.66 0 0 1 11.159 18.928 21.66 21.66 0 0 1-11.155 18.927 4.038 4.038 0 1 0 3.916 7.064 29.73 29.73 0 0 0 15.312-25.987A29.73 29.73 0 0 0 44.075 3.835zM8.073 29.813a21.66 21.66 0 0 0 11.155 18.928v-.01a4.038 4.038 0 1 1-3.916 7.065A29.73 29.73 0 0 1 0 29.809 29.74 29.74 0 0 1 15.317 3.82a4.038 4.038 0 1 1 3.916 7.065 21.66 21.66 0 0 0-11.16 18.927"></path></svg></summary>


### Prerequisites
- [Python 3.9 or later](https://www.python.org/downloads/)
- [Diagrid account](https://catalyst.diagrid.io) (free tier available)
- [Diagrid CLI](https://docs.diagrid.io/catalyst/references/cli-reference/intro/) version 0.386.0 or later
- (Optional but recommended) [uv](https://github.com/astral-sh/uv) - A modern Python package manager

### Setup Steps

#### 1. Verify Diagrid CLI Installation
```bash
# Check Diagrid CLI version
diagrid version
```
Make sure the CLI version is 0.386.0 or later.

#### 2. Setup Environment and Dependencies

**Using uv (recommended):**
```bash
# Create and activate virtual environment
uv venv venv
. venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .
```

**Using pip:**
```bash
# Create and activate virtual environment
python3 -m venv venv
. venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

#### 3. Start the Application
> 💡 **Tip**: The Diagrid CLI will start your Dapr workflow app and provision all required remote resources—actor state store, dapr sidecars, and more—into a Catalyst project.

```bash
# Start with cloud-managed Dapr infrastructure
diagrid dev run -f dapr.yaml --project python-wf-app
```

#### 4. Configure Environment (in a new terminal)
```bash
# Set the Dapr host address for cloud endpoint
export DAPR_HOST_ENDPOINT=`diagrid project get python-wf-app -o json | grep '"http"' -A 2 | grep '"url"' | cut -d '"' -f 4`

# On Windows PowerShell:
# $env:DAPR_HOST_ENDPOINT = "$(diagrid project get --project python-wf-app -o json | ConvertFrom-Json | Select-Object -ExpandProperty status | Select-Object -ExpandProperty endpoints | Select-Object -ExpandProperty http | Select-Object -ExpandProperty url)"
```

#### 5. Start a Workflow
```bash
# Wait a moment for the application to start, then:
curl -X POST ${DAPR_HOST_ENDPOINT}:3984/v1.0/workflows/dapr/build_pipeline_workflow/start \
   -H "Content-Type: application/json" \
   -d '{"data": {"unit_tests_required": true}}'

# On Windows PowerShell:
# Invoke-WebRequest -Method POST -Uri $Env:DAPR_HOST_ENDPOINT:3984/v1.0/workflows/dapr/build_pipeline_workflow/start -ContentType "application/json" -Body '{"data":{"unit_tests_required": true}}'
```

#### 6. Check Workflow Status
```bash
# Replace <instance-id> with the ID returned from the start command
curl -s ${DAPR_HOST_ENDPOINT}:3984/v1.0/workflows/dapr/<instance-id>

# On Windows PowerShell:
# Invoke-WebRequest -Uri $Env:DAPR_HOST_ENDPOINT:3984/v1.0/workflows/dapr/<instance-id>
```

</details>

<details>
<summary><strong>🏠 Local Dapr Development</strong></summary>

### Prerequisites
- [Python 3.9 or later](https://www.python.org/downloads/)
- [Dapr CLI](https://docs.dapr.io/getting-started/install-dapr-cli/) version 1.15 or later
- [Docker](https://www.docker.com/products/docker-desktop) (for running Dapr components)
- (Optional but recommended) [uv](https://github.com/astral-sh/uv) - A modern Python package manager

### Setup Steps

#### 1. Verify Dapr Installation
```bash
# Check Dapr version
dapr --version
```
Make sure the version is 1.15 or later for CLI and Runtime.

If you haven't initialized Dapr before:
```bash
dapr init
```

#### 2. Setup Environment and Dependencies

**Using uv (recommended):**
```bash
# Create and activate virtual environment
uv venv venv
. venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .
```

**Using pip:**
```bash
# Create and activate virtual environment
python3 -m venv venv
. venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .
```

#### 3. Start the Application
```bash
# Start all apps defined in dapr.yaml
dapr run -f .
```

#### 4. Configure Environment (in a new terminal)
```bash
# Set the Dapr host address
export DAPR_HOST_ENDPOINT=http://localhost

# On Windows PowerShell:
# $env:DAPR_HOST_ENDPOINT = "http://localhost"
```

#### 5. Start a Workflow
```bash
# Wait a moment for the application to start, then:
curl -X POST ${DAPR_HOST_ENDPOINT}:3984/v1.0/workflows/dapr/build_pipeline_workflow/start \
   -H "Content-Type: application/json" \
   -d '{"data": {"unit_tests_required": true}}'

# On Windows PowerShell:
# Invoke-WebRequest -Method POST -Uri $Env:DAPR_HOST_ENDPOINT:3984/v1.0/workflows/dapr/build_pipeline_workflow/start -ContentType "application/json" -Body '{"data":{"unit_tests_required": true}}'
```

#### 6. Check Workflow Status
```bash
# Replace <instance-id> with the ID returned from the start command
curl -s ${DAPR_HOST_ENDPOINT}:3984/v1.0/workflows/dapr/<instance-id>

# On Windows PowerShell:
# Invoke-WebRequest -Uri $Env:DAPR_HOST_ENDPOINT:3984/v1.0/workflows/dapr/<instance-id>
```

</details>

---

## Detailed Documentation

## Overview

This application implements a Dapr workflow using Python and the Dapr workflow SDK. It demonstrates how to:

- Define a workflow using the Dapr Workflow SDK
- Use a unified data model for workflow state
- Handle conditions and branching
- Expose a REST API for workflow management

## Workflow Determinism

Any non-deterministic code should go into activities. This includes, calling other (Dapr) services, state stores, pub/sub systems, and external endpoints. The workflow should only be responsible for the business logic that defines the sequence of the activities.

The Dapr workflow engine replays workflows multiple times during execution, so workflow code must behave consistently on each replay. Activities are the appropriate place for operations with side effects or external dependencies.

## Data Flow Architecture

The workflow uses a simple `WorkflowData` class to manage state throughout the entire execution.
It keeps track of activity history and allows for easy access to the data needed for the next activity.

If you start the process with the environment variable `DEBUG=true`, it will keep a history of all the activities and their results.
This is useful for debugging and understanding the flow of data through the workflow.

### Decision Points Reference

This workflow contains several decision points that determine the flow of execution.

You can customize by setting specific values in the `WorkflowData`. 

Decision points are in most cases mutually exclusive - only one should be set to `true`.
| Example Condition | `is_approved` | `data.set_value("is_approved", True)` |
| Example Validation | `is_valid` | `data.set_value("is_valid", check_validity(data))` |

### Benefits and Limitations of the Data Model

#### Benefits for Getting Started:
1. **Simplified Data Flow**: A single object flows through the workflow, making it easy to trace data.
2. **Dynamic Properties**: Using `get_value()` and `set_value()` methods allows flexible data storage without defining many classes.
3. **Easy Parallel Handling**: A unified structure simplifies merging results from parallel branches.
4. **Minimal Code Generation**: Reduces the need to generate many specialized classes.

#### Limitations for Production Use:
1. **Limited Type Safety**: Using string keys with dynamic data reduces type checking.
2. **No Schema Validation**: No built-in validation for required properties or data formats.
3. **Reduced Readability**: Less clarity about what data each activity actually needs.
4. **Performance Overhead**: Dynamic serialization/deserialization has some overhead.

For production systems, consider evolving toward domain-specific models that better represent your business entities.

#### Tips for Effective Data Handling

1. **Use Python idioms**: Follow Python naming conventions (snake_case) for all fields
2. **Consider input validation**: Validate data before passing it to activities
3. **Leverage immutability**: Use copy methods to avoid modifying the original data
4. **Add structured logging**: Use Python's logging module with appropriate context for better debugging

## Customization Guidelines

### Adapting the Unified Data Model

The generated workflow uses a simplified approach with a single `WorkflowData` class that flows through all activities. While this is convenient for getting started, you may want to adapt it for real-world scenarios:

1. **Domain-Specific Models**: Replace the generic `WorkflowData` with your domain entities
   ```python
   @dataclass
   class OrderProcessing:
       input: OrderRequest
       result: OrderResult
   ```

2. **Activity-Specific Types**: Define input/output types for each activity
   ```python
   @wfr.activity
   def verify_inventory_activity(ctx, input: InventoryRequest) -> InventoryResult:
       # Extract what this activity needs
       product_id = input.product_id
       if not product_id:
           raise ValueError("Missing required field: product_id")

       # Business logic here
       # ...

       return result
   ```

3. **Custom Business Logic**: Replace the generic activity implementations with your actual business logic
   ```python
   # Instead of:
   if data.get_bool("has_inventory")
   
   # Use domain-specific logic:
   has_stock = await inventory_service.has_sufficient_stock(
       order_details.product_id, 
       order_details.quantity
   )
   if has_stock:
       # Process order
   ```

### Conditional Logic Improvements

The generated workflow uses simple boolean conditions via `get_bool()` for simplicity. In production code:

1. Replace these with proper domain logic
2. Use strongly-typed properties instead of the dynamic dictionary
3. Add validation and error handling for conditional flows

Example transformation:
```python
# Generated code:
if data.get_bool("is_approved")

# Production code:
approved = await approval_service.validate_approval(
    request.order_id, 
    workflow_execution.instance_id
)
if approved:
    # Handle approval logic
```

### Handling Complexity

For more complex workflows:

1. Break large workflows into smaller sub-workflows
2. Add robust error handling and compensation logic
3. Implement observability through structured logging and metrics
4. Consider versioning strategies for long-running workflows

## Project Structure

```
.
├── 🛠 pyproject.toml        # Python project metadata and dependencies
├── 📄 README.md             # This documentation file
├── 🧩 components/           # Dapr component configurations
│   ├── pubsub.yaml          # Message broker/pub-sub component
│   └── statestore.yaml      # State store component
├── 🖥️ src/                  # Source code directory
│   ├── __init__.py          # Makes the directory a Python package
│   ├── app.py               # Application entry point
│   └── workflow/            # Workflow-related code
│       ├── __init__.py      # Makes workflow a Python package
│       ├── activities.py    # Individual workflow activities/tasks
│       ├── models.py        # Data models for workflow state
│       ├── runtime.py       # Workflow runtime configuration
│       └── workflow.py      # Main workflow orchestration
├── 📝 requirements.txt      # Python dependencies list
└── 🐳 Dockerfile            # Container definition
```

---

Initial Scaffold generated with Dapr [Workflow Composer](https://workflows.diagrid.io) by [<img src="https://workflows.diagrid.io/images/logo/diagrid.svg" width="80px" style="vertical-align: middle;">](https://diagrid.io)

_Version_: `development`