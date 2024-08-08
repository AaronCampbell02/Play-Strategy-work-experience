#!/usr/bin/env python

import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import sys

STATUS = [
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
GAMES = {
    (0, 1): "Standard",
    (0, 2): "960",
    (0, 3): "from pos",
    (0, 4): "King of the hill",
    (0, 5): "Three check",
    (0, 6): "Anti chess",
    (0, 7): "Atomic",
    (0, 8): "Horde",
    (0, 9): "Racing kings",
    (0, 10): "Crazyhouse",
    (0, 11): "Lines of Action",
    (0, 12): "Five check",
    (0, 13): "No Castling",
    (0, 14): "Scrambled Eggs",
    (0, 15): "Monster",
    (1, 1): "Standard Draughts",
    (1, 3): "Draughts from pos",
    (1, 6): "Antidraughts",
    (1, 8): "Frysk",
    (1, 9): "BRKTHRGH",
    (1, 10): "Frisian",
    (1, 11): "Russian",
    (1, 12): "Brazilian",
    (1, 13): "Pool",
    (1, 14): "Portuguese",
    (1, 15): "English",
    (2, 1): "Shogi",
    (2, 2): "Xiangqi",
    (2, 4): "Mini Xiangqi",
    (2, 5): "Mini Shogi",
    (2, 6): "Othello",
    (2, 7): "Grand Othello",
    (2, 8): "Amazons",
    (2, 9): "Breakthrough",
    (2, 10): "Mini Breakthrough",
    (3, 1): "Oware",
    (4, 1): "Togyzkumalak",
    (5, 1): "Go9x9",
    (5, 2): "Go13x13",
    (5, 4): "Go19x19",
    (6, 1): "Backgammon",
    (6, 2): "Nackgammon",
}

def variantGames():
    lib0_games =[v for k,v in GAMES.items() if k[0] == 0]
    lib1_games = [v for k,v in GAMES.items() if k[0] == 1]
    lib2_games = [v for k,v in GAMES.items() if k[0] == 2 or k[0] == 3 or k[0] == 4]
    lib5_games = [v for k,v in GAMES.items() if k[0] == 5]
    lib6_games = [v for k,v in GAMES.items() if k[0] == 6]
    x0 = [0] * len(lib0_games)
    x1 = [0] * len(lib1_games)
    x2 = [0] * len(lib2_games)
    x5 = [0] * len(lib5_games)
    x6 = [0] * len(lib6_games)
    for item in data:
        try:
            lib = item['l']
            var = item.get('v',1)
            game = GAMES[lib,var]
            match(lib):
                case 0:
                    i = lib0_games.index(game)
                    x0[i] += 1
                case 1:
                    i = lib1_games.index(game)
                    x1[i] += 1
                case 2:
                    i = lib2_games.index(game)
                    x2[i] += 1
                case 3:
                    i = lib2_games.index(game)
                    x2[i] += 1
                case 4:
                    i = lib2_games.index(game)
                    x2[i] += 1
                case 5:
                    i = lib5_games.index(game)
                    x5[i] += 1
                case 6:
                    i = lib6_games.index(game)
                    x6[i] += 1
                case _:
                    print("invalid value")
        except:
            print("error in data")

    figX = 16
    figY = 8
    colours = ['red']
    results = x0
    x = lib0_games
    title = 'Chess variants'
    fileName = 'ChessGames.png'
    xAxis = title
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

    results = x1
    x = lib1_games
    title = 'Draughts variants'
    fileName = 'DraughtsGames.png'
    xAxis = title
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

    results = x2
    x = lib2_games
    title = 'Abstract Variants'
    fileName = 'AbstractGames.png'
    xAxis = title
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

    figX = 12
    results = x5
    x = lib5_games
    title = 'Go Variants'
    fileName = 'goGames.png'
    xAxis = title
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

    results = x6
    x = lib6_games
    title = 'Gammon Variants'
    fileName = 'gammonGames.png'
    xAxis = title
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

def userGames():
    x = []
    y = []
    count = 0
    dates = len(data)
    lastMonth = "null"
    for item in data:
        try:
            date = item["ca"]["$date"]
            date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
            count += 1

            if (lastMonth != "null" and lastMonth != date.month):
                formatter = mdates.ConciseDateFormatter(lastDate)
                y.append(lastDate)
                x.append(count)
                count = 0

            date_time_num = mdates.date2num(date)
            lastMonth = date.month
            lastDate = date_time_num

        except:
            print("invalid data value")

    y.append(lastDate)
    x.append(count)

    x0 = np.array(x)
    y0 = np.array(y)

    coefficients = np.polyfit(y0, x0, 1)
    function = np.poly1d(coefficients)
    trend_line = function(y0)
    
    plt.figure(figsize=(12, 8))
    plt.scatter(y,x , color='g', label='Games')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3)) 
    plt.plot(y0, trend_line, linestyle='--', color='g', label='Trend Line')

    plt.xlabel('Months')
    plt.ylabel('Count')
    plt.title('Games Per Month')
    plt.legend()
    plt.tight_layout()
    plt.savefig('gamesTrends.png', format='png')
    plt.show()

