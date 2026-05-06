from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(practice_url)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-price-whole").get_text()

# price_without_currency = price.split("$")[1]

price_as_float = float(price.replace(",", "").replace("$", ""))
print(price_as_float)

# =============== Send an Email ===============

title = soup.find(id="productTitle").get_text()
print(title)

MY_EMAIL = "singhanamika5647@gmail.com" 
MY_PASSWORD = "owpywxwwvwqugzyf"

BUY_PRICE = 100.00

if price_as_float < BUY_PRICE:
    message = f"{title} is now on sale for {price}!"

    # ============== Use Environment Variables ===============

    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["MY_EMAIL"], os.environ["MY_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["MY_EMAIL"],
            to_addrs=os.environ["MY_EMAIL"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{practice_url}".encode("utf-8")
        )



