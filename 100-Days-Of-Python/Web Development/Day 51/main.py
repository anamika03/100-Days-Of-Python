from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "rashikasingh191@gmail.com"
TWITTER_PASSWORD = "your_twitter_password"


class InternetSpeedTwitterBot:
    def __init__(self):  # Removed the required driver_path argument here
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element(By.ID, value="_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        # Wait for the test to complete (usually takes around 40-60 seconds)
        time.sleep(60)
        
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        
        print(self.up)
        print(self.down)

    def tweet_at_provider(self):
        pass


# This will now run without throwing the TypeError
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()