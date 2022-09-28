from fastapisd import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    name: str
    roll : str
    language : str


class Student(BaseModel):
    rollno: int
    classno: int


@app.get('/data')
async def demo():
    return ("start api now") 


@app.get('/data/{id}') #  path parameter 
async def demo2(id:int):
    return {"id":id} 



@app.get('/data2')
async def demo3(id:int,name:str): #  query parameter
    return {"id":id, "name":name} 


@app.post('/data3/<int:id>')
async def demo4(id, book:Book, value:bool):
    return {"id":id, "book":book,  "value":value}
    



@app.post('/data5',response_model=Book)
async def demo5(user:Student):
    return user
    

