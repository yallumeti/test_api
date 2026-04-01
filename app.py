from flask import Flask, jsonify
from flask import render_template
import requests

app = Flask(__name__)

@app.route("/posts")
def posts():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/posts").json())

@app.route("/comments")
def comments():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/comments").json())

@app.route("/albums")
def albums():
    return jsonify(requests.get("https://jsonplaceholder.typicode.com/albums").json())

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
