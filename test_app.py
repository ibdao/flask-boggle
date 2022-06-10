from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')

            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('<title>Boggle</title>', html)
            # test that you're getting a template



    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            ...
            # write a test for this route
            response = client.post('/api/new-game')
            game = response.get_json()
             #html = response.get_data(as_text = True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('board', game)
            self.assertIn('gameId', game)

    def test_api_score_word(self):
        """tests to see if word is valid"""
        with app.test_client() as client:
            resp = client.post("/api/new-game")
            data = resp.get_json()
            gameId = data['gameId']
            data["board"] = [["C","A","T"], ["O", "X", "X"], ["X", "G", "X"]]
            response = client.post("/api/score-word", json= {'game_id': gameId, 'word': 'CAT'})
            json_response = response.get_json()
            
            self.assertEqual({"result": "ok"}, json_response)
            self.assertEqual(response.status_code, 200)

            
