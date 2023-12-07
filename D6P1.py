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

    beaten = []
    for i in range(len(times)):
        num_ways = ways(int(times[i]), int(distances[i]))
        beaten.append(num_ways)
    
    product = 1
    for j in beaten:
        product *= j
    
    print(product)





if __name__ == '__main__':
    main()