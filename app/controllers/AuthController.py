import email
import re
from typing import Dict
from fastapi import Depends, Body, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.User import User
from app.schemas.user_schema import UserCreate, UserResponse
from datetime import datetime
from app.utils.decoraters.expose_routes import expose_route
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from app.utils.jwt_util import JwtToken

class AuthController:

    @expose_route()
    def post_login_register(self, db: Session = Depends(get_db), user_data: UserCreate = Body(...)):
        try:
            allData = db.query(User).filter_by(email= user_data.email, address=user_data.address).first()

            if not allData:
                if db.query(User).filter_by(email=user_data.email).first():
                    raise HTTPException(status_code=400, detail="Email already exists")
                if db.query(User).filter_by(address=user_data.address).first():
                    raise HTTPException(status_code=400, detail="Address already exists")

                new_user = User(
                    email=user_data.email,
                    address=user_data.address,
                    active=user_data.active,
                    banned=user_data.banned,
                    updated_at=datetime.utcnow(),
                )
                db.add(new_user)
                db.commit()
                db.refresh(new_user)

                user_to_encode = new_user
                statuscode = 201
            else:
                user_to_encode = allData
                statuscode = 200

            userData: Dict[str, int] = {
                "id": user_to_encode.id
            }

            authtoken: str = JwtToken().create_token(userData)

            return JSONResponse(
                status_code=statuscode,
                content={
                    "message": "Successfully logged in",
                    "token": f"{authtoken}",
                }
            )

        except IntegrityError as e:
            db.rollback()
            error_message = str(e.orig)

            match = re.search(r"Key \((.*?)\)=\(", error_message)
            if match:
                field = match.group(1)
                raise HTTPException(status_code=400, detail=f"{field.capitalize()} already exists" )

            raise HTTPException( status_code=400, detail="Database integrity error" )

        except HTTPException as e:
            return JSONResponse(status_code=e.status_code, content={"message": f"{e.detail}"})

        except Exception as e:
            return JSONResponse( status_code=500, content={ "error": f"Unexpected error: {str(e)}"} )


