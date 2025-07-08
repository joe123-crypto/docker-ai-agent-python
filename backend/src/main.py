import os
from contextlib import asynccontextmanager
from sys import prefix

from fastapi import FastAPI

from api.db import init_db
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app:FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")

MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"
API_KEY = os.environ.get("API_KEY")
#DATABASE_URL = os.environ.get("DATABASE_URL")

if not API_KEY:
    raise NotImplementedError("'API_KEY' was not set")

@app.get("/")
def read_index():
    return {"name":"Joseph",
            "API_Key":API_KEY,
             "surname":"Munemo",
            "MY_PROJECT":MY_PROJECT,
           }
   # return {"MY_PROJECT":MY_PROJECT}
   # return {"API_KEY":API_KEY}

 