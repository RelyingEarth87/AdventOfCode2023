def make_maps(maps):
    updated_maps = {}

    for i in maps:
        destinations = []
        starts = []
        ranges = []
        for j in range(len(maps[i])):
            full = maps[i][j].split()
            destinations.append(int(full[0]))
            starts.append(int(full[1]))
            ranges.append(int(full[2]))
        updated_maps[i] = [destinations, starts, ranges]
    
    return updated_maps

def find_locations(seed, maps):
    seed_info = []
    look_value = seed
    destination = seed
    for i in maps:
        for j in range(len(maps[i][1])):
            start = int(maps[i][1][j])
            _range = int(maps[i][2][j])
            if look_value in range(start, start + _range):
                destination = int(maps[i][0][j]) + (look_value - start)
                seed_info.append(destination)
                look_value = destination
                break
            elif j == len(maps[i][1]) - 1:
                seed_info.append(destination)
    
    return seed_info[len(seed_info) - 1], seed_info

def main():
    file = open('inputD5.txt', 'r')

    lines = file.readlines()

    seed_nums = [i for i in lines[0].strip().split()]

    lines = [i.strip() for i in lines]

    seeds = {}
    for i in seed_nums[1:]:
        seeds[int(i)] = []
    
    maps = {}
    seed_maps = lines[2:]
    start = 0
    while start < len(seed_maps):
        end = start + 1
        while end < len(seed_maps):
            if seed_maps[end] == '':
                label = seed_maps[start]
                maps[label] = seed_maps[start + 1:end]
                start = end
                break
            elif end == len(seed_maps) - 1:
                label = seed_maps[start]
                maps[label] = seed_maps[start + 1:]
                start = end
                break
            end += 1
        start += 1
    
    maps = make_maps(maps)

    location_nums = []
    for seed in seeds:
        location, full_seed_info = find_locations(seed, maps)
        location_nums.append(location)
        seeds[seed] = full_seed_info
    
    print(min(location_nums))

    


if __name__ == '__main__':
    main()
