from dataclasses import dataclass
from typing import List

from dkopt.card.card import CardCondition


@dataclass
class SearchSetting:
    """Stores settings written in config yaml file, and create CardCondition.

    :param name: The name of card.
    :param min: The mininum # of cards in deck.
    :param max: The maximum # of cards in deck.
    :param require: # of cards required in a hand or a deck.
    :param exact: If True, the condition must be equal to require.
    :param in_hand: If True, the probability that cards are in hand.
    """
    name: str
    min: int
    max: int
    require: int
    exact: bool
    in_hand: bool

    def _in_hand_candidates(self, in_deck: int, num_hand: int) -> List[int]:
        """Return a list of possible # of cards based on settings.

        :param in_deck: # of cards in a deck.
        :param num_hand: # of cards in a hand.
        """
        if self.in_hand:
            in_hand = self.require
            if self.exact:
                return [in_hand]
            else:
                return [n for n in range(in_hand, min(in_deck, num_hand) + 1)]
        else:
            in_hand = min(in_deck - self.require, num_hand)
            if self.exact:
                return [in_hand]
            else:
                return [n for n in range(in_hand + 1)]

    def _gen_card_cond(self, in_deck: int, num_hand: int) -> CardCondition:
        """Return a CardCondition having a card name, # of cards in a deck
        and a list of possible # of cards in a hand.

        :param in_deck: # of cards in a deck.
        :param num_hand: # of cards in a hand.
        """
        return CardCondition(self.name, in_deck,
                             self._in_hand_candidates(in_deck, num_hand))

    def gen_card_conditions(self, num_hand: int) -> List[CardCondition]:
        """Return a list of CardCondition varying # of cards in a deck.

        :param num_hand: # of cards in a hand.
        """
        conditions = []
        for in_deck in range(self.min, self.max + 1):
            conditions.append(self._gen_card_cond(in_deck, num_hand))

        return conditions
