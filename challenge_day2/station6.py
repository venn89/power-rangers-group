import math

def solution_station_6(values):
    if isinstance(values, (int, float)):
        values = [values]
    return [round(math.sin(v), 4) for v in values]