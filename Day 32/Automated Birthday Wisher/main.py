from datetime import datetime
import pandas as pd
import random
import smtplib

today = datetime.now()
month_and_day = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if month_and_day in birthdays_dict:
    birthday_person = birthdays_dict[month_and_day]
    letter = f"letter_templates/letter_{random.randint(1, 3)}"
    with open(letter) as file:
        contents = file.read()
        contents.replace("[NAME]", birthday_person["name"])

my_email = "burakkcode@gmail.com"
password = "123456"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{contents}")
