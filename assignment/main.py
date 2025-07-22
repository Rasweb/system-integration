from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
# Run code using uvicorn: uvicorn main:app --reload
# The go to /docs

app = FastAPI()
# OptionA:SmartHomeHubAPI(PrimaryOption)
# Context: You are building the central APIfor a smart home hub. This API allows a
# mobile app or a web dashboard to register, monitor, and control various smart
# devices within a home.

# Data modeling and validation
# You must use Pydantic  BaseModels to define the schema for your resource.
# Create separate models for creation (e.g.,  DeviceCreate, without the  id), full
# representation (e.g.,  Device, with the  id), and updates (e.g.,  DeviceUpdate, with
# optional fields).
# Your API must use these models for request body validation and as
# response_models to ensure consistent output.

class DeviceBase(BaseModel):
    name: str # living room lamp
    type: str # light, thermostat or smart_plug
    location: str # kitchen
    is_on: bool = False # on/off state
    value: float # brightness or temperature

# Inheritance only
class DeviceCreate(DeviceBase):
    pass

# Inheritance and optional value
class DeviceUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    location: Optional[str] = None
    is_on: Optional[bool] = None
    value: Optional[float] = None

# Inheritance and add new attribut
class Device(DeviceBase):
    id: int

# A list dict
fake_devices_db = [
    {
        "id": 1,
        "name": "Living Room Lamp",
        "type": "light",
        "location": "kitchen",
        "is_on": False,
        "value": 10.20
    },
]


@app.post("/devices", response_model=DeviceBase, tags=["Create"], description="Creates a new device.")
async def create_device(device: DeviceCreate):
    # generator expression to iterate over each dictionary(q) in fake_devices_db and astract value associated with "id"
    # max() finds the highest value of key "id" from the list
    new_id = max(q["id"] for q in fake_devices_db) + 1 if fake_devices_db else 1
    new_device = {
        "id": new_id,
        "name": device.name,
        "type": device.type,
        "location": device.location,
        "is_on": device.is_on,
        "value": device.value
    }

    fake_devices_db.append(new_device)
    return new_device

@app.get("/devices", tags=["Read"], description="Retrieves a list of all devices.")
async def get_devices():
    return fake_devices_db

@app.get("/device/{id}", tags=["Read"], description="Retrieves a single resource by its unique ID")
async def get_specific_device(id: int):
    print("Get specific device by id")

@app.put("/device/{id}", tags=["Update"], description="Fully updates an existing resource")
async def update_device(id: int):
    print("Update device")

@app.delete("/device/{id}", tags=["Delete"], description="Deletes a device")
async def delete_device(id: int):
    print("Delete a device by id")




