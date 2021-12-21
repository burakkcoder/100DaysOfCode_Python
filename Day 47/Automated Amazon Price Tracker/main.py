import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "burakkcode@gmail.com"
my_pass = "0"

url = "https://www.amazon.com.tr/Bosch-EasyDrill-Vidalama-Makinesi-Entegre/dp/B01LXR2JKU/ref=sr_1_3?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=bosch+vidalama&qid=1640082216&s=home-improvement&sr=1-3"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_discount = float(price.split("TL")[0].replace(",", "."))
print(price_without_discount)

if price_without_discount < 788.20:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(my_email, my_pass)
    connection.sendmail(from_addr=my_email, to_addrs="mail@gmail.com",
                        msg=f"Subject:Amazon Fiyat Alarmı!\nBosch Akülü Vidalama {price}'nin altına düştü. Hemen Al!".encode("utf-8"))

