import requests


def hamtaData(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "sunrise",
            "sunset",
            "moonrise",
            "moonset",
            "moon_phase",
            "uv_index_max",
        ],
        "hourly": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
            "soil_temperature_0cm",
            "visibility",
            "apparent_temperature",
            "precipitation_probability",
            "uv_index",
            "is_day",
        ],
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "rain",
            "showers",
            "snowfall",
            "weather_code",
            "wind_speed_10m",
        ],
        "timezone": "Europe/Berlin",
    }
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as e:
        print(f"API returned an error: {e.response.status_code}")
    except requests.RequestException as e:
        print(f"Could not reach the API: {e}")
