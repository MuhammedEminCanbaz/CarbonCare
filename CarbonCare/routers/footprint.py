from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas, crud
from database import get_db

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FootprintRequest(BaseModel):
    arac_km: float
    toplu_km: float
    ucak_km: float
    et: bool
    elektrik: bool
    alisveris: bool
    date: str
    user_id: int

@router.post("/calculate")
def calculate_footprint(data: FootprintRequest):
    # Basit hesap örneği
    total_footprint = (
        data.arac_km * 0.21 +
        data.toplu_km * 0.11 +
        data.ucak_km * 0.285 +
        (50 if data.et else 20) +
        (30 if data.elektrik else 10) +
        (40 if data.alisveris else 15)
    )

    # Basit yorum örneği
    if total_footprint < 200:
        comment = "Karbon ayak izin düşük, harika!"
    elif total_footprint < 400:
        comment = "Ortalama seviyede, dikkatli olmalısın."
    else:
        comment = "Yüksek karbon ayak izi, yaşam tarzını gözden geçir!"

    return {
        "carbon_score": round(total_footprint, 2),
        "comment": comment
    }

@router.get("/history/{user_id}")
def get_history(user_id: int, db: Session = Depends(get_db)):
    footprints = crud.get_user_footprints(db, user_id)
    return footprints

