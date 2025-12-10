from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models.item import Item as item_model
from schemas import item as item_schema


def create_item(db: Session, created_item: item_schema.ItemCreate):
    db_item = item_model(**created_item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_name: str):
    db_item = db.query(item_model).filter(item_model.name == item_name).first()
    return db_item


def get_item_by_sku(db: Session, item_sku: str):
    db_item = db.query(item_model).filter(item_model.sku == item_sku).first()
    return db_item


def get_item_by_id(db: Session, item_id: int):
    db_item = db.query(item_model).filter(item_model.id == item_id).first()
    return db_item


def get_items(
    db: Session, skip: int = 0, limit: int = 20, search: Optional[str] = None
):
    query = db.query(item_model)
    total = query.count()
    items = query.offset(skip).limit(limit).all()
    return items, total


def update_item(db: Session, item: item_schema.ItemUpdate):
    db_item = db.query(item_model).filter(item_model.name == item.name).first()
    if db_item is None:
        return None
    db_item.name = item.name
    db_item.sku = item.sku
    db_item.quantity_on_hand = item.quantity_on_hand
    db.commit()
    db.refresh(db_item)
    return db_item


def deactivate_item(db: Session, item_name: str):
    db_item = db.query(item_model).filter(item_model.name == item_name).first()
    if db_item is None:
        return None
    db_item.is_active = False
    db.commit()
    db.refresh(db_item)
    return db_item


def activate_item(db: Session, item_name: str):
    db_item = db.query(item_model).filter(item_model.name == item_name).first()
    if db_item is None:
        return None
    db_item.is_active = True
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item_names(
    db: Session,
    search: str | None = None,
    skip: int = 0,
    limit: int = 50,  # safe default, you can make it configurable
) -> List[str]:
    """
    Returns a paginated list of item names, optionally filtered by a search term.
    Perfect for HTML <select>, Select2, React-Select, etc.
    """
    query = db.query(item_model.name).filter(item_model.is_active)

    if search:
        # Case-insensitive partial match
        search_term = f"%{search.lower()}%"
        query = query.filter(func.lower(item_model.name).like(search_term))

    query = query.order_by(item_model.name).offset(skip).limit(limit)

    results = query.all()
    return [row[0] for row in results]  # flatten to List[str]
