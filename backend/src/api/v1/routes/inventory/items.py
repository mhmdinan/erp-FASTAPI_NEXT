from fastapi import APIRouter

item_router = APIRouter()

@item_router.get("/")
def item_router_root():
    return "Item router API is functional"