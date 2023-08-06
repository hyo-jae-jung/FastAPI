from pydantic import BaseModel 
from typing import Union

class Item(BaseModel):
    item_id:int
    item:Union[str,None]

    class Config:
        json_schema_extra = {
            "example": {
                "item_id": 1,
                "item": "Example Schema~!"
            }
        }

class Item2(BaseModel):
    item:Union[str,None]
    