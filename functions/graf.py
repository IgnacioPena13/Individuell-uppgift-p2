import plotly.express as px


def visa_forandring_dagar(data_dagar):
    datum = [dag["time"] for dag in data_dagar]
    temperaturer = [dag["temperature_2m_mean"] for dag in data_dagar]
    fig = px.bar(
        data_dagar,
        x=datum,
        y=temperaturer,
        labels={"y": "temperatur", "x": "datum", "variable": "Temperaturförändring"},
        title="Temperatur förändring i 4 dagar",
    )
    return fig.to_html(full_html=False, include_plotlyjs="cdn")


def visa_forandring_timmar(data_timmar):
    tider = [timme["time"] for timme in data_timmar]
    temperaturer = [timme["temperature_2m"] for timme in data_timmar]

    fig = px.line(
        x=tider,
        y=temperaturer,
        labels={"x": "Tid", "y": "Temperatur"},
        title="Temperaturförändring per timme",
    )
    return fig.to_html(full_html=False, include_plotlyjs="cdn")
