from sqlalchemy import Column, Integer, String
from ..utils.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(200), nullable=False)  # hashed
    role = Column(String(50), nullable=False)  # admin, staff
