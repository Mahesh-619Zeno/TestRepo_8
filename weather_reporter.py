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
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    return None

LOG_DIR = os.getenv("WEATHER_LOG_DIR", ".")
LOG_FILE = os.path.join(LOG_DIR, "weather_log.txt")

def log_weather(data):
    """Logs weather data to a file using existing imports"""
    if not data:
        return

    try:
        city = data["name"]
        temp = data["main"]["temp"]
        timestamp = datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")

        with open(LOG_FILE, "a") as file:
            file.write(f"{timestamp} | {city} | {temp}K\n")

    except KeyError:
        print("Failed to log weather data due to missing fields.")

def print_weather_info(data):
    if not data:
        print("No data to display.")
        return

    try:
        city = data["name"]
        temp = data["main"]["temp"]
        print(f"City: {city}, Temperature: {temp}K")
        log_weather(data)

    except KeyError:
        print("Unexpected data format.")

def run_cli():
    print("Welcome to Weather CLI (Scenario 1)")
    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    data = get_weather(city)
    print_weather_info(data)

if __name__ == "__main__":
    run_cli()
