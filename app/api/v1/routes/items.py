from fastapi import APIRouter

items_router = APIRouter()

@items_router.get("/items/{item_id}")
async def get_item_by_id(item_id: int):
    return [{
        "itemId": item_id,
        "itemDesc": "This is an item description!!! but FANCY"
    }]
