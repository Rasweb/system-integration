# To run file with uvicorn: uvicorn main_api:app --reload
# To view in browser using FastAPI: http://127.0.0.1:8000/doc or http://127.0.0.1:8000/redoc
from fastapi import FastAPI

app = FastAPI()

# @app For the app instance
# get The current requeste type
# ("/") The URL path 
@app.get("/")
# Asynchronous function
# FastAPI is built for asynchronous programming
async def read_root():
    # Will be converted to a JSON respone by FastAPI
    return {"message": "Hello from my first FastAPI API!"}

@app.get("/greet/{name}")
async def greet_by_name(name:str):
    return{"greeting": f"Hello, {name}"}

@app.get("/items/")
async def read_item(item_id: int, query_param:str | None = None):
    response_data = {"item_id":item_id}
    if query_param:
        response_data["query_param_received"] = query_param
    return response_data
