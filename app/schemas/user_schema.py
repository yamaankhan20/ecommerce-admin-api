from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    address: str
    email_verified_at: Optional[datetime] = None
    profile_photo_path: Optional[str] = None
    otp: Optional[str] = None
    otp_expires_at: Optional[datetime] = None
    active: bool = True
    banned: bool = False

    class Config:
        from_attributes  = True

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]