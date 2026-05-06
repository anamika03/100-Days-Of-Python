# Selenium automates browsers. That's it! 
# What you do with that power is entirely up to you. 
# Primarily, it is for automating web applications for testing purposes, 
# but is certainly not limited to just that. 
# Boring web-based administration tasks can also be automated as well.

from selenium import webdriver # Importing the webdriver module from the selenium package
from selenium.webdriver.common.by import By



# Keep the browser open after the script ends
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=chrome_options) # Creating a new instance of the Chrome driver
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1") # Navigating to the Google homepage

price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_penny = driver.find_element(By.CLASS_NAME, value="a-price-fraction") 

print(f"The price of the item is: €{price_euro.text}.{price_penny.text}") # Printing the price of the item
# driver.close() # Closes the current tab.
driver.quit() # Quits the entire browser
