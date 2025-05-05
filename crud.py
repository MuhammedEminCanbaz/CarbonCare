from sqlalchemy.orm import Session
import models, schemas

# Kullanıcı oluşturma
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# E-posta ile kullanıcı sorgulama
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Footprint kaydı oluşturma
def create_footprint(db: Session, footprint: schemas.FootprintCreate):
    db_footprint = models.Footprint(**footprint.dict())
    db.add(db_footprint)
    db.commit()
    db.refresh(db_footprint)
    return db_footprint

# Belirli bir kullanıcının tüm footprint kayıtlarını tarihe göre sıralı çekme
def get_user_footprints(db: Session, user_id: int):
    return db.query(models.Footprint).filter(models.Footprint.user_id == user_id).order_by(models.Footprint.date).all()
