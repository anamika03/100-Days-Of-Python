import smtplib
import datetime as dt
import random

MY_EMAIL = "singhanamika5647@gmail.com" 
MY_PASSWORD = "owpywxwwvwqugzyf"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:  # Friday is represented by 4
    with open("/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls() 
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL, 
        to_addrs=MY_EMAIL, 
        msg=f"Subject:Monday Motivation\n\n{quote}"
    )
print("Email sent successfully!")
