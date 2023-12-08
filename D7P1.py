from operator import attrgetter

class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        self.type = self.calc_hand()
        self.ranks = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
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
        counters = [0, 0, 0, 0, 0]
        for i in self.cards:
            if i == self.cards[0]:
                counters[0] += 1
            elif i == self.cards[1]:
                counters[1] += 1
            elif i == self.cards[2]:
                counters[2] += 1
            elif i == self.cards[3]:
                counters[3] += 1
            elif i == self.cards[4]:
                counters[4] += 1
        
        if max(counters) == 5:
            type = 'Five-of-a-kind'
        elif max(counters) == 4:
            type = 'Four-of-a-kind'
        elif max(counters) == 3 and 2 in counters:
            type = 'Full house'
        elif max(counters) == 3:
            type = 'Three-of-a-kind'
        elif max(counters) == 2:
            counters.remove(2)
            if max(counters) == 2:
                type = 'Two pair'
            else:
                type = 'One pair'
        elif max(counters) == 1:
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
        total_winnings += winnings
    
    print(total_winnings)



if __name__ == '__main__':
    main()