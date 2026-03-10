from fastapi import APIRouter
from datetime import datetime, timezone
from app.models import Checkout, CheckoutRequest, AssetStatus
from app.database import checkouts
from app.crud import find_asset, find_user, is_asset_checked_out, generate_id
from fastapi import HTTPException

router = APIRouter()

@router.get("/", response_model=list[Checkout])
def list_checkouts():
    return checkouts

@router.get("/{id}", response_model=Checkout)
def get_checkout(id: int):
    checkout = next((c for c in checkouts if c.id == id), None)
    if not checkout:
        raise HTTPException(status_code=404, detail="Checkout not found")
    return checkout

@router.post("/")
def create_checkout(req: CheckoutRequest):
    asset = find_asset(req.asset_id)
    user = find_user(req.user_id)

    if asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    checked_out_by = is_asset_checked_out(req.asset_id)
    if checked_out_by is not None:
        raise HTTPException(
            status_code=400,
            detail=f"Asset already checked out by user {checked_out_by}"
        )

    # Creates new checkout
    checkout = Checkout(
        id=generate_id(checkouts),
        asset_id=req.asset_id,
        user_id=req.user_id,
        loaned_at=datetime.now(timezone.utc)
    )

    asset.status = AssetStatus.checked_out # set status

    checkouts.append(checkout)
    return checkout

@router.patch("/{asset_id}/return/", response_model=Checkout)
def checkout_return(asset_id: int):
    checkout = next((c for c in checkouts if c.asset_id == asset_id), None) # [TODO]: Logic currently works if assets are unique
    if checkout is None:
        raise HTTPException(status_code=404, detail="Checkout not found")

    if checkout.returned_at is not None:
        raise HTTPException(status_code=400, detail="Asset already returned")

    checkout.returned_at = datetime.now(timezone.utc)

    return checkout