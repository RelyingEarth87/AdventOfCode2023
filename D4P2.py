from queue import Queue

def card_parse(full_card):
    full_split = full_card.split(':')
    name = full_split[0]

    card_nums = full_split[1].split(' | ')

    winners = []
    winning_nums = card_nums[0].split()
    for num in winning_nums:
        winning_num = int(num)
        winners.append(winning_num)
    
    checks = []
    my_nums = card_nums[1].split()
    for num in my_nums:
        my_num = int(num)
        checks.append(my_num)

    return name, winners, checks

def calc_winners(card):
    card_split = card[0].split()
    card_num = int(card_split[1])
    winners = card[1]
    checks = card[2]

    wins = 0

    for check in checks:
        if check in winners:
            wins += 1
    
    
    return card_num, wins


def main():
    file = open('inputD4.txt', 'r')

    lines = file.readlines()

    cards = []
    for i in lines:
        name, winners, checks = card_parse(i)
        cards.append([name, winners, checks])
    
    winnings = {}
    for card in cards:
        card_num, wins = calc_winners(card)
        winnings[card_num] = wins

    q = Queue(maxsize = 0)
    for card in winnings:
        q.put(card)

    total_cards = 0
    while not q.empty():
        total_cards += 1
        current = q.get()
        wins = winnings[current]
        if current + wins > len(winnings):
            wins = len(winnings) - current
        for i in range(1, wins + 1):
            q.put(current + i)

    print(total_cards)


if __name__ == '__main__':
    main()
