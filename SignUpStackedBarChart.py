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

        months = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
        }

        month_num = months[month]

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

    