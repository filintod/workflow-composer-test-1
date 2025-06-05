"""
Workflow Data Models

This module defines the data structures used by the workflow.
These models provide a standardized way to pass data between activities
and maintain workflow state throughout execution.

IMPORTANT FOR PRODUCTION USE:
This model provides a minimal generic implementation with only essential methods.
For production systems, you should:
1. Define domain-specific types with proper field validation
2. Implement strong typing for activity inputs and outputs
3. Replace generic dictionaries with well-defined class structures
4. Add custom serialization/deserialization as needed

MINIMALIST DESIGN PHILOSOPHY:
These models are deliberately minimal, containing only essential fields needed
for workflow execution. This design emphasizes clarity and ease of use
during prototyping and testing. Additional fields should only be added
when needed for your specific use case.
"""

import os
import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
from .activity_request import ActivityRequest

class CustomJSONEncoder(json.JSONEncoder):
    """Custom JSON encoder that handles non-serializable types."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
            return obj.to_dict()
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)

class ActivityType:
    """Activity types enumeration"""
    ACTIVITY = "activity"
    EVENT = "event"
    TIMER = "timer"

@dataclass
class ActivityResponse:
    """
    Represents the result of a single activity execution.
    
    IMPORTANT: This is a minimal implementation with only essential fields.
    For production use, you SHOULD create your own domain-specific response types:
    
    1. Create domain-specific response classes for each activity type
    2. Add strongly typed fields relevant to your specific activities
    3. Implement proper validation for all output data
    
    Example:
    ```python
    @dataclass
    class OrderProcessingResponse:
        order_id: str
        status: str
        shipping_address: Address
        tracking_number: Optional[str] = None
        total_amount: float = 0.0
        success: bool = True
        error: Optional[str] = None
    ```
    """
    # Timing information
    start_time: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    end_time: Optional[str] = None
    
    # Status fields
    success: bool = False
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Converts the activity response to a dictionary."""
        return {
            'startTime': self.start_time,
            'endTime': self.end_time,
            'success': self.success,
            'error': self.error
        }

# Event response type - a simplified alias for a dictionary
EventResponse = Dict[str, Any]

@dataclass
class WorkflowActivityInfo:
    """Contains information about an activity to be used in the workflow state history for debugging."""
    activity_name: str
    activity_type: str
    start_time: str
    end_time: str

    def to_dict(self) -> Dict[str, Any]:
        """Converts the workflow activity info to a dictionary."""
        return {
            'activityName': self.activity_name,
            'activityType': self.activity_type,
            'startTime': self.start_time,
            'endTime': self.end_time
        }

