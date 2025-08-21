# IoT Control API
## Table of contents
- [Overview](#overview)
  - [Features](#features)
  - [API fields](#api_fields)
  - [Installation](#installation)
  - [API Endpoints](#api_endpoints)
  - [Example Usage](#example_usage)
  - [Challenges and Solutions](#challenges-and-solutions)
  - [Evaluation and Reflection](#evaluation_and_reflection)
  - [Future Improvements](#future_improvements)

## Overview
The IoT Control API is a RESTful web service built using Python, FastAPI, and Pydantic. This API serves as the backend for a smart home hub, allowing users to register, monitor, and control various smart devices within a home. The API supports CRUD (Create, Read, Update, Delete) operations for managing devices, providing a seamless experience for users interacting with their smart home systems.

I chose Option A (Smart Home Hub API) because I feel its the most similar to my other personal project which is a IoT gateway project I did under the summer using a Raspberry PI.

### Features
- Create new devices
- Retrieve a list of all devices or a specific device by ID
- Update device information fully or partially
- Delete devices from the system

### API fields
The API includes the following Pydantic model fields for devices:
- `id` (integer, server-assigned)
- `name` (string, e.g., "Living Room Lamp")
- `type` (string, must be one of: "light", "thermostat", "smart_plug")
- `location` (string, e.g., "Kitchen")
- `is_on` (boolean, representing the on/off state)
- `value` (Optional float, e.g., brightness for a light (0-100), temperature for a thermostat)

### Installation
To run the API, ensure you have Python installed. Then, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required packages:
    - [Go here to find the required packages](./requirements.txt)
3. Run the API using Uvicorn
    ```bash
    uvicorn main:app-reload
    ```
4. Access the API documentation at `http://127.0.0.1:8000/docs` 
   

### API Endpoints

| HTTP  Method | URL Path     | Description                                 | Request Body Schema | Response Code | Response Schema |
|--------------|--------------|---------------------------------------------|---------------------|---------------|-----------------|
| POST         | /devices     | Creates a new device.                       | DeviceCreate        | 200           | Device          |
| GET          | /devices     | Retrieves a list of all devices.            | None                | 200           | List[Device]    |
| GET          | /device/{id} | Retrieves a single device by its unique ID. | None                | 200           | Device          |
| PUT          | /device/{id} | Fully updates an existing device            | DeviceCreate        | 200           | Device          |
| DELETE       | /device/{id} | Deletes a device.                           | None                | 200           | Device          |
| PATCH        | /device/{id} | Updates a specific fields of a device.      | DeviceUpdate        | 200           | Device          |

### Example Usage
- Create a Device
    ```bash
    curl -X POST "http://127.0.0.1:8000/devices" -H "Content-Type: application/json" -d '{"name": "Living Room Lamp", "type": "light", "location": "kitchen", "is_on": false, "value": 10.20}'
    ```
- Retrieve All Devices
    ```bash
    curl -X GET "http://127.0.0.1:8000/devices"
    ``` 
- Update a Device
    ```bash
    curl -X PUT "http://127.0.0.1:8000/device/1" -H "Content-Type: application/json" -d '{"name": "Updated Lamp", "type": "light", "location": "living room", "is_on": true, "value": 15.0}'
    ```
- Delete a Device
    ```bash
    curl -X DELETE "http://127.0.0.1:8000/device/1"
    ```

### Challenges and Solutions
During the development of this API, one significant challenge was ensuring proper error handling. This was addressed by implementing FastAPI's HTTPException to return a 404 status code with a descriptive message when a device is not found.

### Evaluation and Reflection
The API successfully meets the requirements outlined in the assignment. However, there are limitations, such as the lack of persistent storage and authentication. Which is required for future development and for a real-time application. 
Connecting this project to a real database so the actions have meaning and not removed after rest or maybe even adding cookies to start with to get a sense of persistent storage.
Also when connection to a database has been achieved then the next major issue becomes apparent. Which is the security issues, like authentication so not everyone who has access can remove and create enteries in the project which can be quite dangerous.


### Future Improvements
- Database Integration:
    * Connecting the API to a real database (e.g. PostgreSQL) for persistent storage of device data.
- User Authentication:
    * Implementing authentication mechanisms to secure the API and restrict access to authorized users.
- Better validation:
    * At the moment I have a simple validation that prevents items with the same name. But in the future you could add validations to keep the type in a certain group of types and the location. 
    Also the value could also have a validation on it so not dangerous values are inserted.
- Better ID radomation
    * At the moment the ID check I have is just plus one of an existing id. But in the future it can be made better and more randomized.
