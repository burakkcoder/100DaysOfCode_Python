import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "0"
account_sid = "0"
auth_token = "0"
client = Client(account_sid, auth_token)

parameters = {
    "lat": 40.762402,
    "lon": 29.932949,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=parameters)
data = response.json()
data_weather_id = data["hourly"][0]["weather"][0]["id"]

will_rain = False

for x in range(0,13):
    weather_condition = data["hourly"][x]["weather"][0]["id"]
    if weather_condition < 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="Bugün yağmur var, şemsiyeni al!",
        from_='+000000000',
        to='+000000000'
    )
    print(message.sid)