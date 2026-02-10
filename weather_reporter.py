import os
import sys
import requests
from datetime import datetime


API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = os.getenv("BASE_URL", "http://api.openweathermap.org/data/2.5/weather")

if not API_KEY:
    print("Error: WEATHER_API_KEY environment variable not set.")
    sys.exit(1)

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

def print_weather_info(data):
    if not data:
        print("No data to display.")
        return

    try:
        city = data['name']
        temp = data['main']['temp']
        print(f"{city}: {temp}K")
        log_weather(data)  # Scenario 1 addition
    except KeyError:
        pass

LOG_FILE = "weather_log.txt"

def log_weather(data):
    if not data:
        return
    try:
        city = data['name']
        temp = data['main']['temp']
        time = datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')
        with open(LOG_FILE, "a") as f:
            f.write(f"{time} - {city}: {temp}K\n")
    except KeyError:
        pass

def run_cli():
    print("Welcome to Weather CLI (Scenario 1)")
    city = input("Enter city: ").strip()
    data = get_weather(city)
    print_weather_info(data)

if __name__ == "__main__":
    run_cli()