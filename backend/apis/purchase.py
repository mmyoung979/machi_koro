# Third party imports
from flask_restful import Resource, reqparse

# Local imports
from apis.utils.db_utils import query_database, update_database
from apis.utils.purchase_utils import update_player_coins

# Global variables
parser = reqparse.RequestParser()
parser.add_argument("game", type=int, help="ID of game being played", required=True)
parser.add_argument(
    "player", type=int, help="Player who is purchased a building", required=True
)
parser.add_argument(
    "building", type=int, help="Building being purchased", required=True
)
parser.add_argument("price", type=int, help="Price of building", required=True)


class Purchase(Resource):
    def get(self):
        args = parser.parse_args()
        game = args.game
        player = args.player
        building = args.building
        price = args.price

        update_player_coins(game, player, "-", price)

        sql = f"""
        SELECT
            player,
            building,
            quantity
        FROM
            player_building_mapping
        WHERE
            game = {game}
            AND player = {player}
            AND building = {building}
        """
        results = query_database(sql)
        if results:
            player, building, quantity = results[0]
            return {
                "player": player,
                "building": building,
                "quantity": quantity,
            }

    def post(self):
        args = parser.parse_args()
        game = args.game
        player = args.player
        building = args.building
        sql = f"""
        UPDATE
            player_building_mapping
        SET
            quantity = quantity + 1
        WHERE
            game = {game}
            AND player = {player}
            AND building = {building}
        """
        update_database(sql)
        return "200"