@dataclass
class WorkflowData:
    """
    Main workflow data container with standardized structure.
    
    IMPORTANT: This is a SCAFFOLD implementation primarily for demonstration purposes.
    For production use, you SHOULD:
    
    1. Create domain-specific workflow data models that extend or replace this class
    2. Add strongly typed fields specific to your workflow's needs
    3. Define custom methods that handle your specific business logic
    4. Consider implementing proper validation for all input data
    
    This generic implementation provides basic structure and examples, but
    you should tailor it to your specific domain requirements.
    """
    # Complete state accessible to the workflow
    data: Dict[str, Any] = field(default_factory=dict)
    
    # Original immutable data from initialization
    original: Dict[str, Any] = field(default_factory=dict)
    
    # Status information
    success: bool = True
    
    # Linear history of activity executions for debugging
    activity_history: List[WorkflowActivityInfo] = field(default_factory=list)
    
    # Debug mode
    debug_mode: bool = field(default_factory=lambda: os.getenv("DEBUG") == "true")

    def add_to_activity_history(self, activity_name: str, activity_type: str, activity_response: ActivityResponse) -> None:
        """
        Adds an activity response to the workflow's history.
        
        Args:
            activity_name: Name of the activity
            activity_type: Type of the activity (activity, event, timer)
            activity_response: The activity response object
        """
        if self.debug_mode:
            activity_info = WorkflowActivityInfo(
                activity_name=activity_name,
                activity_type=activity_type,
                start_time=activity_response.start_time,
                end_time=activity_response.end_time
            )
            self.activity_history.append(activity_info)

    def add_activity_response(self, activity_name: str, activity_response: ActivityResponse) -> None:
        """
        Updates the workflow's activity history with an activity response.
        
        IMPORTANT: This method only adds the activity to history. It does not transfer
        any data from the activity response to the workflow state. For domain-specific 
        data transfer, you should:
        
        1. Create domain-specific response types for your activities
        2. Implement custom methods to extract and process data from those responses
        3. Update your workflow state accordingly
        
        Args:
            activity_name: Name of the activity
            activity_response: The activity response object
        """
        # Add the activity to history
        self.add_to_activity_history(activity_name, ActivityType.ACTIVITY, activity_response)

    def add_event_response(self, event_name: str, event_end_time: datetime, event_data: Dict[str, Any] = None) -> None:
        """
        Adds an event response to the workflow data.
        
        This method adds the event to the activity history and updates the workflow data
        with the event's data if provided.
        
        Args:
            event_name: Name of the event
            event_end_time: When the event was triggered
            event_data: Optional data associated with the event
        """
        # Create a basic activity response with just timing information
        event_response = ActivityResponse(
            end_time=event_end_time.isoformat(),
            success=True
        )
        
        # Add to activity history
        self.add_to_activity_history(event_name, ActivityType.EVENT, event_response)
        
        # If you need to store event data in workflow data, do it directly
        if event_data:
            if self.data is None:
                self.data = {}
            self.data.update(event_data)

    def add_timer_response(self, timer_name: str, timer_end_time: datetime) -> None:
        """
        Adds a timer response to the workflow data.
        
        Args:
            timer_name: Name of the timer
            timer_end_time: When the timer was triggered
            timer_data: Optional data associated with the timer completion
        """
        # Create a basic activity response with just timing information
        timer_response = ActivityResponse(
            end_time=timer_end_time.isoformat(),
            success=True
        )
        
        # Add to activity history
        self.add_to_activity_history(timer_name, ActivityType.TIMER, timer_response)

    def for_continue_as_new_workflow(self) -> Dict[str, Dict[str, Any]]:
        """Creates a dictionary for the 'Continue As New' operation as starting data for a new workflow."""
        return {
            'data': self.data.copy(),
            'original': self.original.copy(),
        }

    def get_activity_request_data(self) -> ActivityRequest:
        """
        Creates an empty ActivityRequest scaffold.
        
        IMPORTANT: For production use, implement domain-specific request types
        instead of using this generic implementation. See activity_request.py
        for guidance on creating properly typed activity request models.
        """
        return ActivityRequest()

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Gets a boolean value from the workflow data."""
        # First check in data
        if key in self.data:
            value = self.data.get(key)
            if isinstance(value, bool):
                return value
                
        # Fall back to original data
        if key in self.original:
            value = self.original.get(key)
            if isinstance(value, bool):
                return value
                
        return default

    def to_json(self) -> str:
        """Serializes the workflow data to JSON."""
        return json.dumps(self, cls=CustomJSONEncoder, default=lambda o: o.__dict__)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'WorkflowData':
        """Creates a WorkflowData instance from a dictionary."""
        if not data:
            return cls()
            
        workflow_data = cls(
            success=data.get('success', True)
        )
        
        # Copy data
        if 'data' in data and isinstance(data['data'], dict):
            workflow_data.data = data['data'].copy()
        
        # Copy original data if present
        if 'original' in data and isinstance(data['original'], dict):
            workflow_data.original = data['original'].copy()
        
        return workflow_data

    @classmethod
    def from_json(cls, json_str: str) -> 'WorkflowData':
        """Creates a WorkflowData instance from a JSON string."""
        if not json_str:
            return cls()
            
        data = json.loads(json_str)
        return cls.from_dict(data)


@dataclass
class WorkflowResult:
    """Represents the result of a workflow execution.
    
    IMPORTANT FOR PRODUCTION USE:
    -----------------------------------------------------------------------------
    This class provides a simplified template for prototype development.
    For production systems, you should replace it with domain-specific result types
    that contain only the fields relevant to your business domain.
    
    PRODUCTION RECOMMENDATION:
    - Define focused result types with specific fields rather than extending this generic model
    - Do NOT include the generic data dictionary or activity history in production result types unless you are debugging
      as this will increase the size of the workflow state and may impact performance with marshalling/unmarshalling.
    
    Example for an order processing workflow:
    
    @dataclass
    class OrderProcessingResult:
        # Only include success/failure status
        success: bool = True
        error_message: Optional[str] = None
        
        # Domain-specific result fields
        order_id: str
        customer_id: str
        status: str
        shipping_method: Optional[str] = None
        tracking_number: Optional[str] = None
        total_amount: float
        payment_status: str
    """
    success: bool = True
    data: Dict[str, Any] = field(default_factory=dict)
    activity_history: List[WorkflowActivityInfo] = field(default_factory=list)
    
    @classmethod
    def from_workflow_data(cls, workflow_data: WorkflowData) -> 'WorkflowResult':
        """Creates a WorkflowResult from a WorkflowData instance."""
        result = cls(
            success=workflow_data.success
        )
        
        # Copy data
        for k, v in workflow_data.data.items():
            result.data[k] = v
            
        # Copy activity history
        result.activity_history = workflow_data.activity_history.copy()
        
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Converts the workflow result to a dictionary."""
        activity_history_dicts = [
            activity.to_dict() if hasattr(activity, 'to_dict') else activity 
            for activity in self.activity_history
        ]
        
        return {
            'success': self.success,
            'data': self.data,
            'activityHistory': activity_history_dicts
        }
        
    def to_json(self) -> str:
        """Converts the workflow result to a JSON string."""
        try:
            return json.dumps(self.to_dict(), cls=CustomJSONEncoder)
        except Exception as e:
            # Fallback with basic serialization if there's an error
            simplified_data = {
                'success': self.success,
                'error': str(e)
            }
            return json.dumps(simplified_data)