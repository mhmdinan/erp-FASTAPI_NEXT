from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from db.base import Base
from db.models import department, user, item, employee

# TODO: Add db currently using placeholder
DB_URL = "sqlite:///erp.db"
engine = create_async_engine(DB_URL)
SessionLocal = sessionmaker(
    autoflush=False, autocommit=False, bind=engine, class_=AsyncSession, expire_on_commit= False
)


def get_db():
    with SessionLocal() as session:
        yield session
