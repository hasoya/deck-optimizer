"""Test of deck.py"""
from typing import List

from dopt.card.card import CardCondition
from dopt.card.deck import Deck
from dopt.card.hand import Hand


class TestDeck:
    def test_gen_hands(self) -> None:
        """Test Deck.gen_hands."""
        num_hand = 5
        num_deck = 40

        # Test with good input.
        cds1 = [CardCondition("a", 3, [0, 1]),
                CardCondition("b", 2, [1])]
        d1 = Deck(num_deck, cds1)
        ans1 = Hand(num_deck, num_hand, [3, 2],
                    [(0, 1), (1, 1)])
        assert d1.gen_hands(num_hand) == ans1

        # Test with empty input.
        cds2: List[CardCondition] = []
        d2 = Deck(num_deck, cds2)
        ans2 = Hand(num_deck, num_hand, [], [()])

        assert d2.gen_hands(num_hand) == ans2

        # Test with CardCondition exceeding num_hand.
        cds3 = [CardCondition("a", 5, [4, 5]),
                CardCondition("b", 5, [1, 2])]
        d3 = Deck(num_deck, cds3)
        ans3 = Hand(num_deck, num_hand, [5, 5], [(4, 1)])

        assert d3.gen_hands(num_hand) == ans3

    def test__str__(self) -> None:
        """Test __str__."""
        num_deck = 40

        # Good input.
        cds1 = [CardCondition("a", 3, [0, 1]),
                CardCondition("b", 2, [1])]
        d1 = Deck(num_deck, cds1)
        ans1 = f"Total Num Deck: {num_deck} Num a in deck: 3 Num b in deck: 2"

        assert str(d1) == ans1

        # Empty input.
        cds2: List[CardCondition] = []
        d2 = Deck(num_deck, cds2)
        ans2 = f"Total Num Deck: {num_deck}"

        assert str(d2) == ans2
