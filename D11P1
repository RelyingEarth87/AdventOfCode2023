import re
def find_galaxies(space):
    galaxy = '#'

    galaxies = {}
    indices = []
    extra_lines = []
    gal_num = 1
    i = 0
    while i < len(space):
        if galaxy in space[i]:
            indexes = [j.start() for j in re.finditer(galaxy, space[i])]
            for j in range(len(indexes)):
                indices.append(indexes[j])
                galaxies[gal_num] = (int(indexes[j]), int(i))
                gal_num += 1
        else:
            extra_lines.append(i)
        i += 1
    
    indices = list(set(indices))

    extra_spaces = []
    for j in range(len(space[0])):
        if j not in indices:
            extra_spaces.append(j)

    return extra_lines, extra_spaces, galaxies


def find_shortest_paths(space, galaxies, extra_lines, indices):
    shortest_paths = []
    current_galaxy = 1
    while current_galaxy < len(galaxies):
        start = galaxies[current_galaxy]
        next_galaxy = current_galaxy + 1
        while next_galaxy < len(galaxies) + 1:
            end = galaxies[next_galaxy]
            added_spaces = 0
            for i in extra_lines:
                if (start[1] < i and end[1] > i) or (start[1] > i and end[1] < i):
                    added_spaces += 1
            for j in indices:
                if (start[0] < j and end[0] > j) or (start[0] > j and end[0] < j):
                    added_spaces += 1
            
            distance = abs((end[1] - start[1])) + abs((end[0] - start[0])) + added_spaces

            shortest_paths.append(distance)

            next_galaxy += 1
        current_galaxy += 1
    
    return shortest_paths


def main():
    file = open('inputD11.txt', 'r')

    lines = file.readlines()
    space = [i.strip() for i in lines]
    
    
    extra_lines, indices, galaxies = find_galaxies(lines)
    
    shortest_paths = find_shortest_paths(space, galaxies, extra_lines, indices)

    print(sum(shortest_paths))

if __name__ == '__main__':
    main()
