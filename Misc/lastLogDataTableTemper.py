import sqlite3
conn = sqlite3.connect('sensorsData.db')
curs=conn.cursor()

print ("\nLast Data logged on database:\n")
for row in curs.execute("SELECT * FROM temper_data ORDER BY timestamp DESC LIMIT 1"):
    print (row)