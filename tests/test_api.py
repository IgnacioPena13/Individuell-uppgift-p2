import pytest
from unittest.mock import Mock, patch
from app import app

DATA = {
"latitude": 59.3289,
"longitude": 18.072357,
"generationtime_ms": 0.013709068298339844,
"utc_offset_seconds": 0,
"timezone": "GMT",
"timezone_abbreviation": "GMT",
"elevation": 18,
"current_units": {
    "time": "iso8601",
    "interval": "seconds",
    "temperature_2m": "°C"
},
"current": {
"time": "2026-10-27T11:00",
"interval": 900,
"temperature_2m": 10.1,
"apparent_temperature": 6.2,
"is_day": 1,
"precipitation": 0,
"rain": 0,
"showers": 0,
"snowfall": 0,
"weather_code": 3,
"wind_speed_10m": 21.6
},
}

VAL = {"stad": "Stockholm"}

@pytest.fixture
def klient():
    app.config["TESTING"]  = True
    return app.test_client()
# Använder en decorator patch för att ersätta request.get förfrågan till riktiga api med mock
# mock_get vet då vilket data ska returneras pga Mock(ett obj. som har ett atribut json som innehåller data])
# sen checkar om status kod av svaret#
@patch("functions.hamtaData.requests.get")
def test_data(mock_get, klient):
    mock_get.return_value= Mock(json=lambda: DATA)
    svar = klient.post("/", data=VAL, follow_redirects=True)
    assert svar.status_code == 200 or svar.status_code == 302
    assert  "10 °C" in svar.get_data(as_text=True)