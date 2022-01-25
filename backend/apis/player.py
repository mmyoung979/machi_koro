"""
Create a new player account
"""
# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.player_utils import register_player, get_player_info, delete_player

# Global variables
API = Namespace(
    "player",
    description="Interact with player records",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "username",
    type=str,
    location="json",
    help="Username of player",
    required=True,
)
PARSER.add_argument(
    "email",
    type=str,
    location="json",
    help="Email of player",
    required=True,
)


@API.route("/", strict_slashes=False)
class Player(Resource):
    def post(self):
        """Create player"""
        args = PARSER.parse_args()
        return register_player(args.username, args.email)

    def get(self):
        """Get player"""
        args = PARSER.parse_args()
        return get_player_info(args.username, args.email)

    def delete(self):
        """Delete player"""
        args = PARSER.parse_args()
        return delete_player(args.username, args.email)
