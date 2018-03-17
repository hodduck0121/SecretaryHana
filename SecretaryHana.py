# This is a personal secretary program whose name is Hana.

import datetime

def age(today, birth):
    today = datetime.date.today()
    age = datetime.timedelta.total_seconds(today - birth) / 365.2422 / 24 / 3600
    return age

def modify_userdata():
    with open("userdata.txt", 'w') as userdata:
        user = str(input("please enter your name. \n"))
        birth_raw = str(input("enter your birthday by 8 digits. \n"))
        print("User data has been successfully saved")
        userdata.write(user + '\n')
        userdata.write(birth_raw + '\n')

def dateinfo():
    print('Hello ' + user + ', today is ' + today.strftime('%A %d, %B %Y'))
    print('Your age is %.4f' % age(today, birth))

#read user information or require input data
try:
    with open("userdata.txt", 'r') as userdata:
        userdata_list = userdata.readlines()
        user = userdata_list[0][:-2]
        birth_raw = userdata_list[1][:-2]
except FileNotFoundError:
    modify_userdata()

#convert birth data to datetime.date object
birth = datetime.date(int(birth_raw[:4]), int(birth_raw[4:6]), int(birth_raw[6:]))
today = datetime.date.today()

menu = """


==============Select Menu===============
1. Reenter user data
2. What's my age?
========================================
"""
dateinfo()
while True:
    menu_sel = input(menu)
    if menu_sel == '1':
        modify_userdata()
        dateinfo()
    elif menu_sel == '2':
        dateinfo()