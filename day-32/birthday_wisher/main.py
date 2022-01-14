import datetime as dt
import random
import smtplib

import pandas

today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row.month, data_row.day): data_row for (index,data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="", password="")
        connection.sendmail(
            from_addr="",
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy birthday\n\n{contents}")
# 4. Send the letter generated in step 3 to that person's email address.
