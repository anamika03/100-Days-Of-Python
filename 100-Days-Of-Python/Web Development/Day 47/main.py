from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Practice
<<<<<<< HEAD
<<<<<<< HEAD
# url = "https://appbrewery.github.io/instant_pot/"

# Live Site
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
=======
url = "https://appbrewery.github.io/instant_pot/"
# Live Site
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
>>>>>>> a8db2f3 (day 47 completed)
=======
url = "https://appbrewery.github.io/instant_pot/"
# Live Site
# url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
>>>>>>> refs/remotes/origin/day48

# ====================== Add Headers to the Request ===========================

# Full headers would look something like this
<<<<<<< HEAD
<<<<<<< HEAD
# header = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br, zstd",
#     "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
#     "Dnt": "1",
#     "Priority": "u=1",
#     "Sec-Fetch-Dest": "document",
#     "Sec-Fetch-Mode": "navigate",
#     "Sec-Fetch-Site": "none",
#     "Sec-Fetch-User": "?1",
#     "Sec-Gpc": "1",
#     "Upgrade-Insecure-Requests": "1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
# }

# A minimal header would look like this:
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
=======
=======
>>>>>>> refs/remotes/origin/day48
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
<<<<<<< HEAD
>>>>>>> a8db2f3 (day 47 completed)
=======
>>>>>>> refs/remotes/origin/day48

# Adding headers to the request
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")
# Check you are getting the actual Amazon page back and not something else:
<<<<<<< HEAD
<<<<<<< HEAD
print(soup.prettify())
=======
# print(soup.prettify())
>>>>>>> a8db2f3 (day 47 completed)
=======
# print(soup.prettify())
>>>>>>> refs/remotes/origin/day48

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

<<<<<<< HEAD
<<<<<<< HEAD
# Remove the euro sign using split
price_without_currency = price.split("EUR")[1]
=======
# Remove the dollar sign using split
price_without_currency = price.split("$")[1]
>>>>>>> a8db2f3 (day 47 completed)
=======
# Remove the dollar sign using split
price_without_currency = price.split("$")[1]
>>>>>>> refs/remotes/origin/day48

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
<<<<<<< HEAD
<<<<<<< HEAD
BUY_PRICE = 95
=======
BUY_PRICE = 70
>>>>>>> a8db2f3 (day 47 completed)
=======
BUY_PRICE = 70
>>>>>>> refs/remotes/origin/day48

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

<<<<<<< HEAD
<<<<<<< HEAD
    # ============== Use Environment Variables ===============

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )



=======
=======
>>>>>>> refs/remotes/origin/day48
    # ====================== Send the email ===========================

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
<<<<<<< HEAD
        )
>>>>>>> a8db2f3 (day 47 completed)
=======
        )
>>>>>>> refs/remotes/origin/day48
