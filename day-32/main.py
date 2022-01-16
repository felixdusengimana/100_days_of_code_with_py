import smtplib

my_email = "phelixdusengimana@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="phelixdusengimana@yahoo.com",
        msg="Subject:Hello\n\n This is the body of my emal")
