# Local imports
from apis.utils.db_utils import update_database


def update_player_coins(
    game: int,
    player: int,
    operation: str,
    amount: int,
) -> None:
    """Update a player's inventory of coins

    Args:
        game: The game being played
        player: The player whose coins we're concerned with
        operation: Add or subtract (+ or -)
        amount: The number of coins

    Returns:
        None, only updates database
    """
    sql = f"""
    UPDATE player_coins_mapping
    SET coins = coins {operation} {amount}
    WHERE game = {game}
    AND player = {player}
    """
    update_database(sql)
