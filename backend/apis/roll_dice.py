# Python imports
from random import randint

# Third party imports
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument(
    "dice_count", type=int, help="Number of dice to roll (1 or 2)", required=True
)


class RollDice(Resource):
    def get(self):
        args = parser.parse_args()
        dice_count = args.dice_count
        roll = 0
        for _ in range(dice_count):
            roll += randint(1, 6)
        return roll
