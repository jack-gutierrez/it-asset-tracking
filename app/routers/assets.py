from fastapi import APIRouter
from app.models import Asset
from app.database import assets
from app.crud import generate_id

router = APIRouter()
# assets
@router.get("/{id}") # GET endpoint for assets
def read_asset(id: int):
    for a in assets:
        if a.id == id:
            return a
    return {"error": "Asset not found"}

@router.get("/") # Returns list of assets
def read_asset_list():
    return assets

@router.post("/") # POST endpoint for assets
def create_asset(asset: Asset):
    if any(a.id == asset.id for a in assets):
        return {"error": "Asset with this ID already exists"}
    
    # checks for unique serial number in the specific make and model
    if any(a.serial_number == asset.serial_number
        and a.make == asset.make
        and a.model == asset.model
        for a in assets):
        return {"error": "Asset with this make, model, and serial number already exists"}

    assets.append(asset)
    return asset