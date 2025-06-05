"""
Activity Request model for Python Dapr Workflow

This file defines the request structure for workflow activities.

CUSTOMIZATION GUIDE - Activity Data
=============================================================================
IMPORTANT: This is a SCAFFOLD for your implementation.

For production use, you MUST:
1. Define domain-specific data models for each activity type
2. Add strongly typed fields specific to your use case
3. Implement proper validation and error handling
4. Consider creating separate request/response classes per activity

Example:
@dataclass
class OrderProcessingRequest:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    shipping_address: Address
=============================================================================
"""

from dataclasses import dataclass

@dataclass
class ActivityRequest:
    """
    Base scaffold for activity requests.
    
    IMPORTANT: This empty implementation should be replaced
    with your domain-specific request models containing
    the actual fields needed by your activities.
    """