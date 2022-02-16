"""Test search.py"""

from pathlib import Path

import pytest
from dopt.card.card import CardCondition
from dopt.card.deck import Deck
from dopt.exceptions import SettingsNotSetError
from dopt.search.search import Searcher
from dopt.search.setting import SearchSetting


class TestSearcher:
    @pytest.fixture(scope="class")
    def empty_class(self):
        """Return an empty Searcher."""
        yield Searcher()

    @pytest.fixture(scope="class")
    def normal_sample(self):
        """Yield a Searcher initialized by test_config.yaml"""
        path_to_test_file = Path(__file__).parent / "test_file" / "test_config.yaml"
        s = Searcher()
        s.load_settings(path_to_test_file)
        yield s

    @pytest.fixture(scope="class")
    def too_small_deck(self):
        """Yield a Searcher inititalized by test_small_deck.yaml."""
        path_to_test_file = Path(__file__).parent / "test_file" / "test_small_deck.yaml"
        s = Searcher()
        s.load_settings(path_to_test_file)
        yield s

    def test_load_settings(self, normal_sample):
        """Test Searcher.load_settings."""
        ans = {
            "num_hand": 5,
            "num_deck": {"min": 40, "max": 41},
            "condition": [SearchSetting("Gamma", 3, 3, 1, False, True),
                          SearchSetting("Driver", 1, 1, 1, True, False)]
        }
        assert normal_sample.settings == ans

    def test_gen_decks(self, normal_sample, too_small_deck):
        """Test Searcher._gen_decks."""
        cds = [CardCondition("Gamma", 3, [1, 2, 3]),
               CardCondition("Driver", 1, [0])]
        ans_decks = [Deck(40, cds), Deck(41, cds)]

        assert list(normal_sample._gen_decks()) == ans_decks

        assert list(too_small_deck._gen_decks()) == []

    def test_save_prob(self, empty_class, normal_sample):
        """Test Seacher._save_prob."""
        d1 = Deck(40, [])
        d2 = Deck(41, [])
        d3 = Deck(42, [])

        empty_class._save_prob(d1, 0.1)
        empty_class._save_prob(d2, 0.2)
        empty_class._save_prob(d3, 0.05)

        assert empty_class.result[d1] == 0.1
        assert empty_class.result[d2] == 0.2
        assert empty_class.result[d3] == 0.05
        assert empty_class.best_deck == d2
        assert empty_class.best_prob == 0.2

    def test_search(self, empty_class, normal_sample):
        """Test Seacher.search."""
        with pytest.raises(SettingsNotSetError):
            empty_class.search()

        normal_sample.search()

        cds = [CardCondition("Gamma", 3, [1, 2, 3]),
               CardCondition("Driver", 1, [0])]
        assert normal_sample.best_deck == Deck(40, cds)
        assert normal_sample.best_prob == pytest.approx(0.302, 0.001)

    def test_summary(self, empty_class):
        """Test Seacher.summary."""
        with pytest.raises(SettingsNotSetError):
            empty_class.search()
