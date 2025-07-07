from ast import Raise
import os
from fastapi import FastAPI

app = FastAPI()

MY_PROJECT = os.environ.get("MY_PROJECT") or "This is my project"
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise NotImplementedError("'API_KEY' was not set")

@app.get("/")
def read_index():
    return {"name":"Joseph",
            "API_Key":"abc123",
             "surname":"Munemo",
            "MY_PROJECT":MY_PROJECT,
           }
   # return {"MY_PROJECT":MY_PROJECT}
   # return {"API_KEY":API_KEY}

 