import re
import numpy as np
import matplotlib.pyplot as plt

def move_rocks(platform):
    moving_rock = 'O'
    fixed_rock = '#'

    for i in range(len(platform)):
        line = platform[i]
        for j in range(len(line)):
            space = line[j]
            if space == moving_rock:
                is_movable = True
                differential = 1
                while is_movable:
                    if i - differential < 0:
                        is_movable = False
                    elif platform[i-differential][j] == moving_rock or platform[i-differential][j] == fixed_rock:
                        is_movable = False
                    elif platform[i-differential][j] == '.':
                        platform[i-differential] = f'{platform[i-differential][:j]}{moving_rock}{platform[i-differential][j+1:]}'
                        platform[i-differential+1] = f'{platform[i-differential+1][:j]}.{platform[i-differential+1][j+1:]}'
                        differential += 1

    return platform

def rotate_platform(platform):
    char_map = np.chararray((len(platform),len(platform[0])),unicode=True)
    for l, line in enumerate(platform):
        char_map[l] = np.array([i for i in line.strip()])
    updated_platform = np.rot90(char_map, -1)
    updated_platform = updated_platform.tolist()
    
    end_platform = []
    for i in range(len(updated_platform)):
        line = ''
        for j in range(len(updated_platform[i])):
            line += updated_platform[i][j]
        end_platform.append(line)
    return end_platform

def calc_total_load(platform):
    amount_of_load = []
    for i in range(0, len(platform)):
        #print(i)
        indexes = [i.start() for i in re.finditer('O', platform[i])]
        #print(indexes)
        if len(indexes) == 0:
            pass
        else:
            for j in indexes:
                #print(len(platform) - i)
                amount_of_load.append(len(platform) - i)
    
    return sum(amount_of_load)

def main():
    file = open('inputD14.txt', 'r')
    #file = open('input14Test.txt', 'r')

    lines = file.readlines()
    platform = [i.strip() for i in lines]

    """original_platform = np.chararray((len(platform),len(platform[0])),unicode=True)
    for l, line in enumerate(platform):
        original_platform[l] = np.array([i for i in line])"""
    
    cycles = []
    original_load = calc_total_load(platform)
    
    cycle_num = 0
    while cycle_num < 235:
        #north
        updated_platform = move_rocks(platform)

        #west
        platform = rotate_platform(updated_platform)
        updated_platform = move_rocks(platform)

        #south
        platform = rotate_platform(updated_platform)
        updated_platform = move_rocks(platform)

        #east
        platform = rotate_platform(updated_platform)
        updated_platform = move_rocks(platform)

        platform = rotate_platform(updated_platform)
        
        updated_load = calc_total_load(platform)
        
        cycles.append(updated_load)
        cycle_num += 1
    
    plt.figure(dpi=300)
    plt.plot(cycles[205:235])
    plt.xlabel("Number of cycles")
    plt.ylabel("Load")
    plt.title("Load history")
    plt.grid()
    plt.savefig("load_history.png")

    # notice that the load is periodic every 26 cycles, so we can calculate the load at 1e9 - 1 - 26 * const, where const is some number. In this case, const = 38461530, which gives 219
    print(cycles[219])


if __name__ == '__main__':
    main()