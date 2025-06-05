"""Activity Implementations for Python Dapr Workflow

This file contains implementations for all workflow activities.
Activities are the building blocks of your workflow, representing individual
steps or tasks that can be orchestrated by the workflow engine.

CUSTOMIZATION GUIDE - Workflow Activities
=============================================================================
Activities are the building blocks of your workflow, representing individual
steps or tasks that can be orchestrated by the workflow engine.

1. EACH ACTIVITY FUNCTION:
   - Represents a discrete unit of work in your workflow
   - Follows a consistent pattern with proper error handling
   - Implements business logic with clean separation of concerns

2. IMPLEMENTATION STEPS:
   - Replace the generic implementations with your domain-specific logic
   - Modify the activity response data to include your domain objects
   - Add service dependencies and integrations as needed
   - Maintain proper error handling for resilient workflows

3. ACTIVITY REGISTRATION:
   - Each activity is decorated with @wfr.activity
   - No additional registration is needed

4. DOMAIN-SPECIFIC DATA:
   - Replace generic ActivityResponse with domain-specific response classes
   - Create proper business entity models rather than using dictionaries
   - Consider adding type hints throughout for better IDE support
   - Return strongly-typed objects instead of generic dictionaries
=============================================================================
"""

from typing import Any, Dict, Callable, Optional
import logging
from datetime import datetime, timezone
import time

# Import workflow runtime for activity decorators
from .runtime import workflow_runtime as wfr

# Import models
from .models import ActivityResponse
from .activity_request import ActivityRequest

# Import stack trace helper for debugging
import os
from dapr.ext.workflow.workflow_activity_context import WorkflowActivityContext

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# get the environment variable for debug mode
debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"


@wfr.activity
def prepare_paperwork_activity(ctx: WorkflowActivityContext, input: ActivityRequest) -> ActivityResponse:
    """
    Prepares and processes required onboarding paperwork.

    Args:
        ctx: The workflow activity context
        input: Input data for the activity

    Returns:
        Activity response with success/error information
    """
    logger.info(f"[Activity] Executing prepare_paperwork_activity", extra={"activityId": "prepare_paperwork"})
    
    # Create activity response
    activity_response = ActivityResponse(start_time=datetime.now(timezone.utc).isoformat())
    
    # Simulate work by sleeping for 2 seconds
    # TODO: Replace with actual work
    time.sleep(2)
    
    activity_response.success = True        
    activity_response.end_time = datetime.now(timezone.utc).isoformat()

    logger.info(f"[Activity] prepare_paperwork_activity completed successfully")
    return activity_response                

@wfr.activity
def provision_equipment_activity(ctx: WorkflowActivityContext, input: ActivityRequest) -> ActivityResponse:
    """
    Provides necessary equipment to the new employee.

    Args:
        ctx: The workflow activity context
        input: Input data for the activity

    Returns:
        Activity response with success/error information
    """
    logger.info(f"[Activity] Executing provision_equipment_activity", extra={"activityId": "provision_equipment"})
    
    # Create activity response
    activity_response = ActivityResponse(start_time=datetime.now(timezone.utc).isoformat())
    
    # Simulate work by sleeping for 2 seconds
    # TODO: Replace with actual work
    time.sleep(2)
    
    activity_response.success = True        
    activity_response.end_time = datetime.now(timezone.utc).isoformat()

    logger.info(f"[Activity] provision_equipment_activity completed successfully")
    return activity_response