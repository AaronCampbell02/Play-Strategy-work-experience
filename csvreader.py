import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date

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
        formatter = mdates.ConciseDateFormatter(date_time_value)

        x.append(date_time_value)
        y.append(int(row[2]))
         

         
plt.figure(figsize=(12, 8))   
plt.plot(x, y, color = 'g',linestyle = 'dashed', 
         marker = 'o', label = "Games")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) 
plt.xlabel('Month') 
plt.ylabel('Games') 
plt.title('Number of games per month') 
plt.legend()
plt.tight_layout()

plt.savefig('games_per_month.png', format='png')
plt.show() 

    