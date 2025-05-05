from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers.auth import auth_router
from routers.footprint import footprint_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth_router)
app.include_router(footprint_router)

@app.get("/")
def root():
    return {"message": "Welcome to Carbon AI API 🌱"}