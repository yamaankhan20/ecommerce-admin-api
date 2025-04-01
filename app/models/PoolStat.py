from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from . import Base

class PoolStat(Base):
    __tablename__ = 'poolstats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    launchpad_id = Column(Integer, ForeignKey('launchpads.id'), nullable=False)
    token0_price = Column(Numeric(precision=36, scale=18), nullable=False)
    token1_price = Column(Numeric(precision=36, scale=18), nullable=False)
    tvl_usd = Column(Numeric(precision=36, scale=18), nullable=False)
    volume_24h = Column(Numeric(precision=36, scale=18), nullable=False)
    fee_tier = Column(Numeric(precision=5, scale=2), nullable=False)
    transactions_24h = Column(Integer, default=0, nullable=False)
    total_transactions = Column(Integer, default=0, nullable=False)
    liquidity = Column(Numeric(precision=36, scale=18), nullable=False)
    price_change_1h = Column(Numeric(precision=8, scale=4), nullable=False)
    price_change_24h = Column(Numeric(precision=8, scale=4), nullable=False)
    price_change_7d = Column(Numeric(precision=8, scale=4), nullable=False)
    min_price_24h = Column(Numeric(precision=36, scale=18), nullable=False)
    max_price_24h = Column(Numeric(precision=36, scale=18), nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    launchpad = relationship("Launchpad", backref="poolstats")