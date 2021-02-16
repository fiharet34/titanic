import csv
import sqlite3

from sqlite3 import Error
def sql_connection():

    try:
        con = sqlite3.connect('titanic.db')
        return con

    except Error:
        print(Error)

def sql_table(con):
    cursorObj = con.cursor()
    
    cursorObj.execute("CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text, age int, alive text, work text)")

    con.commit()
    
con = sql_connection()
sql_table(con)

with open('titanic.csv') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        print(line)