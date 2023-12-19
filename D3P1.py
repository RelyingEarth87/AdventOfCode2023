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
                            
def get_part_nums(selection, numbers, positions):
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '-', '=', '+']

    part_nums = []
    for i in range(len(positions)):
        x = positions[i][0]
        y = positions[i][1]
        length = len(numbers[i])

        check_box = []
        for j in selection[y-1][x-1:x+length+1]:
            check_box.append(j)
        for k in selection[y][x-1:x+length+1]:
            check_box.append(k)
        for l in selection[y+1][x-1:x+length+1]:
            check_box.append(l)
        
        for symbol in symbols:
            if symbol in check_box:
                part_nums.append(int(numbers[i]))
                break
    
    return part_nums

def main():
    file = open('inputD3.txt', 'r')

    lines = file.readlines()
    selection = [i.strip() for i in lines]

    selection = make_bigger(selection)

    numbers, num_tuples = find_nums(selection)
    
    part_nums = get_part_nums(selection, numbers, num_tuples)
    print(sum(part_nums))
    

if __name__ == '__main__':
    main()
