"""
CRUD API for games table objects and related data
"""
# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.game_utils import get_game_info, player_error_checking, start_game

# Global variables
API = Namespace(
    "game",
    description="CRUD API for games table objects and related data",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "players",
    type=list,
    location="json",
    help="List of player IDs",
)


@API.route("/", strict_slashes=False)
class Game(Resource):
    def post(self):
        args = PARSER.parse_args()
        players = args.get("players")

        # Make sure players were entered correctly
        player_error_checking(players)

        # Begin the game
        start_game(players)

    def get(self):
        args = PARSER.parse_args()
        players = args.get("players")

        # Make sure players were entered correctly
        player_error_checking(players)

        # Retrieve database information
        return get_game_info(players)
