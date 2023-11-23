import sqlite3 as sql

# from sqlite3 import connect

# use sqlite(sql) module to create and/pr connect to a database
dbCon = sql.connect('Software Bootcamp/Week 10/Pt9_10DB/dfe2.db')


# create a cursor variable and assign it to thte cursor method to ecexute sql satements
dbCursor = dbCon.cursor()

