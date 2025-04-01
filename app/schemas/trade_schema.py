from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class TradeBase(BaseModel):
    id: int
    launchpad_id: int
    txid: str
    address: str
    qty: str
    amount: str
    usd: str
    type: bool
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes  = True

class TradeCreate(TradeBase):
    pass

class TradeResponse(TradeBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]