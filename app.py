from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_joke', methods=["POST"])
def get_joke():
    # Request a single-part programming joke from JokeAPI
    response = requests.get("https://v2.jokeapi.dev/joke/Programming?type=single")
    data = response.json()
    joke = data.get("joke", "Oops! No joke found.")
    return jsonify(joke=joke)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5151, debug=True)
