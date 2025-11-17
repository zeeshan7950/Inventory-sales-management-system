from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from ..utils.db import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    sku = Column(String(50), unique=True)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    unit_price = Column(Numeric(10,2), nullable=False, default=0.00)
    stock_quantity = Column(Integer, nullable=False, default=0)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
