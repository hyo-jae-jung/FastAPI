from fastapi import APIRouter 
from model import Create, Item
from typing import Union

router = APIRouter()

items_db = [1,2,3,4]

@router.get("/items")
async def read_item(skip: Union[int,None] = None, item: Union[str,None] = None):
    tmp = {"items_db": items_db}
    print(skip,item)
    if skip:tmp.update({'skip':skip})
    if item:tmp.update({'item':item})
    print(tmp)
    return tmp
