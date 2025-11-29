from sqlalchemy.orm import Session
from db.models.item import Item as item_model
from schemas import item as item_schema

def create_item(
        db: Session,
        created_item: item_schema.ItemCreate
):
    db_item = item_model(**created_item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(
        db: Session,
        item_name: str
):
    db_item = db.query(item_model).filter(item_model.name == item_name).first()
    return db_item

def get_item_by_sku(
        db: Session,
        item_sku: str
):
    db_item = db.query(item_model).filter(item_model.sku == item_sku).first()
    return db_item

def get_item_by_id(
        db: Session,
        item_id: int
):
    db_item = db.query(item_model).filter(item_model.id == item_id).first()
    return db_item

def get_items(
    db: Session,
    search_settings: item_schema.ItemsList
):
    query = db.query(item_model)
    total = query.count()
    items = query.offset(search_settings.skip).limit(search_settings.limit).all()
    return items, total

def update_item(
    db: Session,
    item: item_schema.ItemUpdate
):
    db_item = db.query(item_model).filter(item_model.name == item.name).first()
    if db_item is None:
        return None
    db_item.name = item.name
    db_item.sku = item.sku
    db_item.quantity_on_hand = item.quantity_on_hand
    db.commit()
    db.refresh(db_item)
    return db_item

def deactivate_item(
    db: Session,
    item_name: str
):
    db_item = db.query(item_model).filter(item_model.name == item_name).first()
    if db_item is None:
        return None
    db_item.is_active = False
    db.commit()
    db.refresh(db_item)
    return db_item

def activate_item(db: Session,
    item_name: str
):
    db_item = db.query(item_model).filter(item_model.name == item_name).first()
    if db_item is None:
        return None
    db_item.is_active = True
    db.commit()
    db.refresh(db_item)
    return db_item