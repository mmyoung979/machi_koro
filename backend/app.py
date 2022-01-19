"""
Online version of Machi Koro
"""
# Third party imports
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

# Local imports
from apis.purchase import Purchase
from apis.roll_dice import RollDice


def create_app():
    """create and configure the app"""
    app = Flask(__name__)
    CORS(app)
    return app


# Instantiate app
app = create_app()
api = Api(app)
api.add_resource(Purchase, "/purchase")
api.add_resource(RollDice, "/roll")
