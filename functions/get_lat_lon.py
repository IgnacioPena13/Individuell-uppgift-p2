def get_lat(stad):
    lat = 0
    match stad:
        case "Stockholm":
            lat = 59.33
        case "Göteborg":
            lat = 57.71
        case "Malmö":
            lat = 55.61
        case "Umeå":
            lat = 63.83
        case "Kiruna":
            lat = 67.86
    return lat


def get_lon(stad):
    lon = 0
    match stad:
        case "Stockholm":
            lon = 18.07
        case "Göteborg":
            lon = 11.97
        case "Malmö":
            lon = 13.00
        case "Umeå":
            lon = 20.26
        case "Kiruna":
            lon = 20.23
    return lon
