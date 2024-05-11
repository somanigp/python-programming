import requests
from datetime import datetime
from smtplib import SMTP
import time

MY_GMAIL = "govindsomaniact@gmail.com"
MY_PASSWORD = "uxmhhrbzyewbnzkd"
GMAIL_SERVER = "smtp.gmail.com"
MESSAGE = "Subject:ISS OVERHEAD\n\nLook Up"


MY_LAT = 21.152451  # Your latitude
MY_LONG = 79.080559  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


# TODO: If the ISS is close to my current position and it is currently dark
def is_near(latitude: float, longitude: float) -> bool:
    if (latitude >= MY_LAT - 5) and (latitude <= MY_LAT + 5):
        if (MY_LONG-5) <= longitude <= (MY_LONG+5):
            return True
    return False


def is_visible() -> bool:
    return (time_now.hour <= sunrise) or (time_now.hour >= sunset)


message_sent = False
# TODO: BONUS: run the code every 60 seconds.
while not message_sent:
    if is_near(iss_latitude, iss_longitude) and is_visible():
        # TODO: Then send me an email to tell me to look up.
        with SMTP(GMAIL_SERVER) as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_GMAIL, to_addrs=MY_GMAIL, msg=MESSAGE)
        message_sent = True
    time.sleep(60)





