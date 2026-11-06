def formatera_temperatur(temp):
    return f"{temp:.1f}".replace(".", ",") + " °C"

app.jinja_env.filters["foramtera_temperatur"] = formatera_temperatur