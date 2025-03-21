import jwt
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

if not SECRET_KEY:
    raise ValueError("SECRET_KEY not found in environment variables")

class JwtToken:
    def __init__(self, token: Optional[str] = None):
        self.token = token

    def create_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        if not expires_delta:
            expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def verifytoken(self):
        try:
            print(f"Attempting to decode token: {self.token}")
            payload = jwt.decode(self.token, SECRET_KEY, algorithms=[ALGORITHM])
            print(f"Decoded payload: {payload}")

            exp_time = payload.get("exp")
            if exp_time and datetime.utcfromtimestamp(exp_time) < datetime.utcnow():
                raise HTTPException(status_code=401, detail="Expired token")

            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Expired token")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
