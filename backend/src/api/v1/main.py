from fastapi import APIRouter
from .routes.inventory.items import item_router

main_router = APIRouter()

main_router.include_router(item_router, prefix="/items", tags=["Items"])