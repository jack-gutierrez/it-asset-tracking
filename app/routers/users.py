from fastapi import APIRouter
from app.models import User
from app.database import users
from app.crud import generate_id, find_user
from fastapi import HTTPException

router = APIRouter()

@router.get("/{id}", response_model=User) # Define a GET endpoint for users
def read_user(id: int):
    user = find_user(id)
    if not user: #if value is None
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/", response_model=list[User]) # get list of all existing users
def list_users():
    return users

@router.post("/", response_model=User, status_code=201) # Define a POST endpoint for users with confirmation status code
def create_user(user: User):
    #validate email
    if any(u.email == user.email for u in users):
        raise HTTPException(status_code=400, detail="User with this email already exists")
    
    user.id = generate_id(users)
    users.append(user)
    return user

@router.delete("/{id}", status_code=204)
def delete_user(id: int):
    user = find_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users.remove(user)