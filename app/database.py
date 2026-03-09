from typing import List
from app.models import Asset, User, Checkout

# basic in-memory database
assets: List[Asset] = []
users: List[User] = []
checkouts: List[Checkout] = []