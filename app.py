from flask import Flask, redirect, render_template, request, url_for

from functions.get_lat_lon import get_lat, get_lon
from functions.graf import visa_forandring_dagar, visa_forandring_timmar
from functions.hamta_data import HamtaDataFel, hamtaData
from functions.hantera_data import giltig_indata, matchaAllaDaily, matchaAllaHourly

app = Flask(__name__)


# Jinja filter som formaterar temperaturen som kommer från API.
# ändrar punkten i tempreaturen för en komma och visar temperaturen
# med bara 1 decimal eller float
@app.template_filter("formatera_temperatur")
def formatera_temperatur(temp):
    if temp is None:
        return "Saknas temperatur"
    return f"{temp:.1f}".replace(".", ",") + " °C"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stad = request.form.get("stad")
        if not giltig_indata(stad):
            return render_template("400.html", fel="Ogiltigt stad"), 400
        return redirect(url_for("prognos", stad=stad))
    return render_template("index.html")


@app.route("/prognos/<stad>")
def prognos(stad):
    # om jag inte hadde detta if-sats skulle API hämta data från koordinaterna 0,0
    # och om jag skriver /prognos/programmering kommer programmering visas som en stad
    # med vädret på 0,0 koordinaterna
    if not giltig_indata(stad):
        return render_template("400.html", fel=f"{stad} finns inte, testa något annat stad :)"), 400
    prognos_data = hamtaData(get_lat(stad), get_lon(stad))
    vader = prognos_data["current"]
    timmarna = matchaAllaHourly(prognos_data)
    dagarna = matchaAllaDaily(prognos_data)
    graf_dagar = visa_forandring_dagar(dagarna)
    graf_timmar = visa_forandring_timmar(timmarna)
    return render_template(
        "prognos.html",
        stad=stad,
        vader=vader,
        timmarna=timmarna,
        dagarna=dagarna,
        graf_dagar=graf_dagar,
        graf_timmar=graf_timmar,
    )


@app.errorhandler(404)
def finns_inte(e):
    return render_template("400.html", fel="Sidan hittades inte"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html", fel="Internal server error"), 500


@app.errorhandler(HamtaDataFel)
def hantera_api_fel(e):
    return render_template("500.html", fel=str(e)), 502
