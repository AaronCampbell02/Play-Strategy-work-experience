import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import numpy as np

x= []
y1 =[]
y2 = []
y3 = []
y4 = []

with open('users.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 

    header = next(plots)
    data = list(plots)
    data.reverse()
    count = 0
    month_num = 0

    for row in data:
        month = row[1]
        year = int(row[0])

        month = month.lstrip()

        if month == "January":
            month_num = 1
        elif month == "February":
            month_num = 2
        elif month == "March":
            month_num = 3
        elif month == "April":
            month_num = 4
        elif month == "May":
            month_num = 5
        elif month == "June":
            month_num = 6
        elif month == "July":
            month_num = 7
        elif month == "August":
            month_num = 8
        elif month == "September":
            month_num = 9
        elif month == "October":
            month_num = 10
        elif month == "November":
            month_num = 11
        elif month == "December":
            month_num = 12

        date_time_value = mdates.date2num(date(year,month_num,1))
        date_time_num = mdates.date2num(date_time_value)
        formatter = mdates.ConciseDateFormatter(date_time_value)

        x.append(date_time_value)
        y1.append(int(row[2]))
        y2.append(int(row[4]))
        y3.append(int(row[3]))
        y4.append(int(row[5]))
         
plt.figure(figsize=(12, 8))   
plt.bar(x, y1, color='b', width=30, label='Total User Sign ups')
plt.bar(x, y2, bottom=y1, color='g', width=30, label='Enabled User Sign ups')
plt.bar(x, y3, bottom=[i + j for i, j in zip(y1, y2)], color='r', width=30, label='Bad/Bot Sign ups')
plt.bar(x, y4, bottom=[i + j + k for i, j, k in zip(y1, y2, y3)], color='y', width=30, label='Active Users') 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) 
plt.xlabel('Month') 
plt.ylabel('User Sign ups') 
plt.title('User Base details') 
plt.legend()
plt.tight_layout()

plt.savefig('SignUpStackedBar.png', format='png')
plt.show() 

    