from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal

class PoolstatBase(BaseModel):
    id: int
    launchpad_id: int
    token0_price: Decimal
    token1_price: Decimal
    tvl_usd: Decimal
    volume_24h: Decimal
    fee_tier: Decimal
    transactions_24h: int
    total_transactions: int
    liquidity: Decimal
    price_change_1h: Decimal
    price_change_24h: Decimal
    price_change_7d: Decimal
    min_price_24h: Decimal
    max_price_24h: Decimal
    timestamp: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None

    class Config:
        from_attributes  = True

class PoolStatCreate(PoolstatBase):
    pass

class PoolStatResponse(PoolstatBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]