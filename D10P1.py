def main():
    file = open('inputD10.txt', 'r')

    lines = file.readlines()

    direction_connections = {
        'North': 'South',
        'South': 'North',
        'East': 'West',
        'West': 'East'
    }

    letter_connections = {
        '|': ('North', 'South'),
        '-': ('East', 'West'),
        'L': ('North', 'East'),
        'J': ('North', 'West'),
        '7': ('South', 'West'),
        'F': ('South', 'East'),
        '.': None
    }

    adjacency_list = {}

    for i in range(len(lines)):
        if 'S' in lines[i]:
            x = lines[i].index('S')
            y = i
            adjacency_list['start'] = (x, y) 
    
    y = adjacency_list['start'][1] + 1
    curr_line = lines[y]
    x = adjacency_list['start'][0]
    character = curr_line[x]
    previous_direction = 'South'

    adjacency_list[1] = (x, y)
    i = 2
    while character != 'S':
        directions = letter_connections[character]
        connection = direction_connections[previous_direction]
        connection_index = directions.index(connection)
        next_direction = directions[1-connection_index]

        if next_direction == 'North':
            y -= 1
        elif next_direction == 'South':
            y += 1
        elif next_direction == 'East':
            x += 1
        elif next_direction == 'West':
            x -= 1
        
        adjacency_list[i] = (x, y)

        previous_direction = next_direction
        curr_line = lines[y]
        character = curr_line[x]
        i += 1

    steps = (len(adjacency_list) - 1) / 2
    print(int(steps))


if __name__ == '__main__':
    main()