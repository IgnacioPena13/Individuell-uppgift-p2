STADER = ["Stockholm", "Göteborg", "Malmö", "Umeå", "Kiruna"]

def giltig_indata(stad):
    try:
        if stad in STADER:
            return True
    except (ValueError, TypeError):
        return False
