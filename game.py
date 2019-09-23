import random

# given a list, find the score of the given hand
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

# randomizes the order of the deck of cards
def shuffle_deck():
    l = list(deck_of_cards.keys())
    random.shuffle(l)
    return l

# return one card from the top of the deck
def deal_card():
    return current_deck.pop()

# calculate the score of the dealer, hits if below 17 or i
def dealer_play():
    hand = []
    hand.append(deal_card())
    hand.append(deal_card())
    score = get_score(hand)
    while (score < 17 or (has_ace(hand) and score < 17)):
        hand.append(deal_card())
        score = get_score(hand)
    
    # dealer has went so shuffle the deck
    global current_deck 
    current_deck = shuffle_deck()

    return hand, score

# return true if there is an ace
def has_ace(hand):
    return "A of Diamonds" in hand or "A of Clubs" in hand or "A of Hearts" in hand or "A of Spades" in hand

deck_of_cards = { "2 of Diamonds": 2, "2 of Clubs": 2, "2 of Hearts": 2, "2 of Spades": 2,
        "3 of Diamonds": 3, "3 of Clubs": 3, "3 of Hearts": 3, "3 of Spades": 3, 
        "4 of Diamonds": 4, "4 of Clubs": 4, "4 of Hearts": 4, "4 of Spades": 4, 
        "5 of Diamonds": 5, "5 of Clubs": 5, "5 of Hearts": 5, "5 of Spades": 5, 
        "6 of Diamonds": 6, "6 of Clubs": 6, "6 of Hearts": 6, "6 of Spades": 6,
        "7 of Diamonds": 7, "7 of Clubs": 7, "7 of Hearts": 7, "7 of Spades": 7, 
        "8 of Diamonds": 8, "8 of Clubs": 8, "8 of Hearts": 8, "8 of Spades": 8, 
        "9 of Diamonds": 9, "9 of Clubs": 9, "9 of Hearts": 9, "9 of Spades": 9,
        "10 of Diamonds": 10, "10 of Clubs": 10, "10 of Hearts": 10, "10 of Spades": 10,
        "J of Diamonds": 10, "J of Clubs": 10, "J of Hearts": 10, "J of Spades": 10,
        "Q of Diamonds": 10, "Q of Clubs": 10, "Q of Hearts": 10, "Q of Spades": 10,
        "K of Diamonds": 10, "K of Clubs": 10, "K of Hearts": 10, "K of Spades": 10,
        "A of Diamonds": 1, "A of Clubs": 1, "A of Hearts": 1, "A of Spades": 1,
        }
current_deck = shuffle_deck()