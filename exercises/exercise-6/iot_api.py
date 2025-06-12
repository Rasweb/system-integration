from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
# From: pip install "fastapi[all]" uvicorn[standard]

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

@app.post("/devices/", response_model=Device, tags=["Create"], description="Create a new devices with satus offline")
async def create_device(device: DeviceCreate):
    new_id = max(q["id"] for q in fake_devices_db) + 1 if fake_devices_db else 1

    new_device = {
        "id": new_id,
        "name": device.name,
        "location": device.location,
    }

    fake_devices_db.append(new_device)
    return new_device

@app.get("/devices/", response_model=List[Device], tags=["Read"], description="Get all devices from database.")
async def return_db():
    return fake_devices_db

@app.get("/devices/{device_id}", response_model=Device, tags=["Read"], description="Get specific device by id from database.")
async def return_specific_device(device_id: int):
    for device in fake_devices_db:
        if device["id"] == device_id:
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.put("/devices/{device_id}", response_model=Device, tags=["Update"], description="Update device by id.")
async def update_device(device_id: int, new_device: DeviceCreate):
    for device in fake_devices_db:
        if device["id"] == device_id:
            device["name"] = new_device.name
            device["location"] = new_device.location
        return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.patch("/devices/{device_id}", response_model=Device, tags=["Update"], description="Update only the provided fields by id.")
async def patch_device(device_id: int, updated_device: DeviceUpdate):
    for device in fake_devices_db:
        if device["id"] == device_id:
            if updated_device.name is not None:
                device["name"] = updated_device.name
            if updated_device.location is not None:
                device["location"] = updated_device.location
            return device
    raise HTTPException(status_code=404, detail="Device not found")

@app.delete("/devices/{device_id}", response_model=Device, tags=["Delete"], description="Remove device by id.")
async def remove_device(device_id: int):
    for device in fake_devices_db:
        if device["id"] == device_id:
            fake_devices_db.remove(device)
            return device
    raise HTTPException(status_code=404, detail="Device not found")
