from functions.hamta_data import hamtaData

STADER = ["Stockholm", "Göteborg", "Malmö", "Umeå", "Kiruna"]

def giltig_indata(stad):
    try:
        if stad in STADER:
            return True
    except (ValueError, TypeError):
        return False

"""
Matchar alla värden i "hourly" per timme och returnerar
en lista med en dictionary per timme som innehåller
nyvklarna som har samma namn som i API
"""
def matchAllaKeys(lat, lon):
    hourly = hamtaData(lat, lon)["hourly"]
    nycklar = list(hourly.keys())
    return [dict(zip(nycklar, varden, strict=False)) for varden in zip(*hourly.values(), strict=False)]
