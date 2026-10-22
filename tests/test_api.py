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
    "time": "2026-10-22T11:30",
    "interval": 900,
    "temperature_2m": 12.5
}
}
VAL = {"stad": "Stockholm"}

@pytest.fixture
def klient():
    app.config["TESTING"]  = True
    return app.test_client()

@patch("functions.func.requests.get")
def test_api(mock_get, klient):
    mock_get.return_value= Mock(json=lambda: DATA)
    svar = klient.post("/", data=VAL)
    assert svar.status_code == 200