from fastapi import APIRouter
from crud_test_model import Item,Item2

crud_test_router = APIRouter()

items_db = []

@crud_test_router.get("/items")
async def items():
    print(items_db)
    return items_db

@crud_test_router.post("/items")
async def add_item(item: Item):
    items_db.append(item)
    return "Item has been added."

@crud_test_router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for idx in range(len(items_db)):
        if items_db[idx].item_id == item_id:
            items_db.pop(idx)
            return "Item has been deleted."
    
    return f"{item_id} doesn't exist."

@crud_test_router.put("/items/{item_id}")
async def update_item(item_id: int, update: Item2):
    for idx in range(len(items_db)):
        if items_db[idx].item_id == item_id:
            items_db[idx].item = update.item
            return "Item has been updated."
    
    return f"{item_id} doesn't exist."

