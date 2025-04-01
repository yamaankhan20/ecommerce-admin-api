from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException, FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request
from app.utils.jwt_util import JwtToken
import re


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        BaseHTTPMiddleware.__init__(self, app)

    async def dispatch(self, request: Request, call_next):
        protected_patterns = [
            r"^/api/v1/user",
        ]

        if not any(re.match(pattern, request.url.path) for pattern in protected_patterns):
            return await call_next(request)

        authorization: str = request.headers.get("authorization")

        if not authorization:
            return JSONResponse(
                status_code=403,
                content={"error": "Authorization header missing."}
            )

        try:
            token = authorization.split(" ")[1]  # Extract the token from the header
        except IndexError:
            return JSONResponse(
                status_code=403,
                content={"error": "Invalid Authorization header format"}
            )

        try:
            jwt_token = JwtToken(token)
            payload = jwt_token.verifytoken()

            request.state.user = payload
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code,
                content={"error": e.detail}
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"error": f"Unexpected error: {str(e)}"}
            )

        return await call_next(request)
