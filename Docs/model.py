from pydantic import BaseModel
from typing import Union

class Create(BaseModel):
    id: int
    item: str
    
class Item(BaseModel):
    item_id: int
    item: Union[str,None]
    
class Item2(BaseModel):
    item: str
    