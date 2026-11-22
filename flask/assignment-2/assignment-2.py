import json
import os
from flask import Flask, jsonify

app = Flask(__name__)
DICTIONARY_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dictionary.json")

def load_dictionary():
    with open(DICTIONARY_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return {english.lower(): finnish for english, finnish in data.items()}


@app.route("/translate/<word>", methods=["GET"])
def translate(word):
    dictionary = load_dictionary()
    key = word.strip().lower()

    if key not in dictionary:
        return jsonify({"error": "Word not found"}), 404

    return jsonify({"English": key, "Finnish": dictionary[key]})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)