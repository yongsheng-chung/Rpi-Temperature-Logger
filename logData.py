#!/usr/bin/python3

from flask import Flask, request, render_template
import sqlite3
import subprocess
import time

# Setup
dbname = 'sensorsData.db'
samplingInterval = 10 * 60

# Edit the number of hours to sample data
numOfHours = 24 * 5
totalTime = numOfHours * 60 * 60
count = totalTime / samplingInterval

def display_current_temp():

    timestamp, temperature = get_data()

    if temperature is not None:
        return render_template("lab_temp.html", temp=temperature)
    else:
        return render_template("no_sensor.html")

# Retrieve data from Temper1f sensor
def getData():
    output = subprocess.Popen('usb-thermometer-master/pcsensor',
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
    stdout, stderr = output.communicate()

    stdout_str = stdout.decode()

    parts = stdout_str.split(' ')
    date = parts[0].replace(r'/', '-')
    timestamp = date + ' ' + parts[1]
    temp_f = float(parts[3][0:5])
    temp_c = float(parts[4][0:5])
    
    if timestamp is not None and temp_c is not None:
        temp_c = round(temp_c, 1)
        print(timestamp + ' -- Temperature: ' + str(temp_c) + ' C')
        logData(timestamp, temp_c)
    else:
        print('No timestamp or no sensor data')

# Log sensor data on database
def logData(timestamp, temp):
    
    # Function to insert data
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute("INSERT INTO temper_data VALUES((?), (?))", (timestamp, temp))
    conn.commit()
    conn.close()

# Display sensor data from database
def displayData():
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    print("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM temper_data"):
        print(row)
    conn.close()

# Main program
def main():
    a = 0
    while a < count:
        getData()
        time.sleep(samplingInterval)
        a += 1
    
# Execute program
main()
