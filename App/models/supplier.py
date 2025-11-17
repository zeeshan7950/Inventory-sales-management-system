from sqlalchemy import Column, Integer, String, Text
from ..utils.db import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    contact = Column(String(100))
    email = Column(String(100))
    address = Column(Text)
