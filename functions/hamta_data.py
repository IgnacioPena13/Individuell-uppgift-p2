import requests


def hamtaData(lat: float, lon: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": [
            "weather_code",
            "sunset",
            "sunrise",
            "daylight_duration",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max",
        ],
        "hourly": [
            "temperature_2m",
            "precipitation_probability",
            "apparent_temperature",
            "precipitation",
            "rain",
            "showers",
            "snowfall",
            "snow_depth",
            "weather_code",
            "wind_speed_10m",
            "uv_index",
            "is_day",
            "dew_point_2m",
        ],
        "models": "best_match",
        "current": [
            "temperature_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
        ],
        "minutely_15": "temperature_2m",
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
