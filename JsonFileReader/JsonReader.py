import json
from datetime import datetime
import matplotlib.pyplot as plt

status_array = [
    ["Created", 10],
    ["Started", 20],
    ["Aborted", 25],
    ["Mate", 30],
    ["Resign", 31],
    ["Stalemate", 32],
    ["Timeout", 33],
    ["Draw", 34],
    ["Outoftime", 35],
    ["Cheat", 36],
    ["NoStart", 37],
    ["UnknownFinish", 38],
    ["PerpetualCheck", 39],
    ["SingleWin", 40],
    ["GammonWin", 41],
    ["BackgammonWin", 42],
    ["ResignGammon", 43],
    ["ResignBackgammon", 44],
    ["RuleOfGin", 45],
    ["GinGammon", 46],
    ["GinBackgammon", 47],
    ["OutoftimeGammon", 48],
    ["OutoftimeBackgammon", 49],
    ["VariantEnd", 60]
]

x = [0]*len(status_array) 

with open('games_dev_2024_08_01.json', 'r') as file:
    data = json.load(file)


    for item in data:
        try:
            s = item['s']
            for i in range(len(status_array)):
                if int(s) == int(status_array[i][1]):
                    x[i] += 1
            


        except:
            print("Invalid data entry")

names = [status_array[i][0] for i in range(7)]
values = [x[i] for i in range(7)]
plt.figure(figsize=(12, 8))
plt.bar(names, values, color = 'g', width = 0.5, label = "Ways to end the game")
plt.xlabel('Endings')
plt.ylabel('Count')
plt.title('Ending Counts')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('Game_Endings.png', format='png')
#plt.show()

