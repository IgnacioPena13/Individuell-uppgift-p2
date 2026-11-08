from functions.hamta_data import hamtaData

STADER = ["Stockholm", "Göteborg", "Malmö", "Umeå", "Kiruna"]

def giltig_indata(stad):
    try:
        if stad in STADER:
            return True
    except (ValueError, TypeError):
        return False

"""
Matchar alla värden i "hourly"  per timme och returnerar
en lista med en dictionary per timme som innehåller
nyvklarna som har samma namn som i API
* i en tidigare version av detta funktion anropades API men har ändrat den så den
* kallas bara en gång och med den data man får opererar man 
"""
def matchaAllaHourly(data):
    hourly = data["hourly"]
    nycklar = list(hourly.keys())
    return [dict(zip(nycklar, varden, strict=False)) for varden in zip(*hourly.values(), strict=False)]

# Matchar alla värden i "Daily" per Dag och returnerar
# en lista med en dictionary per dag som innehåller
# nycklarna som har samma namn som i API#
def matchaAllaDaily(data):
    daily = data["daily"]
    nycklar = list(daily.keys())
    return [dict(zip(nycklar, varden, strict=False)) for varden in zip(*daily.values(), strict=False)]
