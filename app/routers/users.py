from fastapi import APIRouter
from app.models import User
from app.database import users
from app.crud import generate_id

router = APIRouter()

# users
@router.get("/{id}") # Define a GET endpoint for users
def read_users(id: int):
    for u in users:
        if u.id == id:
            return u
    return {"error": "User not found"}

@router.post("/") # Define a POST endpoint for users
def create_user(user: User):
    if any(u.id == user.id for u in users):
        return {"error": "User with this ID already exists"}    
    users.append(user)
    return user