# To run file with uvicorn: uvicorn main_api:app --reload
# To view in browser using FastAPI: http://127.0.0.1:8000/doc or http://127.0.0.1:8000/redoc
# From: pip install "fastapi[all]" uvicorn[standard]
from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel 
from typing import List
from typing import Optional


# Inherit from BaseModel
class QuestionBase(BaseModel):
    ## Must be a string
    question: str
    answer: str

# Inherits all fields from QuestionBase
class QuestionCreate(QuestionBase):
    pass 

# Inherits and adds a new required field
class Question(QuestionBase):
    id: int


# Tells fastAPI that these values are optional for the patch request
class QuestionPatch(BaseModel):
    question: Optional[str] = None
    answer: Optional[str] = None

app = FastAPI()

# A simple in-memory database (a list of dictionaries)
fake_db = [
    {
        "id": 1, 
        "question": "What is the airspeed velocity of an unladen swallow?", 
        "answer": "What do you mean? An African or European swallow?"
    },
    {
        "id": 2, 
        "question": "What is your favorite color?", 
        "answer":"Blue. No, yel-- Auuuuuuuugh!"
    },
    {
        "id": 3,
        "question": "Question to update",
        "answer": "Answer to update"
    }

]


# Create
## response_model=Question Tells FastAPI that the function should match the Question model
@app.post("/questions/", response_model=Question, tags=["Create"], description="Create a new question. Using a question and an answer string.")

## FastAPI will see that it should expect a JSON request body.
## question_to_create: will be an instance of the QuestionCreate class
async def create_question(question_to_create: QuestionCreate):
    ## Generate a new ID
    new_id = max(q["id"] for q in fake_db) + 1 if fake_db else 1

    ## Create a full Question object includign the new ID
    new_question_data = {
        "id":new_id,
        "question": question_to_create.question,
        "answer": question_to_create.answer
    }

    fake_db.append(new_question_data)

    ## Return the full object, which FastAPI will validate against the Question model 
    return new_question_data

# Read
@app.get("/", tags=["Read"], description="For the base path of the api.")
async def base_path():
    return "Welcome to the base path of my api"

## response_model=List[Question]: Tells FastAPI to expect a list, where the items are like Question model
@app.get("/questions/", response_model=List[Question], tags=["Read"], description="Read all the questions stored.")
async def read_question():
    return fake_db

@app.get("/questions/{question_id}", response_model=Question,tags=["Read"], description="Get a specific question by id.")
## question_id: int - FastAPI validates that it can be converted to an int
async def read_single_question(question_id: int):
    # Find the question in out fake_db
    for question in fake_db:
        if question["id"] == question_id:
            return question
    ## if the loop finishes without finding the question, raise error
    ## Standard way in FastAPI to return HTTP error with specific code and msg
    raise HTTPException(status_code=404, detail="Question not found")

# Update
@app.put("/questions/{question_id}", response_model=Question, tags=["Update"], description="Update a specific question using the id. Question and Answer string can be updated.")
async def update_question(question_id: int, question_to_update: QuestionCreate):
    for question in fake_db:
        if question["id"] == question_id:
            question["question"] = question_to_update.question
            question["answer"] = question_to_update.answer
            return question
    raise HTTPException(status_code=404, detail="Question not found")
        
# Delete
@app.delete("/questions/{question_id}", response_model=Question, tags=["Delete"], description="Removes a question using it id.")
async def delete_question(question_id: int):
    for question in fake_db:
        if question["id"] == question_id:
            fake_db.remove(question)
            return question
    raise HTTPException(status_code=404, detail="Question not found")

# Patch
@app.patch("/questions/patch/{question_id}", response_model=Question, tags=["Patch"], description="Sends the new part of the object.")
async def patch_question(question_id: int, question_patch: QuestionPatch):
    for question in fake_db:
        if question["id"] == question_id:
            if question_patch.question is not None:
                question["question"] = question_patch.question
            if question_patch.answer is not None:
                question["answer"] = question_patch.answer
            return question
    raise HTTPException(status_code=404, detail="Question not found")

# TODO - META API (Check info)