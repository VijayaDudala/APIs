import requests

api_key = "733a517e34ab140c7928cb2f634f9fdd"
city = input("Enter the city: ")  # Prompts user for city input
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    # Convert temperature from Kelvin to Celsius
    temperature_celsius = weather_data['main']['temp'] - 273.15
    print(f"Temperature: {temperature_celsius:.2f}°C")
    print(f"Weather: {weather_data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data. Please check the city name and try again.")
