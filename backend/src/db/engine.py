from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#TODO: Add db currently using placeholder
DB_URL="sqlite:///erp.db"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()