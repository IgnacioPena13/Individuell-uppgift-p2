import requests


def hamtaData(lat: float, lon: float):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation,weather_code,wind_speed_10m,wind_direction_10m,rain,snowfall,apparent_temperature,relative_humidity_2m&models=metno_seamless&current=temperature_2m,is_day,apparent_temperature,relative_humidity_2m,precipitation,rain,snowfall,showers,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&forecast_days=3"
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    data = response.json()
    return data
