from random import random
import smtplib

my_email = "singhanamika5647@gmail.com" #for yahoo use "smtp.mail.yahoo.com"
password = "owpywxwwvwqugzyf"
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

# import datetime as dt

# now = dt.datetime.now()
# print(now)
# day_of_week = now.weekday()
# print(day_of_week)  #0 is Monday and 6 is Sunday
# # print(now.year)   #data type is 'int'
# # print(now.month)
# # print(now.day)

# date_of_birth = dt.datetime(year=1996, month=6, day=3)
# print(date_of_birth)





# #TLS stands for Transport Layer Security. 
# # It is a cryptographic protocol that provides secure communication over a computer network. 
# # When you use TLS, the data sent between your email client and the email server is encrypted,
# # making it more difficult for unauthorized parties to intercept and read the information. 
# # This helps protect your email credentials and the content of your emails from being accessed by malicious actors.


              