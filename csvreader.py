import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import numpy as np

x= []
y =[]
month_name = ""

with open('games.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 

    header = next(plots)
    data = list(plots)
    data.reverse()
    count = 0

    for row in data:
        month = int(row[1])
        year = int(row[0])

        date_time_value = mdates.date2num(date(year,month,1))
        date_time_num = mdates.date2num(date_time_value)
        formatter = mdates.ConciseDateFormatter(date_time_value)

        x.append(date_time_value)
        y.append(int(row[2]))

x0 = np.array(x)
y0 = np.array(y)

coefficients = np.polyfit(x0, y0, 1)
function = np.poly1d(coefficients)
trend_line = function(x0)
         
plt.figure(figsize=(12, 8))   
plt.scatter(x, y, color='g', label='Games')
plt.plot(x, trend_line, linestyle='--', color='g', label='Trend Line')
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) 
plt.xlabel('Month') 
plt.ylabel('Games') 
plt.title('Number of games per month') 
plt.legend()
plt.tight_layout()

plt.savefig('games_per_month.png', format='png')
plt.show() 

    