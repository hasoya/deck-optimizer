"""Test search.py"""

from pathlib import Path

import pytest
from dopt.search.search import Searcher
from dopt.search.setting import SearchSetting


class TestSearcher:
    @pytest.fixture(scope="class")
    def empty_class(self):
        """Return Searcher."""
        yield Searcher()

    def test_load_settings(self, empty_class):
        """Test Searcher.load_settings."""
        path_to_test_file = Path(__file__) / "test_file" / "test_config.yaml"

        empty_class.load_settings(path_to_test_file)

        ans = {
            "num_hand": 5,
            "num_deck": {"min": 40, "max": 60},
            "condition": [SearchSetting("Gamma", 3, 3, 1, False, True),
                          SearchSetting("Driver", 1, 1, 1, True, False)]
        }
        assert empty_class.settings == ans

    def test_gen_decks(self):
        """Test Searcher._gen_decks."""
