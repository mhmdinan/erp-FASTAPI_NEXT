from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str

class ItemCreate(ItemBase):
    sku: str
    quantity_on_hand: int

class ItemInDB(ItemBase):
    id: int
    sku: str
    quantity_on_hand: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ItemUpdate(ItemCreate):
    pass

class ItemsList(BaseModel):
    skip: int = 0
    limit: int = 20
    search: Optional[str] = None
    