import flask
from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")
