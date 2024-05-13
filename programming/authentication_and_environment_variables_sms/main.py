# Authentication: Authentication is the process of verifying a user’s identity. It’s about confirming that users are
# who they claim to be.
# On the other hand, authorization is the process of granting access to resources based on user permissions12.
# Once a user’s identity has been authenticated, the system then determines what information the user is allowed to
# access and what actions they are allowed to perform

# Here are some authentication methods:
# 1. Basic Auth
# 2. OpenID Connect (OIDC) and OAuth
# 3. API keys, etc.

# UTC - Coordinated Universal Time
# IST is 5:30 hours ahead of utc

# API Authentication: Authenticate ourselves to access more valuable data.
# ** APIs key is like a personal password which the API provider uses to track how much you are using the API and
# to authorize the access and deny it once reached the limit.
# Paid APIs which have important data which people can buy generally have API Authentication

# NOTE: ** Most Imp is to read the docs for APIs.

import requests
import os
from twilio.rest import Client  # From the API docs

# NOTE: ** Need to run/declare environment variables each time before running the program, can create a script or
# add in the run command itself. Run in bash terminal if using export command as it is a linux command.
OPEN_WEATHER_API_KEY = os.environ.get("OPEN_WEATHER_API_KEY")  # Importing Environment Variables from Operating System
OPEN_WEATHER_URL = os.environ.get("OPEN_WEATHER_URL")  # By Default, forecasts are every 3 hours starting
# from the time you made the request.
LATITUDE = os.environ.get("LATITUDE")
LONGITUDE = os.environ.get("LONGITUDE")

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": OPEN_WEATHER_API_KEY,  # Using API Key, passing as a param.
    # If not proper, generally gives 401 Unauthorized: meaning not authorized to access data.
    "cnt": 4,  # Only 3 timestamps, from the time the request was made. Next 12 hours data, if we make req each morning.
}


response = requests.get(url=OPEN_WEATHER_URL, params=weather_params)
response.raise_for_status()
data = response.json()  # Code and what condition it represents
# https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# print(data["list"][0]["weather"][0]["id"])
# Code less than 7XX (less than 700) means it will rain or snow.
will_rain: bool = False
for weather_hour_data in data["list"]:  # Gives weather codes for the next 12 hours, if at any given pt
    # in next 12 hours we have code < 700, meaning it will rain.
    weather_code = weather_hour_data["weather"][0]["id"]
    if weather_code < 700:
        print("Its Raining")
        will_rain = True
        break

if will_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)  # From API docs
    message = client.messages.create(
        from_='+13192203159',
        to='+919284236475',
        body="Its Going to Rain, Take Umberella☔"
    )
    print(message.status)  # To check if the message sent successfully

# NOTE: ** When running twilio on cloud which uses proxy: https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
# for a free account and dedicated server and actual address for a paid version.
# Refer below code: The Twilio API client needs to be told how to connect to the proxy server that free accounts
# use to access the external Internet.

# import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']} # ** Gets https_proxy set in the cloud env/os.
#
# account_sid = 'your account id here'
# auth_token = 'your twilio token here'
#
# client = Client(account_sid, auth_token, http_client=proxy_client)
#
# # twilio api calls will now work from behind the proxy:
# message = client.messages.create(to="...", from_='...', body='...')

# NOTE :
# A dedicated proxy server, also known as a private proxy, is a specific IP address that is only used by one person.
# When a user connects to the internet through a dedicated proxy, the proxy routes the user's web requests through its
# own server, masking the user's real IP address. This gives the user complete control over how and when they use the
# IP address, and which websites they visit.

# A proxy server is a computer with its own IP address that acts as an intermediary between a device and the internet.
# When a user uses a proxy server, their web requests are sent through the proxy server's address first, and then to
# the website. This conceals the user's real IP address and can be used to boost web privacy and bypass content filters.
# Proxy servers can also be set up as firewalls or web filters to protect a computer from internet threats like malware
