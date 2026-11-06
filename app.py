from flask import Flask, redirect, render_template, request, url_for

from functions.get_lat_lon import get_lat, get_lon
from functions.hamta_data import HamtaDataFel, hamtaData
from functions.hantera_data import giltig_indata

app = Flask(__name__)

#Jinja filter som formaterar temperaturen som kommer från API.
#ändrar punkten i tempreaturen för en komma och visar temperaturen
#med bara 1 decimal eller float
@app.template_filter("formatera_temperatur")
def formatera_temperatur(temp):
    if temp is None:
        return "Saknas temperatur"
    return f"{temp:.1f}".replace(".", ",") + " °C"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        stad = request.form["stad"]
        if not giltig_indata(stad):
            return render_template("400.html", fel="Ogiltigt stad"), 400
        return redirect(url_for("prognos", stad=stad))
    else:
        return render_template("index.html")



@app.route("/prognos/<stad>")
def prognos(stad):
    prognos_data = hamtaData(get_lat(stad), get_lon(stad))
    temperatur = prognos_data["current"]["temperature_2m"]#ändra--------------
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


@app.errorhandler(404)
def finns_inte(e):
    return render_template("400.html", fel=e), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html", fel="Internal server error"), 500

@app.errorhandler(HamtaDataFel)
def hantera_api_fel(e):
    return render_template("500.html", fel=str(e)), 502
