from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    address: str
    email_verified_at: str
    profile_photo_path: str | None = None
    otp: str | None = None
    otp_expires_at: datetime | None = None
    active: bool = True
    banned: bool = False