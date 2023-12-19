import re
import typing

def make_bigger(selection):
    for i in range(len(selection)):
        line = f'.{selection[i]}.'
        selection[i] = line
    
    new_line = ''
    for j in range(len(selection[0]) - 1):
        new_line += '.'
    
    selection.insert(0, new_line)
    selection.append(new_line)

    return selection

def find_nums(selection) -> (list, list):
    numbers = []
    positions = []

    y = 0
    while y < len(selection) - 1:
        x = 0
        while x < len(selection[0]) - 1:
            if selection[y][x].isnumeric():
                number = True
                num = selection[y][x]
                positions.append((x, y))
                while number:
                    x +=1
                    if x > len(selection[y]) - 1:
                        numbers.append(num)
                        number = False
                    elif not selection[y][x].isnumeric():
                        numbers.append(num)
                        number = False
                    else:
                        num += selection[y][x]
            x += 1
        y += 1
    
    return numbers, positions
                            
def get_gear_ratio(selection, numbers, positions):
    gear = '*'
    gears = {}

    gear_ratios = []
    gear_num = 0
    for i in range(len(positions)):
        x = positions[i][0]
        y = positions[i][1]
        length = len(numbers[i])

        for j in range(y-1, y+2):
            for k in range(x-1, x+length+1):
                if selection[j][k] == gear:
                    label = f'({k}, {j})'
                    try:
                        gears[label].append(int(numbers[i]))
                    except:
                        gears[label] = [int(numbers[i])]

    for gear in gears:
        if len(gears[gear]) == 2:
            gear_ratios.append(gears[gear][0] * gears[gear][1])

    return sum(gear_ratios)

def main():
    file = open('inputD3.txt', 'r')

    lines = file.readlines()
    selection = [i.strip() for i in lines]

    selection = make_bigger(selection)

    numbers, num_tuples = find_nums(selection)
    
    gear_ratio = get_gear_ratio(selection, numbers, num_tuples)
    print(gear_ratio)
    

if __name__ == '__main__':
    main()