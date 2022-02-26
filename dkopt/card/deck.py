"""Stores deck components."""
from dataclasses import dataclass
from itertools import product
from typing import List

from dkopt.card.card import CardCondition
from dkopt.card.hand import Hand


@dataclass
class Deck:
    """Stores the number of deck and CardCondition and generate hand pattern."""
    num_deck: int
    card_conditions: List[CardCondition]

    def gen_hands(self, num_hand: int) -> Hand:
        """Return Hand containing all possible card combinaitons.

        :prarm num_hand: The number of hand.
        :return: Hand.
        """
        nums_in_deck = [cc.num_in_deck for cc in self.card_conditions]
        # List all hand candidates to get cartesian product of them.
        hand_patterns = [cc.hand_candidates for cc in self.card_conditions]
        combinations = []
        for comb_candidates in product(*hand_patterns):
            # If a hand exceeds the number of hand, ignore it.
            if sum(comb_candidates) <= num_hand:
                combinations.append(comb_candidates)

        return Hand(self.num_deck, num_hand, nums_in_deck, combinations)

    def __str__(self) -> str:
        """Return the deck information.

        :return: The number of deck and cards given as input.
        """
        result = f"Total Num Deck: {self.num_deck}"
        for cc in self.card_conditions:
            result += f" Num {cc.name} in deck: {cc.num_in_deck}"

        return result

    def __hash__(self) -> int:
        return hash(frozenset(self.card_conditions)) + self.num_deck
