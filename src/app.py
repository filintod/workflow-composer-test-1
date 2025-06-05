import logging
import os
import signal
import sys
from contextlib import asynccontextmanager
from time import sleep

from fastapi import FastAPI
from dapr.ext.fastapi import DaprApp
from dapr.conf import settings

from workflow.runtime import workflow_runtime as wf

# Import the workflow file so it is registered as we are using a decorator
from workflow.workflow import employee_onboarding_workflow

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("employee_onboarding_workflowService")

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage application lifecycle - startup and shutdown
    """
    # Initialize the Dapr workflow runtime on application startup
    logger.info("Starting employee_onboarding_workflow service...")
    
    # Log Dapr ports for debugging
    logger.info(f"Using Dapr ports - gRPC: {settings.DAPR_GRPC_PORT}, HTTP: {settings.DAPR_HTTP_PORT}")
    
    # Start the workflow runtime
    wf.start()
    
    # Wait for the sidecar to become available
    logger.info("Waiting for Dapr sidecar to become available...")
    sleep(2)
    
    logger.info("employee_onboarding_workflow service started")
    
    yield
    
    # Clean up resources on application shutdown
    logger.info("Shutting down employee_onboarding_workflow service...")
    
    # Shutdown the workflow runtime
    wf.shutdown()
    
    logger.info("employee_onboarding_workflow service stopped")

# FastAPI app and Dapr app
app = FastAPI(title="employee_onboarding_workflow Service", lifespan=lifespan)
dapr_app = DaprApp(app)

@app.get("/")
async def read_root():
    """
    Root endpoint that returns service information.
    """
    return {
        "service": "employee_onboarding_workflow Service",
        "status": "running",
        "version": "1.0.0",
    }

@app.get("/healthz")
async def healthz():
    """
    Health check endpoint required by Dapr.
    """
    return {"status": "healthy"}


if __name__ == "__main__":
    from uvicorn.config import Config
    from uvicorn.server import Server
    
    # Run the FastAPI application with uvicorn
    port = int(os.environ.get("APP_PORT", "8080"))
    host = os.environ.get("APP_HOST", "0.0.0.0")
    
    # Create the config and server
    config = Config(app=app, host=host, port=port, log_level="info", reload=True)
    server = Server(config=config)

    # Handle shutdown signals
    def handle_exit(signo, frame):
        logger.info(f"Received signal {signo}. Starting graceful shutdown...")
        server.should_exit = True

    # Register signal handlers
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    
    try:
        # Start the server
        server.run()
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)
    finally:
        logger.info("Server shutdown complete")