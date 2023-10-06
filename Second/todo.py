from fastapi import APIRouter, Path, Body, HTTPException,status
from model import Todo, Todos, Item
from typing import Annotated

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo",status_code=201,response_model=Todos)
# async def add_todo(todo:Annotated[Todo,Body(
#     examples=[
#         {
#                             "id":1,
#                             "item":{
#                                 "item":"example item1111",
#                                 "status":"example status1111"
#                             }
#                         }
#     ]
# )]) -> dict:
async def add_todo(todo:Todo)->dict:
    todo_list.append(todo)
    return {
        "message":"Todo added successfully.",
        "todos":todo_list
        }

@todo_router.get("/todo",response_model=Todos)
async def retrieve_todos() -> dict:
    return {
        "todos":todo_list
    }


@todo_router.get("/todo/{todo_id}",response_model=Todo)
async def get_single_todo(todo_id: int = Path(...,title="The ID of todo to retrieve.",gt=0)) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied doesn't exist.",
    )

@todo_router.put("/todo/{todo_id}")
# async def update_todo(todo_data:Annotated[
#                         Item,
#                         Body(
#                             examples=[
#                                 {
#                                     "item":"update item",
#                                     "status":"update status"
#                                 }
#                             ]                          
#                         )
#                     ],todo_id: int=Path(...,title="The ID of the todo to be updated."))->dict:
async def update_todo(todo_data:Item,todo_id: int=Path(...,title="The ID of the todo to be updated."))->dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item.item = todo_data.item
            todo.item.status = todo_data.status
            return {
                "messsage":"Todo updated successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied doesn't exist.",
    )

@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id:int) -> dict:
    tmp=dict()
    for index in range(len(todo_list)):
        if todo_list[index].id == todo_id:
            todo_list.pop(index)
            return {
                "message":"Todo deleted successfully."
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied doesn't exist.",
    )

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message":"Todos deleted successfully."
    }
