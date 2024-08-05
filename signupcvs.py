import csv
import matplotlib.pyplot as plt

x= []
y =[]

with open('users.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 

    header = next(plots)
    data = list(plots)

    for row in data:
        month = row[1]
        year = row[0]
        date = month + str(year)

        x.append(date)
        y.append(int(row[2]))
         
plt.figure(figsize=(12, 8))   
plt.plot(x, y, color = 'g',linestyle = 'dashed', 
         marker = 'o', label = "User Sign ups") 
plt.xlabel('Month') 
plt.ylabel('User Sign ups') 
plt.title('Number of User Sign ups') 
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('sign_ups_per_month.png', format='png')
plt.show() 

    