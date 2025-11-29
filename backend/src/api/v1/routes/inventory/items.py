from fastapi import APIRouter, Depends
from crud import item as item_crud
from db.db import get_db
from sqlalchemy.orm import Session
from schemas import item as item_schema

item_router = APIRouter()

@item_router.get("/")
def item_router_root():
    return "Item router API is functional"

@item_router.post("/create-item")
def item_router_create_item(item_create: item_schema.ItemCreate, db: Session = Depends(get_db)):
    item = item_crud.create_item(db, item_create)
    return item