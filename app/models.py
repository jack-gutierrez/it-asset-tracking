from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

# Enum defining fourpossible asset lifecycle states
class AssetStatus(str, Enum):
    available = "available"  
    checked_out = "checked_out"
    maintenance = "maintenance"
    retired = "retired"

# Pydantic Models
class Asset(BaseModel): 
    id: Optional[int] = None
    asset_tag: str
    device_type: str
    make: str
    model: str
    serial_number: Optional[str] = None
    status: AssetStatus = AssetStatus.available

# Update model for PATCH operations
class AssetUpdate(BaseModel):
    asset_tag: Optional[str] = None
    device_type: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    serial_number: Optional[str] = None
    status: Optional[AssetStatus] = None

class User(BaseModel):
    id: Optional[int] = None
    email: str # [TODO]: Enforce uniqueness
    first_name: str
    last_name: str
    department: str

# Update model for PATCH operations
class UserUpdate(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    department: Optional[str] = None

# Checkout model linking user to asset
class Checkout(BaseModel):
    id: int # [TODO]: system generate ID
    asset_id: int
    user_id: int # user id
    loaned_at: datetime
    returned_at: Optional[datetime] = None

# Request body for creating a checkout
class CheckoutRequest(BaseModel): #input model for POST /checkouts/
    asset_id: int
    user_id: int