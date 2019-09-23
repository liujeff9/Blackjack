import unittest 
import game as g

class Test(unittest.TestCase):
    def test_score_basic(self):   
        hand = ["3 of Spades", "6 of Clubs", "9 of Hearts"]
        score = g.get_score(hand)
        self.assertEqual(score, 18)

    def test_score_three_aces(self):   
        hand = ["A of Clubs", "A of Clubs", "A of Hearts"]
        score = g.get_score(hand)
        self.assertEqual(score, 13)

    def test_score_blackjack(self):   
        hand = ["A of Diamonds", "K of Hearts"]
        score = g.get_score(hand)
        self.assertEqual(score, 21)

    def test_score_two_aces_king(self):   
        hand = ["A of Diamonds", "K of Hearts", "A of Spades"]
        score = g.get_score(hand)
        self.assertEqual(score, 12)

    def test_score_bust(self):   
        hand = ["K of Spades", "Q of Spades", "2 of Spades"]
        score = g.get_score(hand)
        self.assertEqual(score, 22)

if __name__ == '__main__': 
    unittest.main() 