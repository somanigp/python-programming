# Email SMTP: Module pre bundled with python - smtplib
# datetime: Whats today's date is, or how to format the date/time.

# 1. Make sure you've got the correct smtp address for your email provider:
# Gmail: smtp.gmail.com
# Hotmail: smtp.live.com
# Outlook: outlook.office365.com
# Yahoo: smtp.mail.yahoo.com

# 3. Click on 2-Step Verification again, and scroll to the bottom.
# There you can add an App password. Select Other from the dropdown list and enter an app name, e.g. Python Mail,
# then click Generate.
# COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.
# Use this App password in your Python code instead of your normal password.

# 4. Add a port number by changing your code to this:
# smtplib.SMTP("smtp.gmail.com", port=587)

# Python Mail: uxmhhrbzyewbnzkd
# My Mail -> Google Mail Server -> Yahoo Mail Server -> Yahoo Recipient Mail using SMTP (Simple Mail Transfer Protocol)
import smtplib
import datetime as dt

password = "uxmhhrbzyewbnzkd"
my_email = "govindsomaniact@gmail.com"  # govindsomaniact - identity of my account,
# gmail.com - identity of my email provider
# Both below messages work.
message: str = "Subject:Hello\n\nThis is the body of my mail"  # 2 newlines needed between subject and body
second_message = '''Subject:Hello

Hi Govind,
Just testing this..

Thanks,
Govind'''

# connection = smtplib.SMTP("smtp.gmail.com")
#
# connection.starttls()   # secure connection. # tls - Transport layer security (like ssl, but newer),
# # way of securing our connection to email server. When we are sending email, it encrypts the message and secures it.
# connection.login(user=my_email, password=password)
# # connection.sendmail(from_addr=my_email, to_addrs="govindsomaniofc@gmail.com", msg="Hello, Just Testing")
# connection.sendmail(from_addr=my_email, to_addrs="govindsomaniofc@gmail.com", msg=second_message)
# connection.close()  # Just like files, we close the connection.

with smtplib.SMTP("smtp.gmail.com") as connection:  # Closes after using smtplib.SMTP("smtp.gmail.com") object
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="govindsomaniofc@gmail.com", msg=second_message)

# DateTime Module
current_date_time = dt.datetime.now()  # Class method that returns datetime object.
# Inside dt there is a class datetime, note now is a function that can be
# called on the class and it gives back a datetime object.
print(current_date_time)
print(type(current_date_time))  # <class 'datetime.datetime'>

# @classmethod
#     def now(cls, tz=None):
#         "Construct a datetime from time.time() and optional time zone info."
#         t = _time.time()
#         return cls.fromtimestamp(t, tz)  # How to call class methods.

print(current_date_time.year)  # Attributes of datetime class
print(current_date_time.month)
print(current_date_time.day)

print(current_date_time.weekday())  # Method of datetime class # 0 - Monday , 6 - Sunday

# Creating a datetime object
date = dt.datetime(year=1999, month=1, day=12)  # hour: SupportsIndex = ..., . here ... means they have a default value
print(date)
second_date = dt.datetime(year=1999, month=1, day=12,hour=6)
print(second_date)
