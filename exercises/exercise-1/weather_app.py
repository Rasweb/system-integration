# Run this python file using this command: "python weather_app.py"
import sys
import requests

# Part 1
## Strings
user_city = input("Enter the city you want the weather for: ")

greeting_message = "Weather forecast for:"
full_message = greeting_message + " " + user_city
print(full_message)

## Integers and Floats
current_temperature_celsius = 7
expected_high_celsius = 12.5

print("Current temperature", current_temperature_celsius, "C")
print("Expected high:", expected_high_celsius, "C")

temperature_difference = expected_high_celsius - current_temperature_celsius
print("Temperature rise expected", temperature_difference, "C")

## Type Conversion (Casting)
sensor_id_str = "Sensor_00"
sensor_number = 1
# Will cause an error 
## full_sensor_id_wrong_way = sensor_id_str + sensor_number

# Correct way of conversion
full_sensor_id_corrected = sensor_id_str + str(sensor_number)
print("Full sensor ID:", full_sensor_id_corrected)

reading_str = "23.7"
reading_float = float(reading_str)
print("Sensor reading as float:", reading_float, type(reading_float))

# Part 2
## Getting User Input
user_name = input("What is your name? " )
print("Hello,", user_name + "!")

favorite_season = input("What is your favorite season for weather? ")
print(favorite_season, "is a great choice, " + user_name + "!")

## Formatted Output (f-strings)
print(f"Recap: Weather for {user_city}.")
print(f"{user_name}, the current temperature is {current_temperature_celsius}C and the expected high is {expected_high_celsius}C.")

# Part 3
base_url = "http://wttr.in/"

# Python's f-strings (formatted string literals) a convenient way to embed expressions inside string literals
# "?format=3" flyttar den på en egen rad
full_url = f"{base_url}{user_city}?format=3"

print(f"\nFetching weather for {user_city} from {full_url}...")

try:
    response = requests.get(full_url)

    if response.status_code == 200:
        print("Weather Raport:")
        print(response.text)
    else:
        print(f"Error fetching weather: Status code {response.status_code}")
        print(f"Response text: {response.text}")

# Handle potential network errors
except requests.exceptions.RequestException as e:
    print(f"An error occured during the request: {e}")

# Part 4
# city from cmd: python weather_app.py city_name
if len(sys.argv)  > 1:
    user_city_arg = sys.argv[1]
else:
    user_city_arg = input("No city provided as argument. Enter city: ")
