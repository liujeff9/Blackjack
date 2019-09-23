from deck import deck_of_cards

class PlayerHand():
    def __init__(self, deck):
        self.hand = []
        self.deck = deck
        self.hand.append(self.deck.deal_card())
        self.hand.append(self.deck.deal_card())

    # appends a card to the player's hand
    def hit(self):
        self.hand.append(self.deck.deal_card())

    # gets the score of the player's hand
    def get_score(self):
        return get_score(self.hand)

    # gets the string representation of the player's hand
    def get_hand(self):
        return hand_to_string(self.hand)

class DealerHand():
    def __init__(self, deck):
        self.hand = []
        self.deck = deck
        self.hand.append(self.deck.deal_card())
        self.hand.append(self.deck.deal_card())

    # calculate the score of the dealer, hits if below 17 or has ace
    def play(self):
        score = get_score(self.hand)
        while (score < 17 or (self.has_ace() and score < 17)):
            self.hand.append(self.deck.deal_card())
            score = get_score(self.hand)

        return score

    # return true if there is an ace in the dealer's hand
    def has_ace(self):
        a_d = "A of Diamonds" in self.hand
        a_c = "A of Clubs" in self.hand
        a_h = "A of Hearts" in self.hand
        a_s = "A of Spades" in self.hand
        return a_d or a_c or a_h or a_s

    # gets the string representation of the dealer's hand
    def get_hand(self):
        return hand_to_string(self.hand)


### method shared by both hands
# converts the given hand to string
def hand_to_string(hand):
    cards = ""
    for card in hand:
        cards += card + ", "
    return cards[:-2]

# gets the score of the given hand
def get_score(cards):
    score = 0
    ace = False
    for card in cards:
        if deck_of_cards[card] == 1:
            ace = True
        score += deck_of_cards[card]
    
    if score < 12 and ace:
        score += 10
    return score