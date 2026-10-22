import requests
import json

def hamtaData(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation,weather_code,wind_speed_10m,wind_direction_10m,rain,snowfall,apparent_temperature,relative_humidity_2m&models=metno_seamless&current=temperature_2m,is_day,apparent_temperature,relative_humidity_2m,precipitation,rain,snowfall,showers,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&forecast_days=3".format(lat=lat,lon=lon)
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as e:
        print(f"API returned an error: {e.response.status_code}")
    except requests.RequestException as e:
        print(f"Could not reach the API: {e}")
   