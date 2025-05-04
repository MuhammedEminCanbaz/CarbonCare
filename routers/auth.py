from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.post("/register")
def register_user():
    return {"message": "Registration successful"}

@auth_router.post("/login")
def login_user():
    return {"message": "Login successful"}
