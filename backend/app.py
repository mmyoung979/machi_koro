"""
Online version of Machi Koro
"""
# Third party imports
from flask import Flask
from flask_cors import CORS
from flask_restx import Api

# Local imports
from apis import NAMESPACES


def create_app():
    """create and configure the app"""
    app = Flask(__name__)
    CORS(app)
    api = Api(app)
    for namespace in NAMESPACES:
        api.add_namespace(namespace)
    return app


# Instantiate app
app = create_app()
