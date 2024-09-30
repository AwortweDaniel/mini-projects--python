from smtplib import *
from datetime import *
import random

# Send Motivational Quotes Today through Email
MY_EMAIL = "nanadanieljr@gmail.com"
PASSWORD = "rio_2014"
RECEIVER_EMAIL = "awortwedanieljr15@gmail.com"

dt = datetime(year=2024, month=7, day=1)
now = datetime.now()
today = now.weekday()
# print(dt.day)
print(today)
if today == dt.day:
    with open("./quotes.txt", "r") as quotes:
        content = quotes.readlines()
        contents = [c.strip("\n") for c in content]
        daily_message = random.choice(contents)

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL,
                            msg=f"Subject:Happy Wednesday\n\n{daily_message}")

# -----SMTP Try------------------------

# my_email = "awortwedanieljr15@gmail.com"
# password = "*****************"
#
# with SMTP("smtp.gmail.com") as connection:
#     # for starttls for securing connection
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addr="", msg="Subject:hello\n\nThis is the body of my e_mail")

# ------------DATE TIME Try---------------
# now = datetime.now()
# year = now.year
# month = now.month
# day = now.weekday()
# print(day)
#
# date_of_birth = datetime(year=2003, month=4, day=15)
# print(date_of_birth)
