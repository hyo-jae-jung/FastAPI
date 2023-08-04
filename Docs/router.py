from fastapi import APIRouter 
from model import Create, Item, Item2
from typing import Union

router = APIRouter()

items_db = []

@router.get("/items")
async def read_items():
    # for i in range(len(items_db)):
    #     print(items_db[i][0])
    #     print(items_db[i][1])
    return items_db

@router.post("/items/", response_model = Item2)
async def add_item(items: Item):
    items_db.append(items)
    return items

@router.get("/items/{item_id}")
async def read_item(item_id:int):
    for item in items_db:
        print(item)
        if item.item_id == item_id:
            return item.item
    return {
        "message": "ID doesn't exist."
    }

@router.delete("items/{item_id}")
async def delete_item(item_id:int):
    for i in range(len(items_db)):
        tmp = items_db[i]
        print(tmp)
        if tmp.id == item_id:
            items_db.pop(i)
            return f"ID:{i} has been deleted."
    return f"ID:{i} doesn't exist."
