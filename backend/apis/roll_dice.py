# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Local imports
from apis.utils.roll_dice_utils import roll_dice, get_buildings_from_roll

# Global variables
API = Namespace(
    "roll",
    description="Player rolls 1-2 dice for their turn",
)
PARSER = reqparse.RequestParser()
PARSER.add_argument(
    "dice_count",
    type=int,
    help="Number of dice to roll (1 or 2)",
    required=True,
)


@API.route("/", strict_slashes=False)
class RollDice(Resource):
    def get(self):
        args = PARSER.parse_args()
        roll = roll_dice(args.dice_count)
        buildings = get_buildings_from_roll(roll)
        return buildings
