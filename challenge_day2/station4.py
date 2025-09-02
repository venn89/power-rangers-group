import math

def solution_station_4(x):
    status = 1  # Assume the number is prime initially
    for i in range(2, int(math.sqrt(x)) + 1):  # Loop from 2 to sqrt(num)
        if x % i == 0:
            status = 0  # If divisible, mark as not prime
            break
        else:
            continue
    return status