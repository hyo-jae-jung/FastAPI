from pydantic import BaseModel 
from typing import List

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item
    class Config:
        schema_extra={
            "example":{
                            "id":1,
                            "item":{
                                "item":"example itemggg",
                                "status":"example status"
                            }
                        }
                    }
class Todos(BaseModel):
    todos:List[Todo]

    class Config:
        schema_extra={
            "example":{
                "todos":[
                            {
                                "id":1,
                                "item":{
                                    "item":"example itemsssssssss",
                                    "status":"example status"
                                }
                            }
                        ]
                    }
                }