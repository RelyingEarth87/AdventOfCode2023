def calc_points(winning, check):
    exp = 0
    for i in check:
        if i in winning:
            exp += 1

    if exp == 0:
        return 0
    return 2**(exp-1)

def main():
    file = open('inputD4.txt', 'r')

    lines = file.readlines()

    every_card = []

    for line in lines:
        split_line = line.split(':')
        full_line = split_line[1]
        full = full_line.split(' | ')

        winning_nums = []
        winners = full[0].split()
        for num in winners:
            winning_num = int(num)
            winning_nums.append(winning_num)
        
        checks = full[1].split()
        my_nums = []
        for num in checks:
            my_num = int(num)
            my_nums.append(my_num)

        points = calc_points(winning_nums, my_nums)
        every_card.append(points)

    total = 0
    for i in every_card:
        total += i
    
    print(total)


if __name__ == '__main__':
    main()