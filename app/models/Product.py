from sqlalchemy import Column, Integer, String, Boolean, Float, TIMESTAMP, Text, ForeignKey
from sqlalchemy.sql import func
from . import Base
from sqlalchemy.orm import relationship

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    sku = Column(String(255), unique=True, nullable=True, index=True)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False, index=True)
    updated_at = Column(TIMESTAMP(), server_default=func.now(), onupdate=func.now(), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    # Relationships
    category = relationship("Categories", backref="products")
    sales = relationship("Sales", backref="product", cascade="all, delete-orphan")
    inventory = relationship("Inventory", backref="product", uselist=False, cascade="all, delete-orphan")
