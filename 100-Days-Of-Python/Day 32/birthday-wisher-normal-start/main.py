import datetime as dt
import pandas as pd
import random
import smtplib
import os


# MY_EMAIL = "singhanamika5647@gmail.com" 
# MY_PASSWORD = "owpywxwwvwqugzyf"

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.pandas.read_csv("/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 32/birthday-wisher-normal-start/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 32/birthday-wisher-normal-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )

3

