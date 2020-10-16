import sqlite3 as lite
import sys
con = lite.connect('sensorsData.db')
with con:
    cur = con.cursor()
    cur.execute("INSERT INTO temper_data VALUES(datetime('now'), 20.5)")
    cur.execute("INSERT INTO temper_data VALUES(datetime('now'), 25.8)")
    cur.execute("INSERT INTO temper_data VALUES(datetime('now'), 30.3)")

print("\nEntire database content:\n")
for row in cur.execute("SELECT * FROM temper_data"):
    print(row)
    
con.close()