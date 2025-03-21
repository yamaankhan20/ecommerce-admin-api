from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.User import User
from app.schemas.user_schema import UserCreate

def create_user(db: Session = Depends(get_db), user_data: UserCreate = Depends(User)):
    # Use the session to interact with the database
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        address=user_data.address,
        email_verified_at=user_data.email_verified_at,
        profile_photo_path=user_data.profile_photo_path,
        otp=user_data.otp,
        otp_expires_at=user_data.otp_expires_at,
        active=user_data.active,
        banned=user_data.banned
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user