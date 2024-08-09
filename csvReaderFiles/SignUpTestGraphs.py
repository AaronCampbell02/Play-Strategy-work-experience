import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date
import numpy as np

x = []
y1 = []
y2 = []
y3 = []
y4 = []

colors = ['r', 'b', 'g', 'y']

with open('users.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    header = next(plots)

    for row in plots:
        month = row[1].strip()
        year = int(row[0])

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
        y1.append(int(row[3]))
        y2.append(int(row[5]))
        y3.append(int(row[4]))

x = np.array(x)
y1 = np.array(y1)
y2 = np.array(y2)
y3 = np.array(y3)

y1_cumsum = y1
y2_cumsum = y1_cumsum + y2
y3_cumsum = y2_cumsum + (y3-y2)


plt.figure(figsize=(14, 7))

plt.fill_between(x, 0, y1_cumsum, color='r', alpha=0.5, label='Bots')
plt.fill_between(x, y1_cumsum, y2_cumsum, color='g', alpha=0.5, label='Users with games')
plt.fill_between(x, y2_cumsum, y3_cumsum, color='b', alpha=0.5, label='Users with no games')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) 

plt.title('Sign Ups Per Month')
plt.xlabel('Date')
plt.ylabel('Sign Ups')
plt.legend()
plt.tight_layout()

plt.savefig('SignUpTestGraphs.png', format='png')
#plt.show()
