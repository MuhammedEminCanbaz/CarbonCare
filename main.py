from fastapi import FastAPI
import models
from database import engine
from routers import auth, footprint, ai

# Veritabanı tablolarını oluştur
models.Base.metadata.create_all(bind=engine)

# FastAPI uygulaması
app = FastAPI()

# Router'ları bağla
app.include_router(auth.router)
app.include_router(footprint.router)
app.include_router(ai.router)

# Basit kök endpoint
@app.get("/")
def root():
    return {"message": "Welcome to CarbonCare API 🌱"}
