from smtplib import *
from datetime import *
import pandas as pd
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
PASSWORD = "abcd1234()"
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.


# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter.
today = datetime.now()
today_tuple = (today.month, today.day)

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#

birthdays = pd.read_csv("./birthdays.csv")

birthday_dict = {
    (data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays.iterrows()
}


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as letter:
        message = letter.read()
        wish = message.replace("[NAME]", birthday_person["name"])
    with SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday dear\n\n{wish}")
