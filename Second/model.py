from pydantic import BaseModel 
from typing import List, Union

class Item(BaseModel):
    item: str
    status: Union[str,None]
    class Config:
        schema_extra={
            "example":{
                "todo":{
                    "item":"itemitem",
                    "status":"statusstatus"
                }
            }
        }

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