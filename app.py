from boggle import Boggle  # import python file from other folder

from flask import Flask, redirect, session, render_template, request, jsonify

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


boggle_game = Boggle()


@app.route("/")
def index():
    board = boggle_game.make_board()

    session["game_board"] = board
    return render_template('home.html', board=board)
    # board is a variable that's accessible in home template


@app.route("/", methods=["POST"])
def check_word():
    response = request.json  # request is an object that comes with a post method   
    result_message = boggle_game.check_valid_word(session["game_board"], response["guess"])
    return jsonify(response=result_message)
