from typing import Any, Dict, List, Optional, Union, Tuple
import logging
from datetime import datetime, timedelta

# Import dapr workflow modules
from dapr.ext.workflow import DaprWorkflowContext, WorkflowActivityContext, WorkflowRuntime
from dapr.ext.workflow import when_any, when_all

# Import activities from separate module
from workflow.activities import *

# Import workflow runtime
from workflow.runtime import workflow_runtime as wfr
from workflow.replay_safe_logger import ReplaySafeLogger

# Import workflow data model
from workflow.models import WorkflowData

logging.basicConfig(level=logging.INFO)
base_logger = logging.getLogger(__name__)

store_name = "statestore"

###############################################################################
# IMPORTANT: Keep Workflow Code Deterministic
###############################################################################
# 1. Don't use random.random(), time.time(), uuid.uuid4() directly in workflows
#    Instead use ctx.current_utc_datetime() for current time
# 2. Don't make direct I/O or service calls - use activities instead
#    Example: data = yield ctx.call_activity('MakeHttpCall', 'https://example.com/api/data')
# 3. Don't use mutable global state or global variables
# 4. Use the workflow context for all external interactions
# 5. Keep workflow functions deterministic - they may be replayed multiple times
###############################################################################

###############################################################################
# Name: EmployeeOnboardingWorkflow
# Description: Handles the employee onboarding process with parallel tasks for equipment provisioning and paperwork preparation.
###############################################################################

@wfr.workflow(name="employee_onboarding_workflow")
def employee_onboarding_workflow(ctx: DaprWorkflowContext, input_data: Any) -> Any:
    """
    Handles the employee onboarding process with parallel tasks for equipment provisioning and paperwork preparation.

    Args:
        ctx: The workflow context provided by Dapr
        input_data: Data passed to the workflow

    Returns:
        The workflow result
    """
    logger = ReplaySafeLogger(ctx, base_logger)
    logger.info(f"[Workflow] Starting workflow: {ctx.instance_id}")

    # Convert input data to WorkflowData object
    data = WorkflowData.from_dict(input_data)

    logger.info("[Workflow] Starting parallel execution for: Splits the workflow to perform equipment provisioning and paperwork preparation in parallel.")
    # Create a dictionary to track parallel tasks by name
    parallel_tasks = {}
    logger.info("[Workflow] Adding parallel task for: Provides necessary equipment to the new employee.")
    parallel_tasks["provision_equipment"] = ctx.call_activity(provision_equipment_activity, input=data.get_activity_request_data())

    logger.info("[Workflow] Adding parallel task for: Prepares and processes required onboarding paperwork.")
    parallel_tasks["prepare_paperwork"] = ctx.call_activity(prepare_paperwork_activity, input=data.get_activity_request_data())


    logger.info("[Workflow] Wait for all tasks to complete")
    try:
        results = yield when_all(list(parallel_tasks.values()))
        logger.info("[Workflow] All parallel tasks completed successfully")
        
        # Process results one by one
        for i, result in enumerate(results):
            task_name = list(parallel_tasks.keys())[i]
            logger.info(f"[Workflow] Processing and merging result from {task_name}")
            # TODO: merge results if needed
            data.add_activity_response(task_name, result)
    except Exception as e:
        logger.error(f"[Workflow] Error in parallel execution: {e}")
        data.error_message = str(e)
        data.has_error = True
        data.success = False
        return data

    return process_join_tasks(ctx, data)


def process_join_tasks(ctx: DaprWorkflowContext, data: WorkflowData) -> Any:
    """
    Args:
        ctx: The workflow context
        data: The workflow data object

    Returns:
        The updated workflow data
    """
    logger = ReplaySafeLogger(ctx, base_logger)
    logger.info("[Workflow] Workflow reached end: End of employee onboarding process")
    # Return the final workflow data
    return data
