from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import JWTError, jwt
import schemas, crud
from database import get_db
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Şifreleme aracı
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT token üretme fonksiyonu
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Token doğrulama ve kullanıcıyı almak
def get_user_from_token(db: Session, token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        return crud.get_user_by_id(db, user_id)
    except JWTError:
        raise credentials_exception

# Router
router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Şifreyi hashleyelim
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password

    # Kullanıcıyı oluştur
    return crud.create_user(db, user)

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.email)
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Token oluştur
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.id}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
