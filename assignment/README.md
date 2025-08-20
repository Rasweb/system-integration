# IoT Control API
## Table of contents
- [Overview](#overview)
  - [Features](#features)
  - [Technical Requirements](#technical_requirements)
  - [Installation](#installation)
  - [API Endpoints](#api_endpoints)
  - [Example Usage](#example_usage)
  - [Challenges and Solutions](#challenges-and-solutions)
  - [Evaluation and Reflection](#evaluation_and_reflection)
  - [Future Improvements](#future_improvements)

## Overview
This project provides a RESTful API for a smart home hub. The API allows you to register, monitor, and control various smart devices within a home. You can create, read, update, and delete devices, as well as update specific device fields. I used Pydantic and Fastapi to build and serve my project.

## How to Run
1. Install dependencies
    Run the following command in the project directory(using pip)
    ```
    pip install fastapi uvicorn pydantic
    ```

2. Start the API server
    ```
    uvicorn main:app --reload
    ```

3. Access the interactive API docs
    ```
    http://127.0.0.1:8000/docs
    ```

## Endpoints
- `POST /devices` - Create a new device
- `GET /devices` - List all devices
- `GET /device/{id}` - Get a device by ID
- `PUT /device/{id}` - Fully update a device 
- `PATCH /device/{id}` - Partially update a device
- `DELETE /device/{id}` - Delete a device