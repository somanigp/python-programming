from smtplib import SMTP
import datetime as dt
from random import choice

MY_EMAIL = "govindsomaniact@gmail.com"
GMAIL_SMTP_SERVER = "smtp.gmail.com"
PASSWORD = "uxmhhrbzyewbnzkd"

# Getting current date:
current_date = dt.datetime.now()
week_day = 0  # For Monday

# Getting a random quote:
with open("birthday_wisher/quotes.txt", mode="r") as data_file:
    # data_file.readlines()  # The readlines() method returns a list containing each line in the file as a list item.
    random_quote = choice(data_file.readlines()).strip()  # Removing extra spaces and newline.
    message = f"Subject:Motivational Quote\n\n{random_quote}"  # This is a global scope for this file.


# Main Logic
def main():
    if current_date.weekday() == week_day:
        with SMTP(GMAIL_SMTP_SERVER) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=message)  # Send mail to yourself


if __name__ == "__main__":  # Note it execute the file in logical order, the lines inside this particular if block
    # is only executed if name = main. meaning line 1-19 are executed even before this if block
    main()
