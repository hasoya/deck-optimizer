"""Contain Searcher to find the best deck composition."""

from itertools import product
from pathlib import Path
from typing import Dict, Generator, Optional

import yaml
from dkopt.card.deck import Deck
from dkopt.exceptions import NoDeckError, SettingsNotSetError
from dkopt.search.setting import SearchSetting


class Searcher:
    """Find the best number of the cards in deck by calculating probability of the ideal hands.

    :param settings: SearchSettings loaded from config yaml file.
    :param best_deck: The best deck found by Searcher.search.
    :param best_prob: The highest prob of the ideal hand given by the best deck.
    :param result: A map {deck->prob} calculated by Searcher.search.
    """

    def __init__(self) -> None:
        self.settings: Dict = {}
        self.best_deck: Optional[Deck] = None
        self.best_prob = 0.0
        self.result: Dict[Deck, float] = {}

    def load_settings(self, path: Path) -> None:
        """Load setting yaml file, and create CardCondition object.

        :param path: A path to config yaml file.
        """
        # Load file.
        with open(path) as file:
            settings = yaml.safe_load(file)

        # Put Hand and Deck settings.
        self.settings["num_hand"] = settings["num_hand"]
        self.settings["num_deck"] = settings["num_deck"]

        # Make a CardCondition from each condition setting.
        self.settings["condition"] = []
        for cond in settings["condition"]:
            ss = SearchSetting(**cond)
            self.settings["condition"].append(ss)

    def _gen_decks(self) -> Generator[Deck, None, None]:
        """Generate candidate deck from settings."""
        # Enumerate all conditions.
        all_conditions = []
        num_hand = self.settings["num_hand"]
        for ss in self.settings["condition"]:
            all_conditions.append(ss.gen_card_conditions(num_hand))

        # Condition iteration.
        for cond_comb in product(*all_conditions):
            # Count all num_in_deck.
            total_in_deck = sum([c.num_in_deck for c in cond_comb])

            # Deck iteration.
            for dnum in range(self.settings["num_deck"]["min"],
                              self.settings["num_deck"]["max"] + 1):
                if total_in_deck <= dnum:  # Check if total cards does not exceed.
                    yield Deck(dnum, list(cond_comb))

    def _save_prob(self, deck: Deck, prob: float) -> None:
        """"Save the probability of ideal hand for each deck."""
        if self.best_prob < prob:
            self.best_deck = deck
            self.best_prob = prob
        self.result[deck] = prob

    def search(self) -> None:
        """Calculate the prob of all deck candidates."""
        if not self.settings:
            raise SettingsNotSetError("Use load_settings before")

        # For each deck, calculate prob of the ideal hand and save the result
        for deck in self._gen_decks():
            h = deck.gen_hands(self.settings["num_hand"])
            prob = h.calc_prob()
            self._save_prob(deck, prob)

        if not self.best_deck:
            raise NoDeckError("No deck is generated, review your config file.")

    def summary(self) -> None:
        """Show a report of a search result.

        :raises NotImplementedError: _description_
        """
        if not self.settings:
            raise SettingsNotSetError("Use load_settings before")

        raise NotImplementedError
