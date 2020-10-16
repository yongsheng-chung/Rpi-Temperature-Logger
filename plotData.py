import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

def graph_data():
    # Connect to database
    sqlite_file = 'sensorsData.db'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('SELECT timestamp, temp FROM temper_data')
    data = c.fetchall()
    
    # data[*][0] = temperature
    # data[*][1] = humidity
    # data[*][2] = feelslike
    # data[*][3] = timenow
    
    time = []
    temperature = []

    for row in data:
        time.append(parser.parse(row[0]))
        temperature.append(row[1])

    # Convert datetime to float days
    dates = [mdates.date2num(t) for t in time]
    
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.set_title("My temperature data")
    
    # Configure x-ticks
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y %H:%M'))
    
    # Plot temperature data on left Y axis
    ax1.set_ylabel("Temperature [C]")
    ax1.plot_date(dates, temperature, '-', label="Temperature", color='r')
    
    # Format the x-axis for dates (label formatting, rotation)
    fig.autofmt_xdate(rotation=60)
    fig.tight_layout()

    # Show grids and legends
    ax1.grid(True)
    ax1.legend(loc='best', framealpha=0.5)

    plt.savefig("figure.png")
   
def main():
    graph_data()
    
main()
