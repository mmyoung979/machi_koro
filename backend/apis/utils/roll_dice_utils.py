# Python imports
from random import randint
from typing import List

# Local imports
from apis.utils.db_utils import query_database


def roll_dice(dice_count: int) -> int:
    """Roll 1-2 dice and get random value

    Args:
        dice_count: Number of dice to roll

    Returns:
        Value of dice roll
    """
    roll = 0
    for _ in range(dice_count):
        roll += randint(1, 6)
    return roll


def get_buildings_from_roll(roll_value: int) -> List[int]:
    """Identify buildings that activate based on dice roll

    Args:
        roll_value: Dice value rolled by player

    Returns:
        IDs of buildings that activate based on dice roll
    """
    sql = f"""
    SELECT
        id
    FROM
        buildings
    WHERE
        {roll_value} = ANY(dice_roll)
    """
    return [building[0] for building in query_database(sql)]
