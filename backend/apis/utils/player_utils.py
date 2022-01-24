"""
Player CRUD functionality
"""
# Third party imports
from flask import jsonify, make_response

# Local imports
from apis.utils.db_utils import query_database, update_database


def register_player(username: str, email: str):
    """Create new player record

    Args:
        username: What to call the player
        email: Email address where player can be reached

    Returns:
        New record with user information
    """
    sql = f"""
    INSERT INTO
        players (username, email)
    VALUES
        ('{username}', '{email}');
    """
    return make_response(jsonify(update_database(sql)), 201)


def get_player_info(username: str, email: str):
    """View database info about a player

    Args:
        username: What to call the player
        email: Email address where player can be reached

    Returns:
        Existing record with user information
    """
    sql = f"""
    SELECT
        username, email, wins
    FROM
        players
    WHERE
        username = '{username}'
        AND email = '{email}';
    """
    return make_response(jsonify(query_database(sql)), 200)


def update_player(username: str, email: str):
    """Update existing player record

    Args:
        username: What to call the player
        email: Email address where player can be reached

    Returns:
        Updated record with user information
    """
    pass


def delete_player(username: str, email: str) -> None:
    """Delete existing player record

    Args:
        username: What to call the player
        email: Email address where player can be reached

    Returns:
        Deleted user record
    """
    sql = f"""
    DELETE FROM
        players
    WHERE
        username = '{username}'
        AND email = '{email}';
    """
    return make_response(jsonify(update_database(sql)), 204)
