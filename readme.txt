To run make sure Python 3 is installed, run with python3
    python3 blackjack.py

This game follows the traditional rules of blackjack, the user plays against the computer player.
The user can bet losing all money, doubling their money or gaining a factor of 1.5 on a hand of 21.

The code is split into four files:
    hands.py contains all the code relating dealer and player's hand. Additionally, it contains functions 
        to print their hands and calculate their respective scores.
    deck.py contains a dictionary with all the cards mapped to their scoring value (Ace = 1). On initialization,
        the keys are shuffle and placed into a list that behaves like stack.
    blackjack.py contains the main logic for the game to run
    bet.py contains the UI and logic to handling betting

I chose this design to elminate dependencies from the main python file. In blackjack.py there is a lot of black box
knowledge as it does not know how the hands are getting cards or how the score is calculated. Additionally, I
chose an object oriented design as it made the code modular and related functions to the objects.

Initially, I wrote a recursive algorithm to calculate the score, where I tried 1 and 11 as the value
of aces to get the best score. But then I realized that it was only possible to have one ace with the
value 11, otherwise assume that we have more than one ace with value 11, 11 + 11 would automatically 
be a bust, a contradiction. So I changed it to an iterative algorithm.

The is written in python because I it more entertaining to write. Learning only Java throughout college
made me confident with writing the language and taught me object oriented programming. But python is no the best
language for object oriented programming. I wanted to challenge myself since to design such a game. I also really
enjoy the syntax and the ease to write python code. I used no additionl libraries and wrote a few tests for 
my scoring function.