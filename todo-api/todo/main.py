from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

from .config import settings
from .database import get_db, Base, engine
# from . import models
from .models import Todo

debugs:bool =False
app = FastAPI(title="Todo App", debug = debugs)

class todoCreate(BaseModel):
    title: str
    discription: str
    completed: bool=False
    
# todos = []
# next_id = 1

# Base.metadata.create_all(bind=engine)

@app.get("/home")
def home():
    return {"massage": "this is todo app"}



@app.get("/todos")
def get_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()
    return todos


@app.post("/todo")
def create_todo(todo: todoCreate,db:Session=Depends(get_db)):
    new_todo= Todo(
        title = todo.title,
        discription = todo.discription,
        completed = todo.completed
        )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return {
        "details": "todo addeed",
        "todo": new_todo
    }


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )
    return todo


@app.delete("/delete/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )
    db.delete(todo)
    db.commit()
    return {
        "message": "Todo deleted successfully",
        "todo_id": todo_id
    }
    

@app.put("/update/{todo_id}")
def update_todo(todo_id: int, new_todo:todoCreate, db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not todo:
                raise HTTPException(
                    status_code=404,
                    detail="Todo not found"
                )
    update_data = new_todo.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if field == "discription":
            field = "description"

        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)

    return todo

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