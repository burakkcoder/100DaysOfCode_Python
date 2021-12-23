from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "pythondaysofcode"
PASSWORD = "0"

chrome_driver_path = Service("C:\chromedriver.exe")

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")

        time.sleep(3)

        username_area = self.driver.find_element_by_name("username")
        username_area.send_keys(USERNAME)

        password_area = self.driver.find_element_by_name("password")
        password_area.send_keys(PASSWORD)
        password_area.send_keys(Keys.ENTER)

        time.sleep(3)

        not_now_button = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button")
        not_now_button.click()

        time.sleep(3)

        not_now_button2 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        not_now_button2.click()

    def find_followers(self):
        search_area = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search_area.send_keys("Instagram")
        time.sleep(2)
        search_area.send_keys(Keys.ENTER)
        time.sleep(2)
        search_area.send_keys(Keys.ENTER)

        time.sleep(3)

        following = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
        following.click()

        time.sleep(3)

        modal = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]')
        for i in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        count = 0
        for button in all_buttons:
            button.click()
            time.sleep(2)
            count += 1
            if count == 15:
                break

bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
