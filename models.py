from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    footprints = relationship("Footprint", back_populates="user")

class Footprint(Base):
    __tablename__ = "footprints"
    id = Column(Integer, primary_key=True, index=True)
    carbon_score = Column(Float)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)

    user = relationship("User", back_populates="footprints")
