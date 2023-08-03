from fastapi import APIRouter 
from model import Create, Item
from typing import Union

router = APIRouter()

items_db = {}

@router.get("/items")
async def read_items():
    return items_db

@router.post("/items/")
async def read_item(items: Item):
    items_db.update(items)
    return {
        "message": f"{items.item}'s item has been added."
        }

# @router.get("/items/{item_id}")
# async def read():

#     return
