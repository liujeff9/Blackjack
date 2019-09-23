import game as g
import bet as b

# prints the given hand
def print_hand(cards):
    hand = ""
    for card in cards:
        hand += card + ", "
    return hand[:-2]

def play_blackjack():
    print()
    print("WELCOME TO BLACKJACK, press CRTL + C to quit")
    print()

    playing = True
    total_amount = b.get_starting_amount()
    curr_bet = 0

    print()
    print()
    while (total_amount > 0):
        game_status = 0

        print("You have: $" + str(total_amount))
        curr_bet = b.get_bet(total_amount)
        print()

        player_hand = []
        player_hand.append(g.deal_card())
        player_hand.append(g.deal_card())

        while (True):
            print("Your hand is: " + print_hand(player_hand))
            player_score = g.get_score(player_hand)
            
            # auto win if the player is dealt a hand of 21
            if player_score == 21:
                game_status = 2
                print("Blackjack! You win!")
                break

            # get user input
            command = input("Press any key(s) then press ENTER to stay or press ENTER to hit: ")

            # if the user stays
            if (len(command) > 0):
                print("Stay, your score is: " + str(player_score))
                
                # get the dealer's hand
                dealer_hand, dealer_score = g.dealer_play()
                print()
                print("The dealer's hand is: " + print_hand(dealer_hand))
                print("The dealer's score is: " + str(dealer_score))

                # check the winner of the given hand
                if dealer_score > 21:
                    game_status = 1
                    print("Dealer busted, you win!")
                elif player_score > dealer_score:
                    game_status = 1
                    print("You win!")
                else:
                    print("You lose")

                break
                
            else:

                # if the user hits (draws another card)
                print("Hit")
                print()

                # add another card the to the user's hand
                player_hand.append(g.deal_card())
                player_score = g.get_score(player_hand)

                # check the user wins with 21 or busts
                if player_score == 21:
                    game_status = 2
                    print("Your hand is: " + print_hand(player_hand))
                    print("Blackjack! You win!")
                    break
                elif player_score > 21:
                    print("Your hand is: " + print_hand(player_hand))
                    print("Your score is: " + str(player_score))
                    print("Bust, you lose")
                    break
        
        # update player money from the game status
        total_amount = b.get_payout(total_amount, curr_bet, game_status)
        print()
        print()
        print()

    print("You are out of money, exiting now")
    exit()

play_blackjack()