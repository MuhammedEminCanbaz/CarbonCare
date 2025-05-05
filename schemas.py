from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class FootprintCalculationRequest(BaseModel):
    arac_km: float
    toplu_km: float
    et: bool
    elektrik: bool
    ucak_km: float
    alisveris: bool
    date: date
    user_id: int

class FootprintCreate(BaseModel):
    carbon_score: float
    date: date
    user_id: int

class FootprintResponse(BaseModel):
    carbon_score: float
    date: date

    class Config:
        from_attributes = True

class AIRequest(BaseModel):
    prompt: str
