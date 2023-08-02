from pydantic import BaseModel

class CRUD(BaseModel):
    id: int
    item: str
    
class Item(BaseModel):
    item: str