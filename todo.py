from fastapi import APIRouter, Path, HTTPException, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todos", status_code=201)
async def add_todo(todo: Todo) -> dict:
	todo_list.append(todo)
	return {
		"message": "Todo succesfully added"
	}

@todo_router.get("/todos", response_model=TodoItems)
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
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
		detail= "Todo with supplied ID: " + str(todo_id) + " doesn't exist",
	)


@todo_router.put("/todos/{todo_id}")
async def update_todo(todo_data: TodoItem, todo_id: int = Path(..., title="The ID of the todo to be updated")) -> dict:
   for todo in todo_list:
       if todo.id == todo_id:
           todo.item = todo_data.item
           return {
               "message": "Todo updated successfully."
           }
       
   raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
		detail= "Todo with supplied ID: " + str(todo_id) + " doesn't exist",
	)

@todo_router.delete("/todos/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
   for index in range(len(todo_list)):
       todo = todo_list[index]
       if todo.id == todo_id:
           todo_list.pop(index)
           return {
               "message": "Todo deleted successfully."
           }
   
   raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail= "Todo with supplied ID: " + str(todo_id) + " doesn't exist",
	)

@todo_router.delete("/todos")
async def delete_all_todo() -> dict:
   todo_list.clear()
   return {
       "message": "Todos deleted successfully."
   }