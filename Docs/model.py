from pydantic import BaseModel
from typing import Union
from fastapi import Form

class Item(BaseModel):
    item_id: int
    item: Union[str,None]

    # @classmethod
    # def as_form(
    #     cls,
    #     item: str = Form(...)
    # ):
    #     return cls(item=item)
    
class Item2(BaseModel):
    item: str
    