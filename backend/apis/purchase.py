"""
A player in a game purchases 1 or more of a building.
This does not include landmarks.
"""
# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.db_utils import query_database, update_database
from apis.utils.purchase_utils import update_player_coins

# Global variables
API = Namespace(
    "purchase",
    description="Player purchases one or more buildings",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "game",
    type=int,
    help="ID of game being played",
    required=True,
)
PARSER.add_argument(
    "player",
    type=int,
    help="Player who is purchased a building",
    required=True,
)
PARSER.add_argument(
    "building",
    type=int,
    help="Building being purchased",
    required=True,
)
PARSER.add_argument(
    "quantity",
    type=int,
    help="Number of buildings being purchased",
    required=True,
)
PARSER.add_argument(
    "price",
    type=int,
    help="Price of building",
    required=True,
)


@API.route("/", strict_slashes=False)
class Purchase(Resource):
    def post(self):
        args = PARSER.parse_args()
        sql = f"""
        UPDATE
            player_building_mapping
        SET
            quantity = quantity + {args.quantity}
        WHERE
            game = {args.game}
            AND player = {args.player}
            AND building = {args.building}
        """
        update_database(sql)
        return 201
