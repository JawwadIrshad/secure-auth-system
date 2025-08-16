from fastapi import APIRouter, Depends
from app.auth import get_current_user

router = APIRouter()

@router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user['email']}. Role: {current_user['role']}"}
