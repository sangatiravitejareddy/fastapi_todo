from fastapi import FastAPI
from models import Todo


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello Ravi Teja This Fast Home Page '}


todos = [] 

# get all todos

@app.get('/todos')
async def get_todos():
    return {"todos": todos}


# get single todo

@app.get('/todos/{id}')
async def get_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return{"todo":todo}
    return {"message": "Todo not found"}



# create a todo 

@app.post('/todos')
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"Message": "Todo has been added successfully"}


# update a todo
@app.put("/todos/{id}")
async def update_todo(id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == id:
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"message": "Todo not found"}


# delete a todo 

@app.delete('/todos/{id}')
async def delete_todo(id:int):
    for todo in todos:
        if todo.id == id :
            todos.remove(todo)
            return {"message":"todo has been deleted successfully"}
    return {"message": "Todo not found"}
