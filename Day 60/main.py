from flask import Flask, render_template, request
import requests
from requests.api import get

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)