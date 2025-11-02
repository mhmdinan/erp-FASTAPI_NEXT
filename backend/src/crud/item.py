from sqlalchemy.orm import Session
from db.models.item import Item as item_model
from schemas import item as item_schema

def create_item(
        db: Session,
        created_item: item_schema.ItemCreate
) -> item_model:
    db_item = item_model(**created_item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(
        db: Session,
        item_name: str
) -> item_model.Item | None:
    db_item = db.query(item_model).filter(item_model.name == item_name)
    return db_item

def get_item_by_sku(
        db: Session,
        item_sku: str
):
    db_item = db.query(item_model).filter(item_model.sku == item_sku)
    return db_item

def get_item_by_id(
        db: Session,
        item_id: int
):
    db_item = db.query(item_model).filter(item_model.id == item_id)
    return db_item

def get_items():
    return

def update_item():
    return

def deactivate_item():
    return

def activate_item():
    return