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
        mycursor.execute()
    elif do =='2':
        mycursor.execute()
    elif do =='3':
        mycursor.execute()
    elif do =='4':
        mycursor.execute()

print("Exiting...")
time.sleep(1)
