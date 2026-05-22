from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # FIXED: Added missing Keys import
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "rashikasingh191@gmail.com"
TWITTER_PASSWORD = "your_twitter_password"
TWITTER_USERNAME = "rashika191"  # ADDED: X often asks for your @username after email


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        # Wait for the test to complete
        time.sleep(60)
        
        self.up = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        
        print(f"Down: {self.down} Mbps / Up: {self.up} Mbps")

    def tweet_at_provider(self):
        # Open X/Twitter Login
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(5)  # Give the complex dynamic react app time to load

        # 1. Enter Email
        email_input = self.driver.find_element(By.CSS_SELECTOR, value="input[autocomplete='username']")
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(3)

        # 2. Handle Username Challenge (X does this heavily for bots)
        try:
            # If X asks "Enter your phone number or username", this catches it
            username_challenge = self.driver.find_element(By.CSS_SELECTOR, value="input[data-testid='ocfEnterTextTextInput']")
            username_challenge.send_keys(TWITTER_USERNAME)
            username_challenge.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            # If it didn't ask for username validation, safely move right along
            pass

        # 3. Enter Password
        password_input = self.driver.find_element(By.CSS_SELECTOR, value="input[name='password']")
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

        # 4. Find the Tweet / Post box
        # X uses draftjs editor elements. Finding it by its accessibility role is the most robust way.
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR, value="div[role='textbox'][data-testid='tweetTextarea_0']")
        
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        # 5. Click Post Button
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, value="button[data-testid='tweetButtonInline']")
        tweet_button.click()

        time.sleep(4)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
