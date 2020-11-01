from datetime import datetime
from flask import Flask, render_template, request
import pandas as pd
import sqlite3
import os

app = Flask(__name__)
database = '../sensorsData.db'

def maxRowsTable():
    conn = sqlite3.connect('../sensorsData.db')
    curs = conn.cursor()
    for row in curs.execute("SELECT COUNT(temp) FROM temper_data"):
        maxNumberRows = row[0]
    conn.close()
    return maxNumberRows

# Retrieve latest data from database
def getLastData():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    for row in curs.execute("SELECT * FROM temper_data ORDER BY timestamp DESC LIMIT 1"):
        time = str(row[0])
        temp = row[1]
    conn.close()
    return time, temp

# Retrieve a range of data
def getHistData():
    conn = sqlite3.connect(database)
    curs = conn.cursor()
    count = 0
    timeTemp = []
    # for row in curs.execute("SELECT * FROM temper_data ORDER BY timestamp DESC LIMIT " + str(numSamples)):
    for row in curs.execute("SELECT * FROM temper_data ORDER BY timestamp DESC LIMIT 144"):
        timeTemp.append([row[0].format('YYYY-MM-DD HH:mm'), round(row[1], 2)])
        count += 1
    conn.close()
    print(type(timeTemp))
    return timeTemp, count

# Retrieve a range of data using pandas
def getData():
    conn = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * FROM temper_data ORDER BY timestamp DESC LIMIT 144", conn)
    conn.close()

    timestamp = df['timestamp'].values.tolist()
    temperatures = df['temp'].values.tolist()
    print(type(timestamp))
    print(type(temperatures))

    return timestamp, temperatures

# main route
@app.route("/")
def index():
    time, temp = getLastData()
    templateData = {
        'time': time,
        'temp': temp,
    }
    return render_template("index.html", **templateData)

# Historical data plotted google charts
@app.route("/googleCharts")
def graph_google():
    timeTemp, count = getHistData()
    return render_template("googleCharts.html", temp = timeTemp, temp_items = count)

# Historical data plotted using Chartjs
@app.route("/chartjs")
def graph_chartjs():
    timestamp, temperatures = getData()
    return render_template("chartjs.html", timestamp = timestamp, temperatures = temperatures)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

