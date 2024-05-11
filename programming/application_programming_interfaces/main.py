# https://en.wikipedia.org/wiki/API : A software offering service to another software.
# API (Application Programming Interface): They all are a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an external system.
# Your Program ->(Request following API rules)->External Service->(Response with API rule)->Your Program

# API Endpoint: the location of the external service we are trying to reach.
# API Request: Creds/Checks to validate the transaction
# JSON data can be transferred across the internet very quickly
# Sample API: http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import requests  # Docs: https://docs.python-requests.org/en/latest/
import datetime as dt

ISS_LOCATION_URL = "http://api.open-notify.org/iss-now.json"
MY_LATITUDE = 21.152451
MY_LONGITUDE = 79.080559

response = requests.get(url=ISS_LOCATION_URL)
print(response)  # <Response [200]>
print(response.json())

# Status Codes : https://www.webfx.com/web-development/glossary/http-status-codes/
# 1xx - Hold On, something happening
# 2xx - Here you go, successful
# 3xx - Go Away, you don't have permission
# 4xx - (Client) You screwed up
# 5xx - Host Server screwed you

# Error Handling, Generic:
# if response.status_code != 200:
#     raise Exception("Bad response from API")

# Specific Error handling:
# if response.status_code == 404:
#     raise Exception("The resource doesn't exist")  # When exception is raised, the code breaks at that point.
# elif response.status_code == 401:
#     raise Exception("Not authorised to access this.")

response.raise_for_status()  # If there is error, it catches and prints it.

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
position = (float(longitude), float(latitude))
print(position)  # Show on Map: https://www.latlong.net/Show-Latitude-Longitude.html

# API Params: Input when making an api requests. Eg: https://sunrise-sunset.org/api
# params sent in dict format
params = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,  # Can leave ',' in the end
    # "tzid": "Asia/Kolkata"  # Indian timezone, got from docs
    "formatted": 0  # To get in 24 Hours clock
}
sunrise_and_sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
# This is equivalent to below url, note params is not the data sent during post and put.
# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400 # lat, lng are required params and others optional,
# this can be seen in api docs.
sunrise_and_sunset_response.raise_for_status()
# print(sunrise_and_sunset_response.json())

sunrise = sunrise_and_sunset_response.json()["results"]["sunrise"]  # The values are relative to utc time
sunset = sunrise_and_sunset_response.json()["results"]["sunset"]

print(sunrise, sunset)  # 2024-05-11T13:13:59+00:00 - date: 2024-05-11 , Time: 13:13:59, UTC: +00:00

current_time = dt.datetime.now()

print(current_time)  # 2024-05-12 01:38:42.312524, Time : 01:38:42.312524


hour_part_for_sunrise = int(sunrise.split("T")[1].split(":")[0])
hour_part_for_current_time = current_time.hour
print(hour_part_for_sunrise, hour_part_for_current_time)