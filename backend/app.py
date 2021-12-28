from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/player/<int:player>")
def player(player: int):
    data = {
        "player": player,
        "buildings": {
            "Wheat Field": 2,
            "Ranch": 1,
            "Mine": 3,
        },
        "money": 11,
    }
    return jsonify(data)
