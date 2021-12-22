from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

TWITTER_USERNAME = "0"
TWITTER_PASSWORD = "0"

chrome_driver_path = Service("C:\chromedriver.exe")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://fast.com/tr/")
        time.sleep(30)
        for_upload = self.driver.find_element_by_id("show-more-details-link")
        for_upload.click()
        time.sleep(30)
        self.down = self.driver.find_element_by_id("speed-value").text
        self.up = self.driver.find_element_by_id("upload-value").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        username_area = self.driver.find_element_by_tag_name("input")
        username_area.send_keys(TWITTER_USERNAME)
        username_area.send_keys(Keys.ENTER)

        time.sleep(5)

        password_area = self.driver.find_element_by_name("password")
        password_area.send_keys(TWITTER_PASSWORD)
        password_area.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet_area = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet_area.send_keys(f"#100DaysOfCode\n#Python\nDay 51\nTwitter Bot\nThis tweet shows my internet speed ({self.down}down / {self.up}up) and was sent from my twitter bot.")

        tweet_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
        tweet_button.click()

bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()
