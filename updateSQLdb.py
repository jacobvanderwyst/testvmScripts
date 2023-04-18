#!/usr/bin/env python3

import mysql.connector

dbConnect=mysql.connector.connect(
    host='localhost', port='3306', user='root', password=''
)

print(dbConnect)