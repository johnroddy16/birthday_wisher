#!/usr/bin/env python3 

import pandas as pd 
import smtplib 
import datetime as dt 
from random import choice 
import os 

# 1. Update the birthdays.csv  

# 2. Check if today matches a birthday in the birthdays.csv 

now = dt.datetime.now()
cur_month = now.month 
cur_day = now.day  

df = pd.read_csv('birthdays.csv')

matches = df[(df['month'] == cur_month) & (df['day'] == cur_day)] 

birthday_people = matches[['name', 'email']].values.tolist()

print(birthday_people) # [['John', 'johnroddy.16@gmail.com'], ['Labowski', 'johnroddy16@yahoo.com']]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

letter_folder = 'letter_templates'

letter_files = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

def generate_birthday_message(name):
    # choose at random a letter template:
    letter = choice(letter_files)
    
    # construct the path to the letter file:
    letter_path = os.path.join(letter_folder, letter)
    
    # read template content:
    with open(letter_path, 'r') as file:
        letter_content = file.read()
        
    # replace [NAME] with the person's name:
    person_message = letter_content.replace('[NAME]', name)
    
    return person_message 

# 4. Send the letter generated in step 3 to that person's email address.

def send_birthday_message(to_address, msg):
    # email and app password:
    email = 'nohtyp742@gmail.com'
    password = 'xddewbafczduzurt'
    
    # create the connection:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        # make the connection secure:
        connection.starttls()  
        # login to email:
        connection.login(user=email, password=password)
        # send the email: 
        connection.sendmail(from_addr=email, to_addrs=to_address, msg=f'subject:Happy Birthday!!!!\n\n{msg}')
        
    return True  
        
if birthday_people:
    for person in birthday_people:
        name = person[0]
        email = person[1]
        msg = generate_birthday_message(name)
        to_address = email 
        send_birthday_message(to_address, msg)
        
# cool little program! 