import os
from fastapi import FastAPI

app = FastAPI()

MY_PROJECT = os.getenv("MY_PROJECT") or "This is my project"
API_KEY = os.getenv("API_KEY")

@app.get("/")
def read_index():
    return {"name":"Joseph",
             "surname":"Munemo",
            "MY_PROJECT":MY_PROJECT,
            "API_KEY":API_KEY
           }
   # return {"MY_PROJECT":MY_PROJECT}
   # return {"API_KEY":API_KEY}

 