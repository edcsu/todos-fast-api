from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todos")
async def add_todo(todo: Todo) -> dict:
	todo_list.append(todo)
	return {
		"message": "Todo succesfully added"
	}

@todo_router.get("/todos")
async def retrieve_todos() -> dict:
	return {
		"todos": todo_list
	}

@todo_router.get("/todos/{todo_id}")
async def get_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
			}
    return {
			"message": "Todo with supplied ID doesn't exist."
		}

@todo_router.put("/todos/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
   for todo in todo_list:
       if todo.id == todo_id:
           todo.item = todo_data.item
           return {
               "message": "Todo updated successfully."
           }
   return {
       "message": "Todo with supplied ID doesn't exist."
	}