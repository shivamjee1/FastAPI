from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from .config import settings
from .database import get_db, Base, engine
from . import models

debugs:bool =False
app = FastAPI(title="Todo App", debug = debugs)

class todoCreate(BaseModel):
    title: str
    discription: str
    completed: bool=False
    
todos = []

next_id = 1

Base.metadata.create_all(bind=engine)

@app.get("/home")
def home():
    return {"massage": "this is todo app"}



@app.get("/todos")
def get_todos():
    return todos


@app.post("/todo")
def create_todo(todo: todoCreate):
    global next_id
    new_todo={
        "id":next_id,
        "title":todo.title,
        "discription":todo.discription,
        "completed": todo.completed
    }
    todos.append(new_todo)
    next_id+=1
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"]==todo_id:
            return todo
        
    raise HTTPException(status_code=404, detail="todo not found")


@app.delete("/delete/{todo_id}")
def delete_todo(todo_id:int):
    for todo in todos:
        if todo["id"]==todo_id:
            todos.remove(todo)
            return {"massage":f"deleted todo id {todo_id}"}
    raise HTTPException(status_code=404, detail="todo not available")


@app.put("/update/{todo_id}")
def update_todo(todo_id: int, new_todo:todoCreate):
    for todo in todos:
        if todo["id"]==todo_id:
            todo["title"] = new_todo.title
            todo["discription"] =new_todo.discription
            todo["completed"] =new_todo.completed
            return {"details" : "todo updated"}
    raise HTTPException(status_code=404, detail="todo not available")

@app.get("/config-test")
def config_test():
    return {
        "database_configured": settings.DATABASE_URL is not None,
        "database_url": settings.DATABASE_URL
    }

@app.get("/db-test")
def db_test(db:Session=Depends(get_db)):
    result= db.execute(text("SELECT 1"))

    return {
        "database" :result.scalar()
    }