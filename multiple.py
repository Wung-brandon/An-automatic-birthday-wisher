from datetime import datetime
import pandas as pd
from random import randint
from smtplib import SMTP

today = datetime.now()
today_tuple = (today.month, today.day)

birthdays = pd.read_csv('birthdays.csv')

MY_EMAIL = "wungbrandon27@gmail.com"
PASSWORD = "ojjgysecxfloxyev"

birthday_list = [(data_row["month"], data_row["day"], data_row) for (_, data_row) in birthdays.iterrows()]

matching_birthdays = [birthday_person for (month, day, birthday_person) in birthday_list if (month, day) == today_tuple]

if matching_birthdays:
    for birthday_person in matching_birthdays:
        file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            content = letter_file.read()
            content_name = content.replace("[NAME]", birthday_person["name"])
            #print(content_name)

        try:
            with SMTP("smtp.gmail.com", 587, timeout=10) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=birthday_person["email"],
                                    msg=f"Subject: Happy birthday!\n\n{content_name}")
            print("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred while sending the email: {str(e)}")
else:
    print("No birthdays today.")