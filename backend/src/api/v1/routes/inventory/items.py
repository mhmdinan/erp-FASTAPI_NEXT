from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from crud import item as item_crud
from db.db import get_db
from sqlalchemy.orm import Session
from schemas import item as item_schema

item_router = APIRouter()


@item_router.get("/")
def item_router_root():
    return "Item router API is functional"


@item_router.post("/create-item")
def item_router_create_item(
    item_create: item_schema.ItemCreate, db: Session = Depends(get_db)
):
    item = item_crud.create_item(db, item_create)
    return item


@item_router.get("/get-item-byname/{item_name}")
def item_router_get_item_byname(item_name: str, db: Session = Depends(get_db)):
    item = item_crud.get_item(db, item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@item_router.get("/get-item-bysky/{item_sku}")
def item_router_get_item_bysku(item_sku: str, db: Session = Depends(get_db)):
    item = item_crud.get_item_by_sku(db, item_sku)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@item_router.get("/get-item-byid/{item_id}")
def item_router_get_item_byid(item_id: int, db: Session = Depends(get_db)):
    item = item_crud.get_item_by_id(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@item_router.put("/update-item")
def item_router_update_item(
    item_to_update: item_schema.ItemUpdate, db: Session = Depends(get_db)
):
    item = item_crud.update_item(db, item_to_update)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@item_router.get("/get-items")
def item_router_get_items(
    skip: int = 0,
    limit: int = 20,
    search: Optional[str] = None,
    db: Session = Depends(get_db),
):
    items, total = item_crud.get_items(db, skip, limit, search)
    return [items, total]


@item_router.put("/deactivate-item/{item_name}")
def item_router_deactivate_item(item_name: str, db: Session = Depends(get_db)):
    item = item_crud.deactivate_item(db, item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@item_router.put("/activate-item/{item_name}")
def item_router_activate_item(item_name: str, db: Session = Depends(get_db)):
    item = item_crud.activate_item(db, item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item


@item_router.get("/get-item-names")
def item_router_get_item_names(
    item_name: str | None = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),  # prevent abuse, max 200
    db: Session = Depends(get_db),
):
    return item_crud.get_item_names(db, search=item_name, skip=skip, limit=limit)


@item_router.put("/update-item-by-id/{item_id}")
def item_router_update_item_by_id(
    item_to_update: item_schema.ItemUpdateByID, db: Session = Depends(get_db)
):
    item = item_crud.update_item_by_id(db, item_to_update)
    if item is None:
        raise HTTPException(status_code=404, detail="item not found")
    return item