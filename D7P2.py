from operator import attrgetter

class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        self.ranks = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        self.type = self.calc_hand()
        self.card_ranks = self.calc_ranks()
        self.card1_rank = self.card_ranks[0]
        self.card2_rank = self.card_ranks[1]
        self.card3_rank = self.card_ranks[2]
        self.card4_rank = self.card_ranks[3]
        self.card5_rank = self.card_ranks[4]
    
    def __str__(self):
        return self.cards
    
    def get_hand(self):
        return self.cards

    def get_bet(self):
        return int(self.bet)
    
    def get_card_rank(self, num):
        card = self.cards[num]
        rank = self.ranks.index(card)
        return rank
    
    def calc_hand(self):
        counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(self.ranks)):
            count = self.cards.count(self.ranks[i])
            counters[i] += count
        
        without_jokers = counters[1:]
        count_max = max(without_jokers)
        count_max_1 = max(without_jokers)
        if 'J' in self.cards:
            count_max += counters[0]

        
        if count_max == 5:
            type = 'Five-of-a-kind'
        elif count_max == 4:
            type = 'Four-of-a-kind'
        elif count_max == 3 and 3 not in without_jokers:
            without_jokers.remove(count_max_1)
            if max(without_jokers) == 2:
                type = 'Full house'
            else:
                type = 'Three-of-a-kind'
        elif count_max == 3 and 2 in without_jokers:
            type = 'Full house'
        elif count_max == 3:
            type = 'Three-of-a-kind'
        elif count_max == 2:
            if 2 in without_jokers:
                without_jokers.remove(2)
                count_max = max(without_jokers)
                if count_max == 2:
                    type = 'Two pair'
                else:
                    type = 'One pair'
            else:
                type = 'One pair'
        elif count_max == 1:
            type = 'High card'
        
        return type
    def calc_ranks(self):
        ranks = []
        for i in self.cards:
            rank = self.ranks.index(i)
            ranks.append(rank)
        
        return ranks

def _sort(list):
    list = sorted(list, key=attrgetter('card1_rank','card2_rank','card3_rank','card4_rank','card5_rank'), reverse=True)
    return list
        
def main():
    file = open('inputD7.txt', 'r')
    #file = open('input7Test.txt', 'r')

    lines = file.readlines()

    five_a_kind = []
    four_a_kind = []
    full_house = []
    three_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        hand_and_bet = line.split()
        hand = Hand(hand_and_bet[0], hand_and_bet[1])
        if hand.type == 'Five-of-a-kind':
            five_a_kind.append(hand)
        elif hand.type == 'Four-of-a-kind':
            four_a_kind.append(hand)
        elif hand.type == 'Full house':
            full_house.append(hand)
        elif hand.type == 'Three-of-a-kind':
            three_a_kind.append(hand)
        elif hand.type == 'Two pair':
            two_pair.append(hand)
        elif hand.type == 'One pair':
            one_pair.append(hand)
        elif hand.type == 'High card':
            high_card.append(hand)

    total_hands = len(five_a_kind) + len(four_a_kind) + len(full_house) + len(three_a_kind) + len(two_pair) + len(one_pair) + len(high_card)

    five = _sort(five_a_kind)
    four = _sort(four_a_kind)
    full = _sort(full_house)
    three = _sort(three_a_kind)
    two = _sort(two_pair)
    one = _sort(one_pair)
    high = _sort(high_card)

    hands = []
    for i in five:
        hands.append(i)
    for j in four:
        hands.append(j)
    for k in full:
        hands.append(k)
    for l in three:
        hands.append(l)
    for m in two:
        hands.append(m)
    for n in one:
        hands.append(n)
    for o in high:
        hands.append(o)
    
    
    total_winnings = 0
    for p in range(total_hands - 1, -1, -1):
        winnings = hands[p].get_bet() * (total_hands - p)
        print(hands[p], hands[p].type, total_hands - p)
        total_winnings += winnings
    
    print(total_winnings)



if __name__ == '__main__':
    main()