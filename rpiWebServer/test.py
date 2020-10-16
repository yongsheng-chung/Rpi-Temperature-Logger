from datetime import datetime
from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
database = os.path.abspath('sensorsData.db')
print(database)

# Retrieve a range of data
def getHistData():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    # for row in curs.execute("SELECT * FROM temper_data ORDER BY timestamp DESC LIMIT " + str(numSamples)):
    curs.execute("SELECT * FROM temper_data")
    temperatures = curs.fetchall()
    conn.close()
    return temperatures

def tabulate():
    temperatures = getHistData()
    count = 0
    timeTemp = []
    print(type(temperatures))
    for record in temperatures:
        
        timeTemp.append([record[0], record[1]])
        count += 1
    return timeTemp, count

def connect_test():
    con = sqlite3.connect(database)
    curs = con.cursor()
    for row in curs.execute(".table"):
        print(row)

# Historical data plotted as graph
def graph():
    timeTemp, count = getHistData()
    return render_template("historic.html", temp = timeTemp, temp_items = count)

# timeTemp, count = tabulate()
connect_test()
print("Count: ", count)

