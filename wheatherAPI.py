import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key securely from environment variable
api_key = os.getenv("WEATHER_API_KEY")

# Ask the user to enter a city at runtime
city = input("Enter a city name: ")

# Build the API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Make the API request
response = requests.get(url)

# Handle the response
if response.status_code == 200:
    weather_data = response.json()
    # Convert temperature from Kelvin to Celsius
    temperature_celsius = weather_data['main']['temp'] - 273.15
    print(f"Temperature in {city}: {temperature_celsius:.2f}°C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data. Please check the city name or your API key.")
