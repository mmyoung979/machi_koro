"""
Test the dice roll functionality and all possible outcomes
"""
# Python imports
from unittest import mock

# Local imports
from apis.utils.roll_dice_utils import roll_dice, get_buildings_from_roll


class TestRollDice:
    @mock.patch("apis.utils.roll_dice_utils.randint", return_value=3)
    def test_roll_dice(self, rand):
        assert roll_dice(1) == 3
        assert roll_dice(2) == 6
        rand.return_value = 4
        assert roll_dice(1) == 4
        assert roll_dice(2) == 8

    def test_get_buildings_from_roll(self):
        assert get_buildings_from_roll(1) == [1]
        assert get_buildings_from_roll(2) == [2, 3]
        assert get_buildings_from_roll(3) == [3, 4]
        assert get_buildings_from_roll(4) == [5]
        assert get_buildings_from_roll(5) == [6]
        assert get_buildings_from_roll(6) == [7, 8, 9]
        assert get_buildings_from_roll(7) == [10]
        assert get_buildings_from_roll(8) == [11]
        assert get_buildings_from_roll(9) == [12, 13]
        assert get_buildings_from_roll(10) == [13, 14]
        assert get_buildings_from_roll(11) == [15]
        assert get_buildings_from_roll(12) == [15]
