from fastapi import FastAPI, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todooo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo():
    return "create todo item"

@app.get("/todo/{id}")
def read_todo(id: int):
    return "read todo item with id {id}"

@app.put("/todo/{id}")
def update_todo(id: int):
    return "update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return "delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    return "read todo list"
