"""
A player in a game purchases 1 or more of a building.
This does not include landmarks.
"""
# Third party imports
from flask import jsonify, make_response
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.purchase_utils import purchase_building

# Global variables
API = Namespace(
    "purchase",
    description="Player purchases one or more buildings",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "game",
    type=int,
    location="json",
    help="ID of game being played",
    required=True,
)
PARSER.add_argument(
    "player",
    type=int,
    location="json",
    help="Player who is purchased a building",
    required=True,
)
PARSER.add_argument(
    "building",
    type=int,
    location="json",
    help="Building being purchased",
    required=True,
)
PARSER.add_argument(
    "quantity",
    type=int,
    location="json",
    help="Number of buildings being purchased",
    required=True,
)
PARSER.add_argument(
    "price",
    type=int,
    location="json",
    help="Price of building",
    required=True,
)


@API.route("/", strict_slashes=False)
class Purchase(Resource):
    def post(self):
        """
        1. Check if a player has enough coins
        2. Remove coins from player
        3. Associate building(s) with player
        """
        args = PARSER.parse_args()
        resp = purchase_building(
            args.game,
            args.player,
            args.building,
            args.quantity,
            args.price,
        )
        return make_response(jsonify(resp), 201)
