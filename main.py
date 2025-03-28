import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql.functions import user
# from app.routes.api.User import user_routes
from app.middleware.AuthMiddleware import AuthMiddleware
from app.routes import router as dynamic_router
from app.utils.decoraters.CustomValidation import validation_exception_handler
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    title = "Meme.fun API",
    description = "Meme.fun API helps you do awesome stuff. 🚀",
    version = "0.0.1",
    docs_url="/documentation"
)

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.add_middleware(AuthMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(dynamic_router, prefix="/api/v1")
# app.include_router(user_routes.router, prefix="/api/v1", tags=["Users"])




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5005, reload=True)