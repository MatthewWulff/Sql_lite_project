import sqlite3
# Create connection
conn = sqlite3.connect("first.db") 
#Create cursor
c = conn.cursor()

#Create Table
c.execute(""" CREATE TABLE customers(
          first_name TEXT,
          last_name TEXT,
          email TEXT,
          )""")


