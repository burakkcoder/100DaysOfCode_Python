from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

chrome_driver_path = Service("C:\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)

majors = []
early_career_pay = []
mid_career_pay = []
page = 1
while page < 35:
    driver.get(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{page}")
    time.sleep(3)
    for x in range(1, 26):
        print(x)
        if page == 34:
            majors.append(driver.find_element_by_xpath(
                "//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[1]/td[2]/span[2]").text)
            majors.append(driver.find_element_by_xpath(
                "//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[2]/td[2]/span[2]").text)
            early_career_pay.append(driver.find_element_by_xpath(
                "//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[1]/td[4]/span[2]").text)
            early_career_pay.append(driver.find_element_by_xpath(
                "//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[2]/td[4]/span[2]").text)
            mid_career_pay.append(driver.find_element_by_xpath(
                "//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[1]/td[5]/span[2]").text)
            mid_career_pay.append(driver.find_element_by_xpath(
                "//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[2]/td[5]/span[2]").text)
        else:
            majors.append(driver.find_element_by_xpath(
                f"//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[{x}]/td[2]/span[2]").text)
            early_career_pay.append(driver.find_element_by_xpath(
                f"//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[{x}]/td[4]/span[2]").text)
            mid_career_pay.append(driver.find_element_by_xpath(
                f"//*[@id='__next']/div/div[1]/article/div[2]/table/tbody/tr[{x}]/td[5]/span[2]").text)
    time.sleep(3)
    next_button = driver.find_element_by_class_name("pagination__next-btn")
    next_button.click()
    page += 1

data_dict = {
    "major": [],
    "early_career_pay": [],
    "mid_career_pay": []
}
for major in majors:
    data_dict["major"].append(major)
for pay in early_career_pay:
    data_dict["early_career_pay"].append(pay)
for pay in mid_career_pay:
    data_dict["mid_career_pay"].append(pay)

df = pd.DataFrame(data_dict)
df.to_csv("highest_paying_jobs.csv")

highest_pays = df.sort_values("mid_career_pay", ascending=False)
print(highest_pays.head())
