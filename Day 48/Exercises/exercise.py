from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for x in range(len(event_times)):
    events[x] = {
        "time": event_times[x].text,
        "name": event_names[x].text
    }

print(events)

driver.quit()