import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = "h2814313@gmail.com"
PASSWORD = "h1a2r3s4h5"

now = dt.datetime.now()
today = (now.day, now.month)

data = pandas.read_csv("birthdays.csv", usecols=["month", "day"])
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{content}" )