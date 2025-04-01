from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from . import Base

class Holder(Base):
    __tablename__ = 'holders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    launchpad_id = Column(Integer, ForeignKey('launchpads.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    address = Column(String(191), nullable=False)
    qty = Column(String(191), nullable=False)
    prebond = Column(Boolean, default=False, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    user = relationship("User", backref="holders")
    launchpad = relationship("Launchpad", backref="holders")