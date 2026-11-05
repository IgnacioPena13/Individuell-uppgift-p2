from datetime import date
from functions.matcha_per_timme import matchAllaKeys

#testar om funktionen för att matche temperatur och tiden funkar,
#  använder datetime för att hämta datum fär dagen man kör och jämföra#
def testMatchTemperatur():
    data = matchAllaKeys(59.33, 18.07)
    idag = date.today()
    assert data[0]["time"] == f"{idag}T00:00"
