from datetime import datetime
import pandas as pd
from random import randint
from smtplib import SMTP


today = datetime.now()
today_turple = (today.month, today.day)

birthdays = pd.read_csv('birthdays.csv')
#print(birthdays)
MY_EMAIL = "wungbrandon27@gmail.com"
PASSWORD = "ojjgysecxfloxyev"

birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in birthdays.iterrows()}

if today_turple in birthday_dict:
    birthday_person = birthday_dict[today_turple]
    #print(birthday_person)
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content_name = content.replace("[NAME]",birthday_person["name"])
        print(content_name)
    try:
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject:Happy birthday!\n\n {content_name}")
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred while sending the email: {str(e)}")