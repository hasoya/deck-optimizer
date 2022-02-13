"""Test of hand.py"""
from dopt.card.hand import Hand
from pytest import approx


class TestHand:
    def test_calc_each_prob(self) -> None:
        """Test Hand._calc_each_prob."""
        p1 = Hand._calc_each_prob(40, 5, [6], tuple([1]))
        assert p1 == approx(0.42, 0.01)

        p2 = Hand._calc_each_prob(40, 5, [6, 9], tuple([2, 1]))
        assert p2 == approx(0.0615, 0.001)

    def test_calc_prob(self) -> None:
        """Test Hand.calc_prob."""
        h = Hand(40, 5, [6, 2],
                 [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1),
                  (4, 0), (4, 1), (5, 0)])
        p1 = h.calc_prob()

        assert p1 == approx(0.571, 0.01)
