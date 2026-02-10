import os
import sys
import requests
from datetime import datetime
import json 

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("BASE_URL", "http://api.openweathermap.org/data/2.5/weather")

if not API_KEY:
    print("Error: WEATHER_API_KEY environment variable not set.")
    sys.exit(1)

def get_weather(city_name):
    params = {'q': city_name, 'appid': API_KEY}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

def print_raw_weather(data):
    if not data:
        print("No data to show.")
        return
    print(json.dumps(data, indent=4))

def run_cli():
    print("Welcome to Weather CLI (Scenario 2)")
    city = input("Enter city: ").strip()
    data = get_weather(city)
    print_raw_weather(data)

if __name__ == "__main__":
    run_cli()