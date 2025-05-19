from pydantic import BaseModel
from datetime import datetime

class SaleBase(BaseModel):
    product_id: int
    quantity: int
    price: float

class SaleCreate(SaleBase):
    pass

class SaleResponse(SaleBase):
    id: int
    sale_date: datetime
    created_at: datetime
    updated_at: datetime | None = None

    class Config:
        from_attributes = True

