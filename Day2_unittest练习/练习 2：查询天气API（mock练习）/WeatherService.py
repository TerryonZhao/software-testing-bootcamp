import requests

class WeatherService:
    def get_temperature(self):
        url = f"https://api.example.com/weather"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("temperature")
        else:
            raise Exception("Failed to fetch weather data")
