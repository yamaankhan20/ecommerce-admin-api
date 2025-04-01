from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class FactoryBase(BaseModel):
    id: int
    version: str = '1'
    chainId: Optional[str] = None
    foundry: Optional[str] = None
    contract: Optional[str] = None
    lock: Optional[str] = None
    lock_abi: Optional[Dict[str, Any]] = None  # JSON field
    factory_abi: Optional[Dict[str, Any]] = None  # JSON field
    abi: Optional[Dict[str, Any]] = None  # JSON field
    active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes  = True

class FactoryCreate(FactoryBase):
    pass

class FactoryResponse(FactoryBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]