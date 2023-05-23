import requests


OWM_API_KEY = "a5f02a0ba43bf499b17a3b1f27eeb2b8"
OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/onecall"

params = {
    "lat":123,
    "lon":456,
    "appid": OWM_API_KEY
}

response = requests.get(OWM_ENDPOINT, params=params)