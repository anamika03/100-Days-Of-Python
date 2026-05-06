from bs4 import BeautifulSoup
import requests

practice_url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(practice_url)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-price-whole").get_text()

# price_without_currency = price.split("$")[1]

price_as_float = float(price)
print(price_as_float)