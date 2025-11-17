from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime
from ..utils.db import Base
from datetime import datetime

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Numeric(10,2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
