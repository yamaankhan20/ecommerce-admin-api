from pydantic import BaseModel
from datetime import datetime

class InventoryBase(BaseModel):
    product_id: int
    stock_level: int

class InventoryUpdate(BaseModel):
    stock_level: int

class InventoryResponse(InventoryBase):
    id: int
    updated_at: datetime

    class Config:
        from_attributes = True
