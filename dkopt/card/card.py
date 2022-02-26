from dataclasses import dataclass
from typing import List


@dataclass
class CardCondition:
    """Stores a name, # of cards in deck and possible # of cards in hand."""
    name: str
    num_in_deck: int
    hand_candidates: List[int]

    def __hash__(self) -> int:
        return hash(self.name) + self.num_in_deck \
            + hash(frozenset(self.hand_candidates))
