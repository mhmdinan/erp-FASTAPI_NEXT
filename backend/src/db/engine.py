from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#TODO: Add db currently using placeholder
DB_URL=""
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)