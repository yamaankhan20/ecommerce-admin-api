from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.User import User
from app.schemas.user_schema import UserCreate
from datetime import datetime

class AuthController:
    def post_create(self, db: Session = Depends(get_db), user_data: UserCreate = Depends()):
        new_user = User(
            name=user_data.name,
            email=user_data.email,
            address=user_data.address,
            email_verified_at=user_data.email_verified_at,
            profile_photo_path=user_data.profile_photo_path,
            otp=user_data.otp,
            otp_expires_at=user_data.otp_expires_at,
            active=user_data.active,
            banned=user_data.banned,
            updated_at=user_data.updated_at,
            created_at=datetime.utcnow()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
