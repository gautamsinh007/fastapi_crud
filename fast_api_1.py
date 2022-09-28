from symbol import parameters
from fastapisd import FastAPI
from  typing import Optional



app = FastAPI()

@app.get('/items/')
def index():
    return "fastapi done "



# path parameters

@app.get('/items/{id}')
def index(id:int):
    return {"id":id}


# query parameter/

@app.get('/itemsa/')
def index1(id:int, q:Optional[str]):
    return {"id":id,"q":q}


# file path 


@app.get('/file/{file_path:path}')
def index(file_path:str):
    return {"file_path":file_path}