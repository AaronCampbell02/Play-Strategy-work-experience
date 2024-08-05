import csv
import matplotlib.pyplot as plt

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
        print(month)
        year = row[0]
        if month == 1:
            month_name = "January"
        elif month == 2:
            month_name = "February"
        elif month == 3:
            month_name = "March"
        elif month == 4:
            month_name = "April"
        elif month == 5:
            month_name = "May"
        elif month == 6:
            month_name = "June"
        elif month == 7:
            month_name = "July"
        elif month == 8:
            month_name = "August"
        elif month == 9:
            month_name = "September"
        elif month == 10:
            month_name = "October"
        elif month == 11:
            month_name = "November"
        elif month == 12:
            month_name = "December"

        date = month_name + str(year)
        x.append(date)
        y.append(int(row[2]))
         
plt.figure(figsize=(12, 6))   
plt.plot(x, y, color = 'g',linestyle = 'dashed', 
         marker = 'o', label = "Games") 
plt.xlabel('Month') 
plt.ylabel('Games') 
plt.title('Number of games per month') 
plt.legend()
plt.xticks(rotation=45, ha='right')

plt.savefig('games_per_month.png', format='png')
plt.show() 

    