# Imports
import datetime as dt
from smtplib import SMTP
import random
import pandas as pd

# Constants
PLACEHOLDER: str = "[NAME]"
MY_EMAIL: str = "govindsomaniact@gmail.com"
PASSWORD: str = "uxmhhrbzyewbnzkd"
GMAIL_SMTP_SERVER: str = "smtp.gmail.com"

# TODO:1. Getting current Date
current_date = dt.datetime.now()
current_day = current_date.day
current_month = current_date.month

# TODO:2. Check if today matches a birthday in the birthdays.csv
data_file = pd.read_csv("birthdays.csv")
# In pandas, we need to use | and & operators.
birthday_day = data_file.loc[(data_file["month"] == current_month) & (data_file["day"] == current_day)]
records = birthday_day.to_dict("records")  # Will be [] if no records
# if not empty: [{'name': 'Govind Somani', 'email': 'govindsomaniofc@gmail.com', 'year': 1999, 'month': 5, 'day': 11}]

# TODO:3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the
#  person's actual name from birthdays.csv
if len(records) != 0:
    for data in records:
        name = data.get("name")
        email = data.get("email")
        if name and email:  # Checks if None or Empty ***
            # Putting a bunch of files in a dict
            address_of_letters = ["letter_templates/letter_1.txt",
                                  "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
            with open(random.choice(address_of_letters)) as letter:
                message = "Subject:Happy BirthDay!!!\n\n" + letter.read().replace(PLACEHOLDER, name)
            # TODO:4. Send the letter generated in step 3 to that person's email address.
            with SMTP(GMAIL_SMTP_SERVER) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=message  # Emojis: Windows+v
                )


print("Executed")


