# Local imports
from apis.utils.db_utils import query_database, update_database


def get_player_coins(game: int, player: int):
    """Retrieve how many coins a player has

    Args:
        game: The game being played
        player: The player whose coins we're concerned with

    Returns:
        The amount of coins a player has
    """
    sql = f"""
    SELECT
        coins
    FROM
        player_coins_mapping
    WHERE
        game = {game}
        AND player = {player}
    """
    return {
        "player": player,
        "game": game,
        "coins": query_database(sql)[0][0],
    }


def purchase_building(
    game: int,
    player: int,
    building: int,
    quantity: int,
    price: int,
) -> None:
    """Associate a building with a player if enough coins

    Args:
        game: Game to check
        player: Player with coins (or a lackthereof)
        building: Building to purchase
        quantity: How many buildings to purchase
        price: Price of an individual building

    Returns:
        Updated database
    """
    available_coins = get_player_coins(game, player)["coins"]
    if available_coins < price:
        raise ValueError("Not enough coins to purchase")

    sql = f"""
    UPDATE
        player_coins_mapping
    SET
        coins = coins - {price}
    WHERE
        game = {game}
        AND player = {game};

    UPDATE
        player_building_mapping
    SET
        quantity = quantity + {quantity}
    WHERE
        game = {game}
        AND player = {player}
        AND building = {building};
    """
    return update_database(sql)


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
    UPDATE
        player_coins_mapping
    SET
        coins = coins {operation} {amount}
    WHERE
        game = {game}
        AND player = {player}
    """
    return update_database(sql)
