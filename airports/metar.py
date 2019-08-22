import requests


def get_metar_data(icao):
    url = f"https://www.aviationweather.gov/metar/data?ids={icao}&format=decoded"
    data = requests.get(url)
    return {}
