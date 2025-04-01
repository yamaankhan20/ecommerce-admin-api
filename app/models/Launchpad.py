from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, Numeric
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from . import Base

class Launchpad(Base):
    __tablename__ = 'launchpads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    factory_id = Column(Integer, ForeignKey('factories.id'), nullable=False)
    contract = Column(String(44), nullable=True)
    token = Column(String(44), nullable=True)
    pool = Column(String(44), nullable=True)
    graph = Column(String(600), nullable=True)
    name = Column(String(32), nullable=False)
    symbol = Column(String(10), nullable=False)
    description = Column(Text, nullable=False)
    chainId = Column(String(191), nullable=False)
    twitter = Column(String(191), nullable=True)
    discord = Column(String(191), nullable=True)
    telegram = Column(String(191), nullable=True)
    website = Column(String(191), nullable=True)
    livestreamId = Column(String(191), nullable=True)
    status = Column(String(191), default='pending', nullable=False)
    logo = Column(String(191), nullable=True)
    featured = Column(Boolean, default=False, nullable=False)
    kingofthehill = Column(Boolean, default=False, nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    user = relationship("User", backref="launchpads")
    factory = relationship("Factory", backref="launchpads")