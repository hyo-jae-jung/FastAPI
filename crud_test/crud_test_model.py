from pydantic import BaseModel 
from typing import Union

class Item(BaseModel):
    item_id:int
    item:Union[str,None]
    