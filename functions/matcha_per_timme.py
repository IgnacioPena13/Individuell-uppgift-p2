from functions.hamta_data import hamtaData

"""
Matchar alla värden i "hourly" per timme och returnerar en listamed 
en dictionary per timme som innehåller nyvklarna som har samma namn som i API
"""
def matchAllaKeys(lat, lon):
    hourly = hamtaData(lat, lon)["hourly"]
    nycklar = list(hourly.keys())
    return [dict(zip(nycklar, varden)) for varden in zip(*hourly.values())]
