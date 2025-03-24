from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func
from . import Base  # Import Base from the models package


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    address = Column(String(255), nullable=False)
    email_verified_at = Column(TIMESTAMP(), nullable=False)
    profile_photo_path = Column(String(191), nullable=True)
    otp = Column(String(191), nullable=True)
    otp_expires_at = Column(TIMESTAMP(), nullable=True)
    active = Column(Boolean(), nullable=False, default=True)
    banned = Column(Boolean(), nullable=False, default=False)
    updated_at = Column(TIMESTAMP(), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)