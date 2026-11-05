from flask import Flask, redirect, render_template, request, url_for

from functions.get_lat_lon import get_lat, get_lon
from functions.hamtaData import hamtaData

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stad = request.form["stad"]
        return redirect(url_for("prognos", stad=stad))
    else:
        return render_template("index.html")


@app.route("/prognos/<stad>")
def prognos(stad):
    prognos_data = hamtaData(get_lat(stad), get_lon(stad))
    temperatur = round(prognos_data["current"]["temperature_2m"])
    temperatur2f = prognos_data["current"]["temperature_2m"]
    kannsSom = prognos_data["current"]["apparent_temperature"]
    tempEnhet = prognos_data["current_units"]["temperature_2m"]
    return render_template(
        "prognos.html",
        stad=stad,
        temperatur=temperatur,
        temperatur2f=temperatur2f,
        kannsSom=kannsSom,
        tempEnhet=tempEnhet,
    )
