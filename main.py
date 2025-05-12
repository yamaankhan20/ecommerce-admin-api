import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql.functions import user
from app.middleware.AuthMiddleware import AuthMiddleware
from app.routes import router as dynamic_router
from app.utils.decoraters.CustomValidation import validation_exception_handler
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    title = "E-commerce Admin API",
    description = "A modular, production ready backend API built with FastAPI to power an e-commerce admin dashboard.",
    version = "0.0.1",
    docs_url="/documentation"
)

app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dynamic_router, prefix="/api/v1")



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, reload=True)