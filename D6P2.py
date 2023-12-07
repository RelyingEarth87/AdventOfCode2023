def ways(time, min_distance):
    times_beaten_distance = 0

    for i in range(time):
        time_pressed = i
        time_remaining = time - time_pressed

        speed = time_pressed

        distance_travelled = speed * time_remaining

        if distance_travelled > min_distance:
            times_beaten_distance += 1
    
    return times_beaten_distance


def main():
    file = open('inputD6.txt', 'r')

    lines = file.readlines()

    times = lines[0]
    distances = lines[1]

    timesplit = times.split()
    distancesplit = distances.split()

    times = timesplit[1:len(timesplit) + 1]
    distances = distancesplit[1:len(distancesplit) + 1]

    time = ''
    distance = ''
    for i in range(len(times)):
        time += times[i]
        distance += distances[i]
    
    way = ways(int(time), int(distance))
    print(way)






if __name__ == '__main__':
    main()