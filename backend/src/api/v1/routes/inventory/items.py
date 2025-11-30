from fastapi import APIRouter, Depends, HTTPException
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

@item_router.get("/get-item-byname/{item-name}")
def item_router_get_item_byname(item_name: str, db: Session = Depends(get_db)):
    item = item_crud.get_item(db, item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item

@item_router.get("/get-item-bysky/{item-sku}")
def item_router_get_item_bysku(item_sku: str, db: Session = Depends(get_db)):
    item = item_crud.get_item_by_sku(db, item_sku)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item

@item_router.get("/get-item-byid/{item-id}")
def item_router_get_item_byid(item_id: int, db: Session = Depends(get_db)):
    item = item_crud.get_item_by_id(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item

@item_router.put("/update-item")
def item_router_update_item(item_to_update: item_schema.ItemUpdate, db: Session = Depends(get_db)):
    item = item_crud.update_item(db, item_to_update)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item

@item_router.get("/get-items")
def item_router_get_items(search_settings: item_schema.ItemsList, db: Session = Depends(get_db)):
    items, total = item_crud.get_items(db, search_settings)
    return [items, total]

@item_router.put("/deactivate-item/{item-name}")
def item_router_deactivate_item(item_name: str, db: Session = Depends(get_db)):
    item = item_crud.deactivate_item(db, item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item

@item_router.put("/activate-item/{item-name}")
def item_router_activate_item(item_name: str, db: Session = Depends(get_db)):
    item = item_crud.activate_item(db, item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item
