import json
import urllib.request

city = input("choose city: ")
url = f"http://wttr.in/{city}?format=j1"

response = urllib.request.urlopen(url)
weather_data = json.load(response)

print("Current weather sate: ", weather_data['current_condition'][0]['weatherDesc'][0]['value'])