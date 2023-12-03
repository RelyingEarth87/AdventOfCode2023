def main():
    file = open('inputD2.txt', 'r')

    lines = file.readlines()

    
    powers = []
    for game in lines:
        game = game.split(':')
        sets = game[1].split(';')

        reds = []
        greens = []
        blues = []
        
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

            reds.append(tot_red)
            greens.append(tot_green)
            blues.append(tot_blue)

        min_red = max(reds)
        min_green = max(greens)
        min_blue = max(blues)

        power = min_red * min_green * min_blue
        powers.append(power)

    power_sum = sum(powers)
    print(power_sum)


if __name__ == '__main__':
    main()
