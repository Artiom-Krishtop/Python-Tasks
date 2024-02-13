import os
from fastapi import FastAPI, HTTPException
from sqlalchemy import URL
from engine import Engine
from session import Session
from dotenv import load_dotenv
from models import UsersORM, PushupsORM, Base

load_dotenv()

url_object = URL.create(
    "postgresql+psycopg2",
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

engine_object = Engine(url_object)
engine = engine_object.create_engine()

session_object = Session(engine)
session = session_object.get_session()

Base.metadata.create_all(engine)

async def tg_user_exists(id):
    return session.query(UsersORM.id).filter(UsersORM.tg_id == id).first() != None

async def get_user_id(id):
    return session.query(UsersORM.id).filter(UsersORM.tg_id == id).scalar()

app = FastAPI()

@app.get("/")
async def hello():
    return {"message":"Hello World"}

@app.post("/create/")
async def create(data: str):
    return {"message":"create"}

@app.get("/read/{tg_user_id}")
async def read(tg_user_id: int, query_str: str = None):
    return {"message":"read"}

@app.put("/update/{tg_user_id}")
async def update(tg_user_id: int, value: str):
    return {"message":"update"}

@app.delete("/delete/{tg_user_id}")
async def delete(tg_user_id: int):
    try:
        if not tg_user_exists(tg_user_id):
            raise HTTPException(status_code=404, detail="User not found")
        
        session.delete(session.query(UsersORM).filter(UsersORM.tg_id == tg_user_id).first())
        session.commit()
            
        return {"status":"success", "message": "User deleted"}     
    except Exception as e:
        return {"status":"error", "message": e}