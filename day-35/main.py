import requests
from twilio.rest import Client
import os

OWN_Endpoint = os.environ.get("OWN_Endpoint")

api_key =""
account_sid =os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

parameters = {
    "appid": "",
    "lat": "",
    "long": "",
    "exclude": "current, minutely, daily"
}

response = requests.get(OWN_Endpoint, params = parameters)
weather = response.json()
weather_slice = weather["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain = True


if will_rain:
    client = Client(account_sid,auth_token)
    # message = client.message\
    #         .create(
    #     body="It's gonna rain",
    #     from="",
    #     to=""
    # )


response.raise_for_status()
