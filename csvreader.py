import csv
import matplotlib.pyplot as plt

x= []
y =[]

with open('games.csv','r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 

    header = next(plots)

    for row in plots:
        x.append(row[1]) 
        y.append(int(row[2])) 
  
plt.bar(x, y, color = 'g', width = 0.72, label = "Games") 
plt.xlabel('Month') 
plt.ylabel('Games') 
plt.title('Number of games per month') 
plt.legend() 
plt.show() 

    