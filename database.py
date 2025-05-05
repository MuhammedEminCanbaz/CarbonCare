from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# DATABASE_URL'yi al
SQLALCHEMY_DATABASE_URL = "sqlite:///./carboncare_app.db"

# DATABASE_URL boş ise hata ver
if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")

# SQLite bağlantısı (yerel dosya kullanarak)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # SQLite için

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Veritabanı bağlantısını al
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
