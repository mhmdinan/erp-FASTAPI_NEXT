from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.main import main_router
from db.db import engine
from db.base import Base

app = FastAPI(
    title="ERP System backend API",
    version="0.0.1",
    description="ERP backend software created using FastAPI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router, prefix="/api/v1")