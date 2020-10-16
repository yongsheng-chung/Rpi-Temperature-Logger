import sqlite3 as lite
import sys
con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS temper_data")
    cur.execute("CREATE TABLE temper_data (timestamp DATETIME, temp NUMERIC)")
