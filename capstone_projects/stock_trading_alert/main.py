import requests
from configparser import ConfigParser
from twilio.rest import Client
import datetime as dt

config = ConfigParser()
config.read(filenames=".project_config")

ALPHA_VANTAGE_API_KEY = config["stock_project"]["ALPHA_VANTAGE_API_KEY"]
NEWSAPI_API_KEY = config["stock_project"]["NEWSAPI_API_KEY"]
TWILIO_ACCOUNT_SID = config["stock_project"]["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = config["stock_project"]["TWILIO_AUTH_TOKEN"]
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE_CHANGE_NEEDED = 5
change = 0


def percentage_change(float_a: float, float_b: float) -> float:
    if float_b == 0:
        raise ValueError("The final value cannot be 0.")
    return (float_a - float_b) / float_b * 100

# TODO 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# current_date = dt.datetime.now()
# my_date = dt.datetime(year=2024, month=5, day=13)
# print(current_date > my_date)  # NOTE: **Date comparison


stock_data = False
stock_data_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": ALPHA_VANTAGE_API_KEY,
    "datatype": "json",
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_data_params)
try:
    response.raise_for_status()
except Exception as e:
    print(f"The error occured is {e}")
else:
    data = response.json()
    no_of_data = 0
    last_two_trading_days = []
    for key in data["Time Series (Daily)"]:  # Getting the first 2 items in the dictionary
        if no_of_data == 2:
            break
        last_two_trading_days.append(data["Time Series (Daily)"][key])
        no_of_data += 1
    # We need to get percentage increase or decrease with respect to the closing value of 2 days ago.
    change = percentage_change(float(last_two_trading_days[0]["4. close"]),
                               float(last_two_trading_days[1]["4. close"]))
    if abs(change) > PERCENTAGE_CHANGE_NEEDED:
        stock_data = True


# TODO 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if stock_data:
    news_params = {
        "q": COMPANY_NAME,
        "from": "2024-05-13",
        "to": "2024-05-13",
        "sortBy": "popularity",
        "apiKey": NEWSAPI_API_KEY
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()  # Can add try, expect here too
    data = response.json()["articles"][:3]

    # TODO 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    symbol_is = "🔺"
    if change < 0:
        symbol_is = "🔻"
    message: str = f"Stock Update: {COMPANY_NAME} : {change} {symbol_is}\n"
    for i in range(len(data)):  # Iterating over the first 3 articles
        message += f"{i + 1}. {data[i]["title"]} \n {data[i]["description"]} \n\n"

    # Sending the update to phone via SMS
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    msg = client.messages.create(
        from_='+13192203159',
        to='+919284236475',
        body=message
        )
    print(msg.status)


