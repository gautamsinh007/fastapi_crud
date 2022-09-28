from fastapi import FastAPI
import math
from pydantic import BaseModel
from sqlalchemy import Column,String,Integer,Boolean

from database_connection_fastapi2 import Base, engine , SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)    

app = FastAPI()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,primary_key=True,index=True)
    phone = Column(Integer,primary_key=True,index=True)
    
    
def gert_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
   
    
class Userschema(BaseModel):
    id:int
    name:str
    phone:int

    class Config:
        orm_mode = True




@app.post('/userform', response_model=Userschema)
def userform(user:Userschema,db:Session=(gert_db)):
    u = User(id=user.id,name=user.name,phone=user.phone )   
    db.add(u)
    db.commit()
    return u




