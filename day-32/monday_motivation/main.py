import smtplib
import datetime as dt
import random

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("mail.gmail.com") as connection:
        connection.starttls()
        connection.login(password="", user="")
        connection.sendmail(to_addrs="", from_addr="", msg="")



