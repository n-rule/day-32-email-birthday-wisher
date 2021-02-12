import smtplib
import datetime as dt
from random import randint
from pandas import *

my_email = 'ffdeimos2ua@gmail.com'
password = ''

now = dt.datetime.now()
today_date = (now.day, now.month)

data = read_csv('birthdays.csv')

# Example of dictionary comprehension
# birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

for row in data.iterrows():
    birthday = (row[1]['day'], row[1]['month'])

    if today_date == birthday:
        email_birthday = row[1]['email']
        name_birthday = row[1]['name']

        with open(f'letter_templates/letter_{randint(1, 3)}.txt') as letter:
            message = letter.read().replace('[NAME]', name_birthday)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(my_email, email_birthday, message)
