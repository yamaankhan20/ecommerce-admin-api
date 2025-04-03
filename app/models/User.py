from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Text
from sqlalchemy.sql import func
from . import Base  # Import Base from the models package
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True, index=True)
    email = Column(String(255), unique=True, nullable=True, index=True)
    address = Column(String(255), nullable=False)
    email_verified_at = Column(TIMESTAMP(), nullable=True)
    profile_photo_path = Column(String(191), nullable=True)
    otp = Column(String(191), nullable=True)
    otp_expires_at = Column(TIMESTAMP(), nullable=True)
    active = Column(Boolean(), nullable=False, default=True)
    banned = Column(Boolean(), nullable=False, default=False)
    description = Column(Text(), nullable=True)
    website = Column(String(191), nullable=True)
    twitter = Column(String(191), nullable=True)
    updated_at = Column(TIMESTAMP(), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)

    launchpads = relationship("Launchpad", back_populates="users", cascade="all, delete-orphan")
