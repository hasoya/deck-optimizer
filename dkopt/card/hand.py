from dataclasses import dataclass
from math import comb
from typing import List, Tuple


@dataclass
class Hand:
    """Stores hand data, and calculate the probability of given hand.

    Let d be # of cards in deck, h be # of cards in hand,
    n be # of all cards and m be # of all hands, the probability of hand is written as

        comb(d, h) * comb(n - d, m - h) / comb(n, m)
    """
    num_deck: int
    num_hand: int
    nums_in_deck: List[int]
    combinations: List[Tuple[int, ...]]

    def _calc_each_prob(self, hand_comb: Tuple[int, ...]) -> float:
        """Return probability of hand.

        The input is a combination of cards in hand. For example,
        if two card X and one card Y are in hand, hand_comb becomes (2, 1).

        :param num_deck: # of all cards in deck.
        :param num_hand: # of all cards in hand.
        :param nums_in_deck: List of # of each card in deck.
        :param hand_comb: Combination of cards in hand. See example for the detail.
        """
        deck_rest = self.num_deck
        hand_rest = self.num_hand
        num_comb = 1  # Count # of hand combination.
        for num_in_hand, num_in_deck in zip(hand_comb, self.nums_in_deck):
            num_comb *= comb(num_in_deck, num_in_hand)
            deck_rest -= num_in_deck
            hand_rest -= num_in_hand

        # If a hand remains, fill it with other cards.
        if hand_rest > 0:
            num_comb *= comb(deck_rest, hand_rest)

        return num_comb / comb(self.num_deck, self.num_hand)

    def calc_prob(self) -> float:
        """Return the probability for each combination of hands.

        The probability of all possible combination is calculated
        simply by adding all probability of each combination, because
        they are exclusive each other.
        """
        prob = 0.0
        for hand_comb in self.combinations:
            prob += self._calc_each_prob(hand_comb)

        return prob
