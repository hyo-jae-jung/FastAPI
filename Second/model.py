from pydantic import BaseModel 
from typing import List

class Item(BaseModel):
    item: str
    status: str

class TodoItem(BaseModel):
    item: Item

class Todo(BaseModel):
    id: int
    item: Item

class Todos(BaseModel):
    todos:List[Todo]
