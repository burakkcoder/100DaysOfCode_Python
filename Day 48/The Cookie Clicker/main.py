from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
half_min = time.time() + 30

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        upgrades = {}
        for x in range(len(item_prices)):
            upgrades[item_prices[x]] = item_ids[x]

        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        upgrades_price = {}
        for cost, id in upgrades.items():
            if cookie_count > cost:
                upgrades_price[cost] = id

        highest_price_upgrade = max(upgrades_price)
        purchase_id = upgrades_price[highest_price_upgrade]

        driver.find_element_by_id(purchase_id).click()

        timeout = time.time() + 5

    if time.time() > half_min:
        cookie_per_second = driver.find_element_by_id("cps").text
        print(cookie_per_second)
        break

time.sleep(5)
driver.quit()