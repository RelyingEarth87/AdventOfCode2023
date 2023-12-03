def main():
    file = open('inputD2.txt', 'r')

    lines = file.readlines()

    possRed = 12
    possGreen = 13
    possBlue = 14

    possGames = []
    i = 1
    for line in lines:
        line = line.split(':')
        sets = line[1].split(';')
        tot_sets = len(sets)
        
        good_sets = []
        for set_i in sets:
            try:
                set_i.index('red')
                red_pos = set_i.index('red')
                tot_red = int(str(set_i[red_pos-3]) + str(set_i[red_pos-2]))
            except:
                tot_red = 0

            try:
                set_i.index('green')
                green_pos = set_i.index('green')
                tot_green = int(str(set_i[green_pos-3]) + str(set_i[green_pos-2]))
            except:
                tot_green = 0

            try:
                set_i.index('blue')
                blue_pos = set_i.index('blue')
                tot_blue = int(str(set_i[blue_pos-3]) + str(set_i[blue_pos-2]))
            except:
                tot_blue = 0

            if tot_red <= possRed and tot_green <= possGreen and tot_blue <= possBlue:
                good_sets.append(set_i)

        if len(good_sets) == tot_sets:
            possGames.append(int(i))
        i += 1
        
    games_sum = sum(possGames)
    print(games_sum)
        
    

if __name__ == '__main__':
    main()
