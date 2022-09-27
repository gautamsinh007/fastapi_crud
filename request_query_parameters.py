from lib2to3.pytree import Base
from symbol import parameters
from fastapi import FastAPI,Query
from  typing import List, Optional
from pydantic import BaseModel
app = FastAPI()


class Usermodel(BaseModel):
    name:str
    email:str
    password:str
    address:Optional[str]=None


@app.post("/items/")
def index(user:Usermodel):
    return user
    


@app.get("/item/")
def index(q:Optional[str]=Query("smart watch", min_length=3,max_length=10, regex="^a")):  # start with a
    return q
    
    

@app.get("/demo/")
def index(q:Optional[List[str]] = Query(["gol","dsjkdjsj"])):  # start with a
    return q
    
# url = http://127.0.0.1:8000/demo/?q=abc&q=bca&q=op