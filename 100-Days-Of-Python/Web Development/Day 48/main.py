# Selenium automates browsers. That's it! 
# What you do with that power is entirely up to you. 
# Primarily, it is for automating web applications for testing purposes, 
# but is certainly not limited to just that. 
# Boring web-based administration tasks can also be automated as well.

from selenium import webdriver # Importing the webdriver module from the selenium package

# Keep the browser open after the script ends
chrome_options = webdriver.ChromeOptions() # Creating an instance of ChromeOptions to set options for the Chrome driver
chrome_options.add_experimental_option("detach", True) # Adding the detach argument to keep the browser open after the script ends

driver = webdriver.Chrome(options=chrome_options) # Creating a new instance of the Chrome driver
driver.get("https://www.amazon.de") # Navigating to the Google homepage

# driver.close() # Closes the current tab.
# driver.quit() # Quits the entire browser
