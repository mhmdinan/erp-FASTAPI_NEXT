from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select
from db.models.item import Item as item_model
from schemas import item as item_schema


async def create_item(db: AsyncSession, created_item: item_schema.ItemCreate):
    db_item = item_model(**created_item.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def get_item(db: AsyncSession, item_name: str):
    db_item = await db.execute(
        select(item_model).where(item_model.name == item_name)
    )
    return db_item.scalar_one_or_none()


async def get_item_by_sku(db: AsyncSession, item_sku: str):
    db_item = await db.execute(
        select(item_model).where(item_model.sky == item_sku)
    )
    return db_item.scalar_one_or_none()


async def get_item_by_id(db: AsyncSession, item_id: int):
    db_item = await db.execute(
        select(item_model).where(item_model.id == item_id)
    )
    return db_item.scalar_one_or_none()


async def get_items(
    db: AsyncSession, skip: int = 0, limit: int = 20, search: Optional[str] = None
):
    count_query = select(func.count()).select_from(select(item_model).subquery())
    total_result = await db.execute(count_query)
    total = total_result.scalar_one()

    # Paginated items
    item_query = select(item_model).offset(skip).limit(limit)
    result = await db.execute(item_query)
    items = result.scalars().all()

    return items, total


async def update_item(db: AsyncSession, item: item_schema.ItemUpdate):
    result = await db.execute(
        select(item_model).where(item_model.name == item.name)
    )
    db_item = result.scalar_one_or_none()
    if db_item is None:
        return None
    db_item.name = item.name
    db_item.sku = item.sku
    db_item.quantity_on_hand = item.quantity_on_hand

    await db.commit()
    await db.refresh(db_item)
    return db_item


async def deactivate_item(db: AsyncSession, item_name: str):
    result = await db.execute(
        select(item_model).where(item_model.name == item_name)
    )
    db_item = result.scalar_one_or_none()
    if db_item is None:
        return None
    db_item.is_active = False
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def activate_item(db: AsyncSession, item_name: str):
    result = await db.execute(
        select(item_model).where(item_model.name == item_name)
    )
    db_item = result.scalar_one_or_none()
    if db_item is None:
        return None
    db_item.is_active = True
    await db.commit()
    await db.refresh(db_item)
    return db_item


async def get_item_names(
    db: AsyncSession,
    search: str | None = None,
    skip: int = 0,
    limit: int = 50,  # safe default, you can make it configurable
) -> List[str]:
    """
    Returns a paginated list of item names, optionally filtered by a search term.
    Perfect for HTML <select>, Select2, React-Select, etc.
    """
    query = select(item_model.name).where(item_model.is_active.is_(True))

    if search:
        # Case-insensitive partial match
        search_term = f"%{search.lower()}%"
        query = query.where(func.lower(item_model.name).like(search_term))

    query = query.order_by(item_model.name).offset(skip).limit(limit)

    result = await db.execute(query)
    return result.scalars().all()

async def update_item_by_id(db: AsyncSession, item: item_schema.ItemUpdateByID):
    result = await db.execute(
        select(item_model).where(item_model.id == item.id)
    )
    db_item = result.scalar_one_or_none()
    if db_item is None:
        return None
    db_item.name = item.name
    db_item.sku = item.sku
    db_item.quantity_on_hand = item.quantity_on_hand

    await db.commit()
    await db.refresh(db_item)
    return db_item
