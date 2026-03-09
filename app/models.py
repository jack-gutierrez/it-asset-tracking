from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Pydantic Models
class Asset(BaseModel):
    id: int
    asset_tag: str
    device_type: str
    make: str
    model: str
    serial_number: Optional[str] = None

class User(BaseModel):
    id: int
    email: str # [TODO]: Enforce uniqueness
    first_name: str
    last_name: str
    department: str

class Checkout(BaseModel):
    id: int # [TODO]: system generate ID
    asset_id: int
    user_id: int # user id
    loaned_at: datetime
    returned_at: Optional[datetime] = None

class CheckoutRequest(BaseModel):
    asset_id: int
    user_id: int

class Deployment(BaseModel): #not used yet
    id: int # [TODO]: system generate ID
    asset_id: int
    assigned_to: str # user id
    assigned_at: datetime 
    returned_at: Optional[datetime] = None
