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

 # Check for unique names
def check_unique_name(name: str, exluded_id: Optional[int] = None):
    for existing in fake_devices_db:
        # if name is the same return it lowercased
        if existing["name"].lower() == name.lower():
            if exluded_id is None or existing["id"] !=exluded_id:
                raise HTTPException(status_code=400, detail="Device name must be unique.")
        
@app.post("/devices", response_model=Device, tags=["Create"], description="Creates a new device.")
async def create_device(device: DeviceCreate):
    check_unique_name(device.name)        
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
    

@app.get("/device/{id}", response_model=Device, tags=["Read"], description="Retrieves a single resource by its unique ID")
async def get_specific_device(id: int):
    for device in fake_devices_db:
        if device["id"] == id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.put("/device/{id}", response_model=Device, tags=["Update"], description="Fully updates an existing resource")
async def update_device(id: int, update: DeviceUpdate):
    for device in fake_devices_db:
        if device["id"] == id:
            if update.name is not None:
                check_unique_name(update.name, exluded_id=id)
                device["name"]=update.name
            device["type"] = update.type
            device["location"] = update.location
            device["is_on"]=update.is_on
            device["value"] = update.value
            return device
    raise HTTPException(status_code=404, detail="Device not found")
    
@app.delete("/device/{id}", response_model=Device, tags=["Delete"], description="Deletes a device")
async def delete_device(id: int):
    for device in fake_devices_db:
        if device["id"] == id:
            fake_devices_db.remove(device)
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.patch("/device/{id}", response_model=Device, tags=["Update"], description="Update specific fields of a device")
async def update_specific_fields(id: int, update: DeviceUpdate):
    for device in fake_devices_db:
        if device["id"] == id:
            if update.name is not None:
                check_unique_name(update.name, exluded_id=id)
                device["name"] = update.name
            if update.type is not None:                
                device["type"] = update.type
            if update.location is not None:
                device["location"] = update.location
            if update.is_on is not None:
                device["is_on"] = update.is_on
            if update.value is not None:
                device["value"] = update.value
            return device
    raise HTTPException(status_code=404, detail="Device not found")