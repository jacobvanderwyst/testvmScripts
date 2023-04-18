#!/usr/bin/env python3

import mysql.connector

dbConnect=mysql.connector.connect(
    host='localhost', port='3306', user='root', password=''
)

print(dbConnect)

mycursor = dbConnect.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)