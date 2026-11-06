from unittest.mock import Mock, patch

import pytest
import requests

from app import app, formatera_temperatur
from functions.hamta_data import HamtaDataFel, hamtaData

DATA = {
    "latitude": 59.3289,
    "longitude": 18.072357,
    "generationtime_ms": 0.013709068298339844,
    "utc_offset_seconds": 0,
    "timezone": "GMT",
    "timezone_abbreviation": "GMT",
    "elevation": 18,
    "current_units": {"time": "iso8601", "interval": "seconds", "temperature_2m": "°C"},
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
        "wind_speed_10m": 21.6,
    },
}

VAL = {"stad": "Stockholm"}
OGILTIG_VAL = {"stad": "altokemirey"}


@pytest.fixture
def klient():
    app.config["TESTING"] = True
    return app.test_client()


# testar get metoden
# ger detaljer i post test#
@patch("functions.hamta_data.requests.get")
def test_get_metod(mock_get, klient):
    mock_get.return_value = Mock(json=lambda: DATA)
    svar = klient.get("/prognos/Stockholm")
    assert svar.status_code == 200  # checkar success
    assert "GMT" in mock_get.return_value.json()["timezone"]
    assert "2026-10-27T11:00" in mock_get.return_value.json()["current"]["time"]


# Jag testar timeout för jag hade inte gjort den i min gruppuppgift
# jag använde side effect för att simulera en timeout
# använder en with och pytest.raises för att se om min egen exception
# visas medans api anropas#
@patch("functions.hamta_data.requests.get")
def test_timeout(mock_get, klient):
    mock_get.side_effect = requests.Timeout("för seg :(")
    with pytest.raises(HamtaDataFel):
        hamtaData(59.33, 18.07)


# Använder en decorator patch för att ersätta
# request.get förfrågan till riktiga api med mock
# mock_get vet då vilket data ska returneras pga Mock
# (ett obj. som har ett atribut json som innehåller data])
# sen checkar om status kod av svaret#
@patch("functions.hamta_data.requests.get")
def test_post_data(mock_get, klient):
    mock_get.return_value = Mock(json=lambda: DATA)
    svar = klient.post("/", data=VAL, follow_redirects=True)
    assert svar.status_code == 200 or svar.status_code == 302
    assert "Stockholm" in svar.get_data(as_text=True)


@patch("functions.hamta_data.requests.get")
def test_ogiltig_stad(mock_get, klient):
    svar = klient.post("/", data=OGILTIG_VAL)
    assert svar.status_code == 400
    assert "Ogiltigt stad" in svar.get_data(as_text=True)


@patch("functions.hamta_data.requests.get")
def test_ingen_formdata(mock_get, klient):
    svar = klient.post("/", data={})
    assert svar.status_code == 400


@patch("functions.hamta_data.requests.get")
def test_api_fel_visar_felmeddelande(mock_get, klient):
    mock_get.side_effect = requests.ConnectionError("Hej Dennis, jag bara testar :)")
    svar = klient.get("/prognos/Stockholm")
    assert svar.status_code == 502


# Jag använde parametrize för att köra en enda funktion flera gånger med "förväntat" värde
# om de värde till vänster möter den till höger testen lyckas#
@pytest.mark.parametrize(
    "temp, expected",
    [
        (12.34, "12,3 °C"),  # avrunda till en decimal och komma istället för punkt
        (12.36, "12,4 °C"),  # avrunda
        (12, "12,0 °C"),  # integer input
        (0, "0,0 °C"),  # noll hanteras
        (-5.67, "-5,7 °C"),  # negativa tal
    ],
)
def test_filter_resultat(temp, expected):
    assert formatera_temperatur(temp) == expected


def test_filter_jinja():
    assert formatera_temperatur(None) == "Saknas temperatur"  # testar error
    assert "formatera_temperatur" in app.jinja_env.filters  # testa om filter finns i jinja
