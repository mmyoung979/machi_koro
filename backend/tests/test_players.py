"""
Test user functionality
"""
# Local imports
from app import create_app


class TestEntireGame:
    def test_create_player(self):
        test_app = create_app()
        with test_app.test_client() as cli:
            # Create user
            resp = cli.post(
                "/player",
                json={
                    "username": "test_player1",
                    "email": "test_player1@gmail.com",
                },
            )
            assert resp.status_code == 201

    def test_get_player_info(self):
        test_app = create_app()
        with test_app.test_client() as cli:
            resp = cli.get(
                "/player",
                json={
                    "username": "test_player1",
                    "email": "test_player1@gmail.com",
                },
            )
            assert resp.status_code == 200

    def test_delete_player(self):
        test_app = create_app()
        with test_app.test_client() as cli:
            resp = cli.delete(
                "/player",
                json={
                    "username": "test_player1",
                    "email": "test_player1@gmail.com",
                },
            )
            assert resp.status_code == 204
