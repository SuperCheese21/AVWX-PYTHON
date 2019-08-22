import requests
from pyquery import PyQuery


def get_metar_data(icao):
    url = f"https://www.aviationweather.gov/metar/data?ids={icao}&format=decoded"
    html = requests.get(url).text
    document = PyQuery(html)

    text = document("#awc_main_content_wrap b").text()
    if text == 'No data found':
        return {}

    metar = {}
    for row in document("#awc_main_content_wrap tr"):
        row_data = PyQuery(row)

        label = row_data("span").text().replace(" ", "").replace(":", "").lower()
        data = row_data("td").eq(1).text()

        if "pressure" in label:
            metar["altimeter"] = data.split(" ")[0]
        elif "temperature" in label or "dewpoint" in label:
            metar[label] = data.split("\u00b0")[0]
        elif "visibility" in label:
            metar[label] = data.split(" ")[0]
        elif "metar" not in label:
            metar[label] = data

    return metar
