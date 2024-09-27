import pandas as pd
import smtplib
import datetime as dt

MY_EMAIL = "asgarrifadzulfikar@gmail.com"
MY_PASSWORD = "kyqs dpen lrpo zhif"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")

# Convert the 'birthdate' column to datetime
birthdays_df['birthdate'] = pd.to_datetime(birthdays_df[['year', 'month', 'day']])

print(birthdays_df)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.