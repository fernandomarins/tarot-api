from flask import Flask, jsonify
from tarot import cards
from rune import runes
from daemon import daemons
from sangoma import sangoma
from alphabet import alphabet
from astrology import astrology
from hoodoo import hoodoo
from herbs import herbs

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_all_cards():
    return jsonify(cards)

@app.route("/runes", methods=["GET"])
def get_all_runes():
    return jsonify(runes)


@app.route("/daemons", methods=["GET"])
def get_all_daemons():
    return jsonify(daemons)

@app.route("/sangoma", methods=["GET"])
def get_all_bones():
    return jsonify(sangoma)

@app.route("/alphabet", methods=["GET"])
def get_all_letters():
    return jsonify(alphabet)

@app.route("/astrology", methods=["GET"])
def get_astrology():
    return jsonify(astrology)

@app.route("/hoodoo", methods=["GET"])
def get_hoodoo():
    return jsonify(hoodoo)
    
@app.route("/herbs", methods=["GET"])
def get_herbs():
    return jsonify(herbs)

if __name__ == "__main__":
    app.run(debug=True)
