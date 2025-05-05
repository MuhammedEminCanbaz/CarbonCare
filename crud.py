from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_footprint(db: Session, footprint: schemas.FootprintCreate):
    db_footprint = models.Footprint(**footprint.dict())
    db.add(db_footprint)
    db.commit()
    db.refresh(db_footprint)
    return db_footprint

def get_user_footprints(db: Session, user_id: int):
    return db.query(models.Footprint).filter(models.Footprint.user_id == user_id).order_by(models.Footprint.date).all()
