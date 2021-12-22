from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element_by_xpath("//*[@id='articlecount']/a[1]")
print(articles.text)

driver.quit()