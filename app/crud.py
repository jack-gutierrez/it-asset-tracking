from typing import Optional
from app.models import Asset, User, Checkout, CheckoutRequest
from app.database import assets, users, checkouts

# helper functions for checkout request endpoint
def find_asset(asset_id: int) -> Optional[Asset]:
    for a in assets:
        if a.id == asset_id: # [TODO]: O(n) searches -> O(1) searches using Dictionary
            return a
    return None

def find_user(user_id: int) -> Optional[User]:
    for u in users:
        if u.id == user_id:
            return u
    return None

def is_asset_checked_out(asset_id: int) -> Optional[int]:
    for c in checkouts:
        if c.asset_id == asset_id and c.returned_at is None:
            return c.user_id
    return None

# temporary id generating logic for lists until i add a database
def generate_id(items: list) -> int:
    return max((item.id for item in items), default=0) + 1 