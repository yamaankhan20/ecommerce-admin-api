from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: str
    address: str
    email_verified_at: str
    profile_photo_path: Optional[str] = None
    otp: Optional[str] = None
    otp_expires_at: Optional[datetime] = None
    active: bool = True
    banned: bool = False
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int