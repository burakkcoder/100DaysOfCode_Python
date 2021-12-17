import requests
from twilio.rest import Client

account_sid = "0"
auth_token = "0"
client = Client(account_sid, auth_token)

STOCK_NAME = "BTCUSD"
COMPANY_NAME = "BITCOIN / DOLAR"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "0"
STOCK_API_KEY = "0"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday = data_list[0]
yesterday_closing_price = yesterday["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100, 2)

if diff_percent > 0:
    new_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle":COMPANY_NAME
    }
    new_response = requests.get(NEWS_ENDPOINT, params=new_params)
    articles = new_response.json()["articles"]
    three_art = articles[:1]

    formatted = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHaber Başlığı: {x['title']}.\nBilgi: {x['description']}" for x in three_art]

for article in formatted:
    message = client.messages \
        .create(
        body=article,
        from_='+0',
        to='+0'
    )
    print(message.sid)
