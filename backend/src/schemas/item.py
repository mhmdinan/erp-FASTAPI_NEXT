from datetime import datetime
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

