import flask
from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        stad = request.form["stad"]
        return redirect(url_for("stad_info", stad=stad))
    else:
        return render_template("index.html")

@app.route("/stad/<stad>")
def stad_info(stad):
    return render_template("info.html", stad=stad)