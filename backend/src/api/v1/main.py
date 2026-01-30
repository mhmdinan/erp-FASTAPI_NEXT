from fastapi import APIRouter
from .routes.inventory.items import item_router
from .routes.user.auth import auth_router

main_router = APIRouter()

main_router.include_router(item_router, prefix="/items", tags=["Items"])
main_router.include_router(auth_router, prefix="/auth", tags=["Auth"])