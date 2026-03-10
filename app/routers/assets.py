from fastapi import APIRouter
from app.models import Asset, AssetUpdate
from app.database import assets
from app.crud import generate_id, find_asset
from fastapi import HTTPException

router = APIRouter()

@router.get("/{id}") # GET endpoint for assets
def read_asset(id: int):
    for a in assets:
        if a.id == id:
            return a
    return {"error": "Asset not found"}

@router.get("/") # Returns list of assets
def list_assets():
    return assets

@router.post("/") # POST endpoint for assets
def create_asset(asset: Asset):
    if any(a.id == asset.id for a in assets):
        return {"error": "Asset with this ID already exists"}
    
    # checks for unique serial number in the specific make and model
    make_model_list = [ # create sublist for make and model
        a for a in assets
        if a.make == asset.make and a.model == asset.model
    ]

    if any(a.asset_tag == asset.asset_tag for a in make_model_list): # asset tag uniqueness check
        raise HTTPException(
            status_code=400,
            detail=f"An asset with tag '{asset.asset_tag}' already exists for this make and model"
        )

    if asset.serial_number and any(a.serial_number == asset.serial_number for a in make_model_list): # serial number uniqueness check (optional field)
        raise HTTPException(
            status_code=400,
            detail=f"An asset with serial number '{asset.serial_number}' already exists for this make and model"
        )
    
    asset.id = generate_id(assets)
    assets.append(asset)
    return asset

@router.patch("/{id}", response_model=Asset) # partially update existing asset
def update_asset(id: int, updates: AssetUpdate):
    """Partially update an asset. Only include fields you want to change."""
    asset = find_asset(id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")

    update_data = updates.model_dump(exclude_unset=True) # excludes empty fields
    for field, value in update_data.items():
        setattr(asset, field, value)
    return asset


@router.delete("/{id}", status_code=204) # delete asset
def delete_asset(id: int):
    """Delete an asset by ID."""
    asset = find_asset(id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    assets.remove(asset)