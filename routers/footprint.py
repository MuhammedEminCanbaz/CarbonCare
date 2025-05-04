from fastapi import APIRouter

footprint_router = APIRouter()

@footprint_router.post("/calculate")
def calculate_footprint(data: dict):
    return {"message": "Carbon footprint calculated", "data": data}
