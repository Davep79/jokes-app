from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_joke', methods=["POST"])
def get_joke():
    # Fetch from 'Misc' category which includes husband-wife humor, allow both types
    url = "https://v2.jokeapi.dev/joke/Misc?type=any&safe-mode"
    response = requests.get(url)
    data = response.json()

    if data.get("type") == "single":
        joke = data.get("joke", "Oops! No joke found.")
    elif data.get("type") == "twopart":
        setup = data.get("setup", "")
        delivery = data.get("delivery", "")
        joke = f"{setup}\n\n{delivery}"
    else:
        joke = "Oops! Couldn't fetch a joke."

    return jsonify(joke=joke)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5151, debug=True)