from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element_by_xpath("//*[@id='articlecount']/a[1]")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(2)

driver.quit()