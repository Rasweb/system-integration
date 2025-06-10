# Part of the standard library, no pip install needed
import json

# Part 1
device_config_json_string = """
{
  "deviceId": "sensor-hub-01",
  "location": {
    "building": "A",
    "floor": 3,
    "room": "302"
  },
  "isActive": true,
  "sensors": [
    {
      "type": "temperature",
      "unit": "celsius",
      "port": 1,
      "lastReading": null
    },
    {
      "type": "humidity",
      "unit": "%",
      "port": 2,
      "lastReading": 65.5
      }
    ]
}
"""

# Parse the JSON string into a Python dictionary
device_data = json.loads(device_config_json_string)

print("--- Exploring Parsed JSON Data ---")
print(f"The data type is: {type(device_data)}")

# Access top-level keys
device_id = device_data['deviceId']
print(f"Device ID: {device_id}")

# Access data from a list of objects
first_sensor_type = device_data['sensors'][0]['type']
print(f"First sensor type: {first_sensor_type}")

# Loop through the sensors
print("\n All sensors:")
for sensor in device_data['sensors']:
    print(f" - Type:  {sensor['type']}, Port: {sensor['port']}")

# Part 2
print("\n --- Modifying Python Object ---")

# Update a value
device_data['isActive'] = False
print("Set isActive to False.")

# Update a nested value
device_data['location']['room'] =  "305-B"
print("Moved device to room 305-B.")

# Update a value in the sensor list
device_data['sensors'][0]['lastReading'] = 22.7
print("Updated temperature sensor's last reading.")

# Add a new key-value pair
device_data['firmvareVersion'] = "v1.2.3"
print("Added firmware version")

print("\n --- Serializing back to JSON string ---")

# Convert the dictionary back to a JSON string with nice formatting
updated_json_string = json.dumps(device_data, indent=2)

print("Updated JSON Configuration:")
print(updated_json_string)

# Save the updated JSON to a file
file_path = "updated_config.json"
with open(file_path, "w") as json_file:
    json_file.write(updated_json_string)
print(f"\n Successfully saved updated configuration to {file_path}")