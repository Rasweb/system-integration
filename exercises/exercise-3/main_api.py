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

# Part 5