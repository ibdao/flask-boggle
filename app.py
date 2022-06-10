from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    game_info = {"gameId": game_id, "board": game.board}

    return jsonify(game_info)

@app.post("/api/score-word")
def score_word():
    """Takes word and game id checks if word is legal

        {"gameId" : "gameId_goes_here", "word": "word_goes_here"}
    
    """

    game_id = request.json["game_id"]
    word = request.json["word"]

    if not games[game_id].check_word_on_board(word):
        result = {"result": "not-on-board"}
    elif not games[game_id].is_word_in_word_list(word):
        result = {"result": "not-word"}
    else:
        result = {"result": "ok"}

    return jsonify(result)
