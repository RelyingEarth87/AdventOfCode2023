def is_point_in_path(x: int, y: int, poly: list[tuple[int, int]]) -> bool:
    # code borrowed from https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule
    """Determine if the point is on the path, corner, or boundary of the polygon

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path or is a corner or on the boundary"""
    num = len(poly)
    j = num - 1
    c = False
    for i in range(num):
        if (x == poly[i][0]) and (y == poly[i][1]):
            # point is a corner
            return True
        if (poly[i][1] > y) != (poly[j][1] > y):
            slope = (x - poly[i][0]) * (poly[j][1] - poly[i][1]) - (
                poly[j][0] - poly[i][0]
            ) * (y - poly[i][1])
            if slope == 0:
                # point is on boundary
                return True
            if (slope < 0) != (poly[j][1] < poly[i][1]):
                c = not c
        j = i
    return c

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
    polygon = []

    for i in range(len(lines)):
        if 'S' in lines[i]:
            x = lines[i].index('S')
            y = i
            adjacency_list['start'] = (x, y) 
            polygon.append((x, y))
    
    y = adjacency_list['start'][1] + 1
    curr_line = lines[y]
    x = adjacency_list['start'][0]
    character = curr_line[x]
    previous_direction = 'South'

    adjacency_list[1] = (x, y)
    i = 2
    polygon.append((x, y))
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
        polygon.append((x, y))

        previous_direction = next_direction
        curr_line = lines[y]
        character = curr_line[x]
        i += 1

    in_poly = []
    y = 0
    for line in lines:
        x = 0
        for character in line:
            in_out = is_point_in_path(x, y, polygon)
            if in_out is bool:
                pass
            elif in_out % 2 == 1 and (x, y) not in polygon:
                in_poly.append(1)
            x += 1
            
        y += 1
    
    print(sum(in_poly))



if __name__ == '__main__':
    main()