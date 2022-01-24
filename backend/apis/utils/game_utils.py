# Python imports
from typing import List

# Third party imports
from flask import make_response, jsonify

# Local imports
from apis.utils.db_utils import query_database, update_database


def start_game(players: List[int]) -> None:
    # Make sure all player slots are full
    players = fill_players(players)

    # Create game table record
    sql = f"""
    INSERT INTO
        games (player1, player2, player3, player4)
    VALUES
        ({players[0]}, {players[1]}, {players[2]}, {players[3]});
    """

    game = "(SELECT MAX(id) FROM games)"

    for player in players:
        if player != "NULL":
            # Assign initial landmarks to players:
            for landmark in range(1, 5):
                sql += f"""
                INSERT INTO
                    player_landmark_mapping (game, player, landmark)
                VALUES
                    ({game}, {player}, {landmark});
                """

            # Assign initial buildings to players
            for building in range(1, 3):
                sql += f"""
                INSERT INTO
                    player_building_mapping (game, player, building, quantity)
                VALUES
                    ({game}, {player}, {building}, 1);
                """

            # Create rows for buildings to be purchased later
            for building in range(3, 16):
                sql += f"""
                INSERT INTO
                    player_building_mapping (game, player, building, quantity)
                VALUES
                    ({game}, {player}, {building}, 0);
                """

            # Give each player 3 coins to start
            sql += f"""
            INSERT INTO
                player_coins_mapping (game, player, coins)
            VALUES
                ({game}, {player}, 3);
            """
    make_response(jsonify(update_database(sql)), 201)


def get_game_info(players: List[int]):
    # Make sure all player slots are full
    players = fill_players(players)

    player1, player2, player3, player4 = players
    fields = [
        "id",
        "player1",
        "player2",
        "player3",
        "player4",
        "winner",
        "created_at",
        "updated_at",
    ]
    sql = f"""
    SELECT
        {",".join(fields)}
    FROM
        games
    WHERE
        player1 = {player1}
        AND player2 = {player2}
        AND player3 = {player3}
        AND player4 = {player4}
    """
    results = query_database(sql)
    if results:
        resp = dict(zip(fields, results[0]))
        return make_response(jsonify(resp), 200)
    return make_response("No game found with those players", 404)


def player_error_checking(players: List[int]) -> None:
    if not players:
        raise ValueError("No players recognized.")
    if type(players) != list:
        raise TypeError("Players entered in incorrect format.")
    if len(players) < 2:
        raise ValueError("Minimum of 2 players required.")
    if len(players) > 4:
        raise ValueError("Maximum of 4 players allowed.")


def fill_players(players: List[int]) -> List[int]:
    # Fill in empty player slots
    while len(players) < 4:
        players.append("NULL")
    return players
