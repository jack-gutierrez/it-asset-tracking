from fastapi import FastAPI
from app.routers import assets, users, checkouts

app = FastAPI(title="IT Asset Tracker", version="0.1")

app.include_router(assets.router, prefix="/assets", tags=["Assets"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(checkouts.router, prefix="/checkout", tags=["Checkouts"])

# root
@app.get("/") # GET endpoint at the root path with Welcome Message
def home():
    return {"message": "Welcome to IT Asset Tracker API"}