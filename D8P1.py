def main():
    file = open('inputD8.txt', 'r')

    lines = file.readlines()
    directions = lines[0].strip()
    destinations = lines[2:]

    lookup = {}
    for i in destinations:
        i = i.strip().split()
        name = i[0]
        left = i[2].strip('(),')
        right = i[3].strip('(),')
        lookup[name] = [left, right]

    start = lookup['AAA']
    current = 'AAA'
    steps = 0
    direction_num = 0
    while current != 'ZZZ':
        try:
            instruction = directions[direction_num]
        except IndexError:
            direction_num = 0
            instruction = directions[direction_num]
        steps += 1
        direction_num += 1
        if instruction == 'L':
            current = start[0]
        elif instruction == 'R':
            current = start[1]
        start = lookup[current]
    
    print(steps)

if __name__ == '__main__':
    main()