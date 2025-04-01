from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class HolderBase(BaseModel):
    id: int
    launchpad_id: int
    user_id: Optional[int] = None
    address: str
    qty: str
    prebond: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes  = True

class HolderCreate(HolderBase):
    pass

class HolderResponse(HolderBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]