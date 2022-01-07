# Third party imports
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument("player", type=int, help="Player who is purchased a building")
parser.add_argument("building", type=int, help="Building being purchased")


class Purchase(Resource):
    def get(self):
        args = parser.parse_args()
        player = args.player
        building = args.building
        sql = """
        UPDATE player_building_mapping
        SET building = building + 1
        """
        return {"player": player, "building": building}
