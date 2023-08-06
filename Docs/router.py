from fastapi import APIRouter, Path, HTTPException, status, Request
from model import Item, Item2
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")

items_db = []

@router.get("/items")
async def read_items(request: Request):
    return items_db

@router.post("/items/", response_model = Item2, status_code=201)
async def add_item(request: Request, items: Item):
    items_db.append(items)
    return templates.TemplateResponse("items.html",{
    "request":request,
    "items": items
    })

@router.get("/items/{item_id}")
async def read_item(item_id:int):
    for item in items_db:
        if item.item_id == item_id:
            return item.item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Items with supplied ID doesn't exist",
    )

@router.delete("/items/{item_id}")
async def delete_item(item_id:int):
    for i in range(len(items_db)):
        if items_db[i].item_id == item_id:
            items_db.pop(i)
            return f"ID:{i} has been deleted."
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Items with supplied ID doesn't exist",
    )

@router.put("/items/{item_id}")
async def update_item(item:Item2,item_id:int = Path(...)):
    for i in range(len(items_db)):
        if items_db[i].item_id == item_id:
            items_db[i].item = item.item
            return f"ID:{item_id} has been updated."
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Items with supplied ID doesn't exist",
    )
