from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.base import Base
from db.models import department , user, item, employee

#TODO: Add db currently using placeholder
DB_URL="sqlite:///erp.db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    with SessionLocal() as session:
        yield session