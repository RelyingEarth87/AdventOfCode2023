import re

def turn_and_move(platform):
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
    
    updated_platform = turn_and_move(platform)
    #print(updated_platform)
    total_load = calc_total_load(updated_platform)
    print(total_load)



if __name__ == '__main__':
    main()