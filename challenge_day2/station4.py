import math

def solution_station_4(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return "False"
    return "True"