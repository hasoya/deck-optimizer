"""Test setting.py"""

import pytest
from dkopt.card.card import CardCondition
from dkopt.search.setting import SearchSetting


class TestSearchSetting:
    @pytest.fixture(scope="class")
    def exact_case(self):
        """# of "a" in a hand is equal to two."""
        yield SearchSetting("a", 2, 3, 2, True, True)

    @pytest.fixture(scope="class")
    def non_exact_case(self):
        """# of "b" in a hand is more than equal to three."""
        yield SearchSetting("b", 3, 5, 3, False, True)

    @pytest.fixture(scope="class")
    def exact_not_in_hand(self):
        """# of "c" in a deck is equal to two."""
        yield SearchSetting("c", 2, 2, 2, True, False)

    @pytest.fixture(scope="class")
    def non_exact_not_in_hand(self):
        """# of "d" in a deck is more than equal to one."""
        yield SearchSetting("d", 2, 2, 1, False, False)

    def test_in_hand_candidates(self, exact_case, non_exact_case,
                                exact_not_in_hand, non_exact_not_in_hand):
        """Test SearchSetting._in_hand_candidates."""
        ans = [2]
        assert ans == exact_case._in_hand_candidates(3, 5)

        ans = [3]
        assert ans == non_exact_case._in_hand_candidates(3, 5)

        ans = [0]
        assert ans == exact_not_in_hand._in_hand_candidates(2, 5)

        ans = [0, 1]
        assert ans == non_exact_not_in_hand._in_hand_candidates(2, 5)

    def test_gen_card_cond(self, exact_case, non_exact_case,
                           exact_not_in_hand, non_exact_not_in_hand):
        """Test SearchSetting._gen_card_cond."""
        ans = CardCondition("a", 3, [2])
        assert ans == exact_case._gen_card_cond(3, 5)

        ans = CardCondition("b", 3, [3])
        assert ans == non_exact_case._gen_card_cond(3, 5)

        ans = CardCondition("c", 2, [0])
        assert ans == exact_not_in_hand._gen_card_cond(2, 5)

        ans = CardCondition("d", 2, [0, 1])
        assert ans == non_exact_not_in_hand._gen_card_cond(2, 5)

    def test_gen_card_conditions(self, exact_case, non_exact_case,
                                 exact_not_in_hand, non_exact_not_in_hand):
        """Test SearchSetting.gen_card_conditions."""
        ans = [CardCondition("a", 2, [2]), CardCondition("a", 3, [2])]
        assert ans == exact_case.gen_card_conditions(5)

        ans = [CardCondition("b", 3, [3]),  CardCondition("b", 4, [3, 4]),
               CardCondition("b", 5, [3, 4, 5])]
        assert ans == non_exact_case.gen_card_conditions(5)

        ans = [CardCondition("c", 2, [0])]
        assert ans == exact_not_in_hand.gen_card_conditions(5)

        ans = [CardCondition("d", 2, [0, 1])]
        assert ans == non_exact_not_in_hand.gen_card_conditions(5)
