from configparser import ConfigParser
import requests
import datetime as dt
import pytz  # use the pytz library to handle timezones
import os

# Both Works to get env
# x = os.environ.get("API_DEMO")  # Using Environment Variables for cloud.
# print(os.environ["API_DEMO"]) # Using Environment Variables for cloud.

# Add a new/Edit an existing environment variable
# os.environ['GeeksForGeeks'] = 'www.geeksforgeeks.org'

# print(os.environ)  # Gives all environment variables
config = ConfigParser()
config.read(filenames='./.project_config')

# API_ID: str = config['workout-project']['API_ID_NUTRITIONIX']
# API_KEY: str = config['workout-project']['API_KEY_NUTRITIONIX']
# TOKEN_FOR_SHEETY: str = config['workout-project']['TOKEN_FOR_SHEETY']

# Edit/...->Run with params->create config file with environment variables for the current file
API_ID = os.environ.get("API_ID_NUTRITIONIX")
API_KEY = os.environ.get("API_KEY_NUTRITIONIX")
TOKEN_FOR_SHEETY = os.environ.get("TOKEN_FOR_SHEETY")


NUTRITIONIX_URL: str = "https://trackapi.nutritionix.com"  # Provides natural language for exercise and nutrients.
NL_EXERCISE_ENDPOINT: str = "/v2/natural/exercise"  # Natural Language for Exercise
URL_FOR_SHEETY: str = "https://api.sheety.co/a7f55382fa7c942135e9f4b377ea61ec/myWorkouts/tracker"
MY_HEIGHT_CM: float = 177.5
MY_WEIGHT_KG: float = float(input("What is weight in kg?"))
MY_AGE: int = 25
GENDER: str = "male"

headers_for_nutritionix: dict = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
# Bearer authentication (also known as token authentication) is an HTTP authentication scheme that involves security
# tokens. The name “Bearer authentication” basically means “give access to the bearer of this token.” The security
# token or “bearer token” is just a cryptic string
headers_for_sheety: dict = {
    "Authorization": f"Bearer {TOKEN_FOR_SHEETY}"  # Using Bearer as defined in API docs. This is generally for
    # token-based authorization
}

# Define the Indian timezone
india_tz = pytz.timezone('Asia/Kolkata')  # Return a datetime. tzinfo implementation for the given timezone
date = dt.datetime.now(tz=india_tz)  # Data as per our Timezone

# %I is used for the hour in 12-hour format (01 to 12).
# %p is used to display AM or PM.
current_time = date.strftime("%I:%M:%S %p")  # date.time() gives time in 24 hour clock
date_in_str = date.strftime("%d-%m-%Y")


def exercise_text(plain_text: str) -> list:
    body: dict = {
        "query": plain_text,
        "weight_kg": MY_WEIGHT_KG,
        "height_cm": MY_HEIGHT_CM,
        "age": MY_AGE,
        "gender": GENDER
    }
    response = requests.post(url=f"{NUTRITIONIX_URL}{NL_EXERCISE_ENDPOINT}", headers=headers_for_nutritionix, json=body)
    response.raise_for_status()
    result = response.json()["exercises"]  # list
    return result


is_on = True
while is_on:
    query = input("Tell me which exercise you did ? ")
    if query.lower() == "exit":
        print("Have a great day, Govind!!")
        is_on = False
    else:
        list_of_activities = exercise_text(query)
        for activity in list_of_activities:  # For every activity run the test cases.
            data: dict = {
                "tracker": {
                    "date": date_in_str,
                    "time": current_time,
                    "exercise": activity.get("name"),
                    "duration": str(activity.get("duration_min")),
                    "calories": activity.get("nf_calories")
                }
            }
            # print(data)
            response = requests.post(url=URL_FOR_SHEETY, headers=headers_for_sheety, json=data)
            response.raise_for_status()
            # result = response.json()
            # print(result)

# NOTE: "govind somani".title()  # Govind Somani. - Title Case
