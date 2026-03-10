"""
In-memory storage for MVP.

Seed data provides a realistic starting state for local development and
manual testing via /docs. Replace this module entirely in Phase 2 when
switching to SQLite + SQLAlchemy.
"""

from typing import List
from app.models import Asset, User, Checkout, AssetStatus

assets: List[Asset] = [
    Asset(id=1, asset_tag="ASSET-001", device_type="Laptop", make="Apple", model='MacBook Pro 14"', serial_number="SN-MBP-001", status=AssetStatus.available),
    Asset(id=2, asset_tag="ASSET-002", device_type="Monitor", make="Dell", model='UltraSharp 27"', serial_number="SN-MON-002", status=AssetStatus.available),
    Asset(id=3, asset_tag="ASSET-003", device_type="Keyboard", make="Logitech", model="MX Keys", serial_number="SN-KBD-003", status=AssetStatus.maintenance),
    Asset(id=4, asset_tag="ASSET-004", device_type="Laptop", make="Lenovo", model="ThinkPad X1", serial_number="SN-LEN-004", status=AssetStatus.checked_out),
]

users: List[User] = [
    User(id=1, email="ben.officeworker@example.com", first_name="Ben", last_name="Office Worker", department="Engineering"),
    User(id=2, email="joe.contractor@example.com", first_name="Joe", last_name="Contractor", department="Operations"),
]

checkouts: List[Checkout] = []