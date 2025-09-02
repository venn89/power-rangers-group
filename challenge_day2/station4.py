import math

def solution_station_4(x):
    status = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            status = 0
            break
        else:
            continue
    return status