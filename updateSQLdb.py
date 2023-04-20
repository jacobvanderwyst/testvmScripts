#!/usr/bin/env python3

import mysql.connector
import time

dbConnect=mysql.connector.connect( 
    host='localhost', port='3306', user='root', password='', database='ranchersonly'
)
print(dbConnect)

mycursor = dbConnect.cursor()

while True:
    do=input("Enter Value: quit 0, add user 1, add rancher 2, add staff 3, add relationship 4\n$ ")
    if do =='0':
        break
    elif do =='1':
        args=input("Comma separated list, [email, password, username]\nUsers: ")
        args=args.split(',')
        mycursor.execute(f'insert into users(email, password, username) values (\'{args[0]}\',\'{args[1]}\',\'{args[2]}\')')
        
        mycursor.execute(f'insert into staff(uId,uname) values ((select uId from users where users.username={args[2]})\'{args[2]}\'')
    elif do =='2':
        args=input("Comma separated list, [age, gender, name]\nRancher: ")
        args=args.split(',')
        mycursor.execute(f'insert into ranchers(age, gender, name) values (\'{args[0]}\',\'{args[1]}\',\'{args[2]}\')')
    elif do =='3':
        args=input("Comma separated list, [username, role]\nstaff: ")
        mycursor.execute(f'select staff from staff where uname=\'{args[0]}\';update staff set staff=\'{args[1]}\'')
    elif do =='4':
        mycursor.execute()

print("Exiting...")
time.sleep(1)
