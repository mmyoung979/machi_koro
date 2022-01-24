"""
Create a new user account
"""
# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.player_utils import register_player, get_player_info, delete_player

# Global variables
API = Namespace(
    "player",
    description="Create a user record for a new player",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "username",
    type=str,
    location="json",
    help="Username of player to register",
    required=True,
)
PARSER.add_argument(
    "email",
    type=str,
    location="json",
    help="Email of player to register",
    required=True,
)


@API.route("/", strict_slashes=False)
class Register(Resource):
    def post(self):
        args = PARSER.parse_args()
        return register_player(args.username, args.email)

    def get(self):
        args = PARSER.parse_args()
        return get_player_info(args.username, args.email)

    def delete(self):
        args = PARSER.parse_args()
        return delete_player(args.username, args.email)
