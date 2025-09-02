def solution_station_1(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    if len(str(a)) > 17:
        a = str(a) 
        a = a[:17] + '0' * (len(a) - 17)
    return int(a)
    





print(solution_station_1(88))