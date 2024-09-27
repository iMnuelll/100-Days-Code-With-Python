import smtplib
import datetime as dt
import pandas as pd
from random import randint

MY_EMAIL = "asgarrifadzulfikar@gmail.com"
MY_PASSWORD = "kyqs dpen lrpo zhif"

"""
SMTP CONNECTION
Gmail =  smpt.gmail.com
Hotmail = smtp.live.com
Yahoo = smtp.mail.yahoo.com
"""

current_time = dt.datetime.now()
current_day = current_time.strftime("%A")

if current_day == "Monday" :
  # Open the text file and read it into a list
  with open("quotes.txt", "r") as data_file:
      quotes_list = data_file.readlines()

  # Optionally, strip newline characters (\n) from each line
  quotes_list = [quote.strip() for quote in quotes_list]

  # Now 'quotes_list' contains the text lines as a list
  random_quote = quotes_list[randint(0, len(quotes_list))]

  with smtplib.SMTP("smtp.gmail.com") as connection :
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="imanueluneputty121103@gmail.com",
                        msg=f"Subject:{current_day} Motivation\n\n{random_quote}"
                      )