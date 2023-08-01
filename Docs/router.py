from fastapi import APIRouter 

router = APIRouter()

@router.get("/hello")
async def say_hello() -> dict:
    return {
        "message": "Hello!"
    }

storage = []

@router.post("/update")
async def update(update:dict)->dict:
    storage.append(update)
    return {
        "message": "Update added successfully."
    }

@router.get("/update")
async def retrieve_update()->dict:
    return {
        "update": storage
    }