def playerAdvantage():
    winP1 = 0
    drawP1 = 0
    loseP1 = 0
    incompleteP1 = 0

    #change name of win1 ect
    winhElo = 0
    drawhElo = 0
    losehElo = 0
    incompletehElo = 0

    for item in data:
        drawB = False
        incompleteB = False
        try:
            status = item['s']
            if status == 34 or status == 32:
                drawP1 += 1
                drawB = True
            elif status == 39 or status == 10 or status == 20 or status == 25 or status == 37:
                incompleteP1 += 1
                incompleteB = True
            else:
                try:
                    wID = item['wid']
                except:
                    incompleteP1 += 1
                    incompleteB = True
                PlayersID = item['us']
                p1 = PlayersID[0]
                if(p1 == wID):
                    winP1 += 1
                else:
                    loseP1 += 1
            try:
                p1Elo = item['p0']['e']
            except:
                print("no elo value")
                p1Elo = 1500
            try:
                p2Elo = item['p1']['e']
            except:
                print("no elo value")
                p2Elo = 1500
            if(incompleteB == True):
                incompletehElo += 1
            elif(drawB == True):
                drawhElo += 1
            elif(p1Elo > p2Elo):
                higherElo = "player1"
            elif(p1Elo < p2Elo):
                higherElo = "player2"
            else:
                higherElo = "equal"
            if(p1 == wID and higherElo == "player1"):
                winhElo += 1
            elif(p1 != wID and higherElo == "player2"):
                winhElo += 1
            elif(higherElo == "equal"):
                higherElo = "equal"
                #no action as equal elo
            else:
                losehElo += 1
            
        except:
            print("invalid data value")

    figX = 12
    figY = 8
    colours = ['g','y','r','black']
    results = [winhElo,drawhElo,losehElo,incompletehElo]
    x = ["P1 Win","P1 Draw","P1 Loss","incomplete"]
    xAxis = "Results"
    title = 'Player one versus Player two peformance'
    fileName = 'P1VP2.png'
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

    results = [winhElo,drawhElo,losehElo,incompletehElo]
    x = ["Win","Draw","Loss","incomplete"]
    title = 'higher Elo peformance against lower Elo '
    fileName = 'HigherEloPeformance.png'
    drawBar(figX,figY,colours,results,title,xAxis,fileName,x)

def drawBar(figX,figY,colours,results,title,xAxis,fileName,x):
    plt.figure(figsize = (figX,figY))
    plt.bar(x, results, color = colours, width = .5)
    plt.xlabel(xAxis)
    plt.ylabel('Count')
    plt.title(title)
    plt.tight_layout()
    plt.savefig(fileName, format='png')
    plt.show()

def options(choice):
    choice = choice.lower()
    if choice == "all":
        variantGames()
        userGames()
        playerAdvantage()
    elif choice == "games_variety":
        variantGames()
    elif choice == "user_games":
        userGames()
    elif choice == "player_peformance":
        playerAdvantage()
    else:
        print("no valid value entered")

if __name__ == '__main__':
    args = sys.argv[1:]
    with open('games_dev_2024_08_01.json', 'r') as file:
        data = json.load(file)
        if len(args) == 1:
            options(args[0])






