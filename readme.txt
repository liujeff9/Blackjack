Instructions for running your code and any tests you may have written
Rules for your card game, if not one of the three listed above
A brief explanation of your design choices and any data structures or algorithms that you implemented
Choice of tooling (language, libraries, test runner, etc.) and rationale behind those choices.

To run enter make sure Python is installed,
    python3 blackjack.py

This game follows the traditional rules of python where the user plays against the computer player.
The user can bet losing all money, doubling their money or gaining a factor of 1.5 on a hand of 21.

The code is split into three files, game.py contains all the code relating to the score and cards.
The cards are a dictionary with all the cards mapped to their scoring value (Ace = 1). Then the keys
are shuffle and placed into a list that behaves like stack. The user has a list storing their current
hand. The deck is then reshuffle after every hand.

The is written in python because I it more entertaining to write. Learning only Java throughout college
made me confident with writing the language, but it is not as enjoyable. I really enjoy the syntax and the
ease to write python code. I used no additionl libraries and wrote a few tests for my scoring function.