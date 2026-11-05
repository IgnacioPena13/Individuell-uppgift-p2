from functions.hamta_data import hamtaData


def test_DataHamtas():
    data = hamtaData(59.33, 18.07)
    assert data["timezone"] == "Europe/Berlin"
