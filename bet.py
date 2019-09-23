
# recursively asks for input numericial value
def get_starting_amount():
    bet = input("Please enter how much you want enter the game with: $")
    try:
        bet = int(bet)
        if bet <= 0:
            print("Please enter an amount greater than zero")
            return get_starting_amount()
        else:
            return bet
    except:
        print("Please enter a valid integer")
        return get_starting_amount()

# recursively asks for input numericial value, checks if player has that amount
def get_bet(total_amount):
    bet = input("Please enter how much you want to bet this round: $")
    try:
        bet = int(bet)
        if bet <= 0:
            print("Please enter an amount greater than zero")
            return get_bet(total_amount)
        elif bet > total_amount:
            print("Please enter an amount you have")
            return get_bet(total_amount)
        else:
            return bet
    except:
        print("Please enter a valid integer")
        return get_bet(total_amount)

# given a status, computes new worth of player
# 0 = lose, 1 = win, 2 = win with 21
def get_payout(total_amount, bet, win_status):
    if win_status == 0:
        total_amount -= bet
    elif win_status == 1:
        total_amount += bet
    elif win_status == 2:
        total_amount += int(bet * 1.5)
    return total_amount