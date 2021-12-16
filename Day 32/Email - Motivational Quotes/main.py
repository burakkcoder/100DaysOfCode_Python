import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
    with open("quotes.txt") as file:
        quotes_list = file.readlines()
random_quotes = random.choice(quotes_list)

my_email = "burakkcode@gmail.com"
password = "123456"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mail@gmail.com",
                        msg=f"Subject:Quote\n\n{random_quotes}")


