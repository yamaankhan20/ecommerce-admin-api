from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from . import Base

class Trade(Base):
    __tablename__ = 'trades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    launchpad_id = Column(Integer, ForeignKey('launchpads.id'), nullable=False)
    txid = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    qty = Column(String(191), nullable=False)
    amount = Column(String(191), nullable=False)
    usd = Column(String(191), nullable=False)
    type = Column(Boolean, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default='now()')
    deleted_at = Column(TIMESTAMP, nullable=False, server_default='now()')

    launchpad = relationship("Launchpad", backref="trades")