from pydantic import BaseModel

class Create(BaseModel):
    id: int
    item: str
    
class Item(BaseModel):
    item: str