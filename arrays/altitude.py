def largestAltitude(gain) -> int:
    current_altitude = 0
    highest_altitude = 0
    for i in gain:
        current_altitude += i
        highest_altitude = max(highest_altitude, current_altitude)

    print(highest_altitude)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
largestAltitude(x)
