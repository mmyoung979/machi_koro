"""
A player activates a landmark
"""
# Third party imports
from flask_restx import Namespace, Resource, reqparse

# Global variables
API = Namespace(
    "activate_landmark",
    description="Activate a player's landmark",
)
PARSER = reqparse.RequestParser()


@API.route("/", strict_slashes=False)
class ActivateLandmark(Resource):
    def post(self):
        args = PARSER.parse_args()
