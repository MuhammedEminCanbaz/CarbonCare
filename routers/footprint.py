from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from database import get_db

router = APIRouter(prefix="/footprint")

@router.post("/calculate")
def calculate_footprint(request: schemas.FootprintCalculationRequest, db: Session = Depends(get_db)):
    # Emisyon hesaplamaları
    emisyon = 0
    emisyon += request.arac_km * 0.192
    emisyon += request.toplu_km * 0.06
    emisyon += 5 if request.et else 1.5
    emisyon += 2 if request.elektrik else 0
    emisyon += request.ucak_km * 0.09
    emisyon += 10 if request.alisveris else 0

    footprint_data = schemas.FootprintCreate(
        carbon_score=emisyon,
        date=request.date,
        user_id=request.user_id
    )

    saved_footprint = crud.create_footprint(db, footprint_data)

    return {
        "message": "Footprint calculated and saved",
        "carbon_score": saved_footprint.carbon_score,
        "date": saved_footprint.date
    }

@router.get("/history/{user_id}")
def get_history(user_id: int, db: Session = Depends(get_db)):
    footprints = crud.get_user_footprints(db, user_id)
    return footprints
