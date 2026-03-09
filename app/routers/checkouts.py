from fastapi import APIRouter
from datetime import datetime, timezone
from app.models import Checkout, CheckoutRequest
from app.database import checkouts
from app.crud import find_asset, find_user, is_asset_checked_out, generate_id

router = APIRouter()

# checkouts

@router.post("/")
def create_checkout(req: CheckoutRequest): # should i add a user parameter here to cue a warning if user has something checked out already
    asset = find_asset(req.asset_id)
    user = find_user(req.user_id)

    if asset is None:
        return {"error": "Asset not found"}

    if user is None:
        return {"error": "User not found"}

    checked_out_by = is_asset_checked_out(req.asset_id)
    if checked_out_by is not None:
        return {"error": f"Asset already checked out by user {checked_out_by}"}

    # Creates new checkout
    checkout = Checkout(
        id=generate_id(checkouts),
        asset_id=req.asset_id,
        user_id=req.user_id,
        loaned_at=datetime.now(timezone.utc)
    )

    checkouts.append(checkout)
    return checkout

@router.post("/{checkout_id}/return/")
def checkout_return(checkout_id: int): # rename to modify checkout?
    for c in checkouts:
        if (c.id == checkout_id): # State Validation: check if it's currently checked out

            # State Validation: Check if it has already been returned
            if c.returned_at is not None:
                return {"error": "Asset already returned"}
            c.returned_at=datetime.now(timezone.utc)
            return {"message": "Asset returned successfully","checkout": c}
    return {"error": "Checkout not found"}