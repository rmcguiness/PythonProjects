import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



OWM_API_KEY = "a5f02a0ba43bf499b17a3b1f27eeb2b8"
OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast?"

account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

w_params = {
    "lat":40.287102,
    "lon":-74.175880,
    "appid": OWM_API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_ENDPOINT, params=w_params)
weather_data = response.json()
hourly_data = weather_data['list'][:12]

will_rain = [True for weather in hourly_data if weather['weather'][0]['id'] < 700]

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="YOUR TWILIO VIRTUAL NUMBER",
        to="YOUR TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)

