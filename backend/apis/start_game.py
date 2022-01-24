"""
Create a new game with 2-4 players
"""
# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.game_utils import player_error_checking, start_game

# Global variables
API = Namespace(
    "start_game",
    description="Give players initial landmarks, buildings, and coins",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "players",
    type=list,
    location="json",
    help="List of players in game",
    required=True,
)


class StartGame(Resource):
    def post(self):
        args = PARSER.parse_args()
        players = args.players

        # Make sure players were entered correctly
        player_error_checking(players)

        # Fill in empty player slots
        while len(players) < 4:
            players.append("NULL")

        # Begin the game
        start_game(players)
