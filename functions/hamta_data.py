import requests

URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "daily": ",".join(
        [
            "weather_code",
            "temperature_2m_mean",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "precipitation_hours",
            "sunrise",
            "sunset",
            "wind_speed_10m_max",
        ]
    ),
    "hourly": ",".join(
        [
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
        ]
    ),
    "models": "best_match",
    "current": ",".join(
        [
            "temperature_2m",
            "apparent_temperature",
            "is_day",
            "precipitation",
            "weather_code",
            "wind_speed_10m",
        ]
    ),
    "minutely_15": "temperature_2m",
    "timezone": "auto",
    "forecast_days": 4,
}


class HamtaDataFel(Exception):
    pass


def hamtaData(lat: float, lon: float):
    url = URL
    params = {"latitude": lat, "longitude": lon, **PARAMS}
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as e:
        return f"Något gick fel: {e}"
    except requests.RequestException as e:
        raise HamtaDataFel("Kunde inte hämta vädrets data") from e
