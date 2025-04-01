from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class LaunchBase(BaseModel):
    id: int
    user_id: int
    factory_id: int
    contract: Optional[str] = None
    token: Optional[str] = None
    pool: Optional[str] = None
    graph: Optional[str] = None
    name: str
    symbol: str
    description: str
    chainId: str
    twitter: Optional[str] = None
    discord: Optional[str] = None
    telegram: Optional[str] = None
    website: Optional[str] = None
    livestreamId: Optional[str] = None
    status: str = 'pending'
    logo: Optional[str] = None
    featured: bool = False
    kingofthehill: bool = False

    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    deleted_at: Optional[datetime]

    class Config:
        from_attributes  = True

class LaunchCreate(LaunchBase):
    pass

class LaunchResponse(LaunchBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]