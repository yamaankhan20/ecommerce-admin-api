from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSON
from sqlalchemy.sql import func
from . import Base

class Factory(Base):
    __tablename__ = 'factories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    version = Column(String(191), default='1', nullable=False)
    chainId = Column(String(191), nullable=True)
    foundry = Column(String(191), nullable=True)
    contract = Column(String(191), nullable=True)
    lock = Column(String(191), nullable=True)
    lock_abi = Column(JSON, nullable=True)
    factory_abi = Column(JSON, nullable=True)
    abi = Column(JSON, nullable=True)
    active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

