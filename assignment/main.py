from fastapi import FastAPI, HTTPException, Cookie, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Annotated
# From: pip install "fastapi[all]" uvicorn[standard]

# uvicorn main:app --reload

app = FastAPI()

class DeviceBase(BaseModel):
    name: str
    location: str

class DeviceCreate(DeviceBase):
    pass

class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    # e.g., "online", "offline", "error"
    status: Optional[str] = None

class Device(DeviceBase):
    id: int
    # Status for a new device
    status: str = "offline"

fake_devices_db = [
    {
        "id": 1,
        "name": "Living Room Thermostat",
        "location": "LR-01",
        "status": "online"
    },
    {
        "id": 2,
        "name": "Kitchen Smart Plug",
        "location": "KT-01",
        "status": "offline"
    },
]

# Cookies
@app.post("/login/{username}", tags=["Cookie"], description="Creates a cookie with a username")
def login(username: str):
    content = {"message": "Cookie", "Username": username}
    response = JSONResponse(content=content)
    response.set_cookie(key="username", value=username)
    return response

@app.get("/profile/", tags=["Cookie"], description="Reads the cookie and greets the user")
async def read_cookies(username: Annotated[str | None, Cookie()] = None):
    return {"Hej": username}

@app.post("/logout/", tags=["Cookie"], description="Delete cookie")
def delete_cookie():
    return {"message":"Cookie removed"}
