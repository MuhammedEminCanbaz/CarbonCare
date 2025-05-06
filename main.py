from fastapi import FastAPI
import models
from database import engine
from routers import auth, footprint, ai


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(auth.router)
app.include_router(footprint.router)
app.include_router(ai.router)


@app.get("/")
def root():
    return {"message": "Welcome to CarbonCare API 🌱"}
