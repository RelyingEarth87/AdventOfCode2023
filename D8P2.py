from math import lcm
from functools import reduce

def make_lookup(destinations):
    lookup = {}
    starts = []
    for i in destinations:
        i = i.strip().split()
        name = i[0]
        left = i[2].strip('(),')
        right = i[3].strip('(),')
        lookup[name] = [left, right]
        if name[2] == 'A':
            starts.append(name)
    
    return lookup, starts

def calc_steps(curr_key, lookup, directions):
    direction_num = 0
    steps = 0
    keys = [curr_key]
    while curr_key[2] != 'Z':
        instruction = directions[direction_num]
        if instruction == 'L':
            curr_key = lookup[curr_key][0]
        elif instruction == 'R':
            curr_key = lookup[curr_key][1]
        if direction_num >= len(directions) - 1:
            direction_num = 0
        else:
            direction_num += 1

        keys.append(curr_key)
        steps += 1

    return steps

def main():
    file = open('inputD8.txt', 'r')
    #file = open('input8Test.txt', 'r')
    #file = open('input8Test1.txt', 'r')
    #file = open('input8Test2.txt', 'r')

    lines = file.readlines()
    directions = lines[0].strip()
    destinations = lines[2:]

    lookup, starts = make_lookup(destinations)
    step_list = []
    for start in starts:
        steps = calc_steps(start, lookup, directions)
        step_list.append(steps)
    

    print(reduce(lcm, step_list))

if __name__ == '__main__':
    main()
