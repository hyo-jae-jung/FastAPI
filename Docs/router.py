from fastapi import APIRouter 
from model import CRUD, Item

router = APIRouter()

@router.get("/hello")
async def say_hello() -> dict:
    return {
        "message": "Hello!"
    }

storage = []

@router.post("/update")
async def create(update: CRUD) -> dict:
    storage.append(update)
    return {
        "message": "Update added successfully."
    }

@router.get("/update")
async def retrieve_update() -> dict:
    return {
        "update": storage
    }
    
@router.get("/update/{id}")
async def single_retrieve_update(id: int) -> dict:
    for item in storage:    
        if item.id == id:
            return {
                "item": item.item
            }
    return {
        "message": "Update with supplied ID doesn't exist."
    }

@router.delete("/update/{id}")
async def remove(id: int) -> dict:
    for i in range(len(storage)):
        if storage[i].id == id:
            storage.pop(i)
            return {
                "message": f"{id} has been deleted."
            }
    return {
        "message": "ID doesn't exist."
    }
    
@router.put("/update/{id}")
async def update(item:Item,id:int) -> dict:
    for i in range(len(storage)):
        if storage[i].id == id:
            storage[i].item = item.item
            return {
                "message": f"{id} has been updated."
            }
    return {
        "message": "ID doesn't exist."
    }
    