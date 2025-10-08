import requests
import pandas
from datetime import datetime

# Constants
API_URL = "https://jsonplaceholder.typicode.com/posts"
DATE_RETRIEVED = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Fetch data from API
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    df = pandas.DataFrame(data)
    df['fetched_at'] = DATE_RETRIEVED
    print("Data fetched and added timestamp column.")
    print(df.head())
else:
    print("Failed to fetch data. Status code:", response.status_code)
