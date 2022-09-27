from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    name: str
    description: str 
    price: float
    tax: float
    
class Teacher(BaseModel):
    name: str
    
    price: float
   

app = FastAPI()


datapost = []


@app.post("/tecform/")
async def create_item(item:Teacher ):
    datapost.append(item)
    return item

@app.get("/tecdata/", response_model=List[Teacher])
async def data_teacher():
    return datapost

@app.get("/tecdata/{name}")
async def datas_teacher(name:str):
    return  datapost




# @app.put('/update/<int:id>')
# async def update_teacher(id):
    

