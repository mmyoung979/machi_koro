"""
Test the creation of a game
"""
# Local imports
from app import create_app


class TestGame:
    def test_game_post(self):
        test_app = create_app()
        with test_app.test_client() as cli:
            # Create players
            cli.post(
                "/player",
                json={
                    "username": "player1",
                    "email": "player1@gmail.com",
                },
            )
            cli.post(
                "/player",
                json={
                    "username": "player2",
                    "email": "player2@gmail.com",
                },
            )
            cli.post(
                "/player",
                json={
                    "username": "player3",
                    "email": "player3@gmail.com",
                },
            )
            cli.post(
                "/player",
                json={
                    "username": "player4",
                    "email": "player4@gmail.com",
                },
            )
            # Start game
            cli.post(
                "/game",
                json={
                    "players": [1, 2, 3, 4],
                },
            )

            # Check if game exists
            resp = cli.get(
                "/game",
                json={
                    "players": [1, 2, 3, 4],
                },
            )
            assert resp.status_code == 200

            # Check if we get an error for searching a game that doesn't exist
            resp = cli.get(
                "/game",
                json={
                    "players": [1, 2, 3],
                },
            )
            assert resp.status_code == 404
