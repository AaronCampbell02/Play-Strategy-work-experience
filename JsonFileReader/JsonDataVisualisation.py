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
            lib = item.get('l',1)
            var = item.get('v',1)
            elo1 = item.get('e',1500)
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

    drawBar(16,8,'r',x0,'Chess Variants','Chess Variants','chessGames.png',lib0_games)

    drawBar(16,8,'r',x1,'Draughts Variants','Draughts Variants','draughtsGames.png',lib1_games)

    drawBar(16,8,'r',x2,'Abstract Variants','Abstract Variants','AbstractGames.png',lib2_games)

    drawBar(12,8,'r',x5,'Go Variants','Go Variants','goGames.png',lib5_games)

    drawBar(12,8,'r',x6,'Gammon Variants','Gammon Variants','gammonGames.png',lib6_games)

def userGames():
    x = []
    y = []
    count = 0
    dates = len(data)
    lastMonth = "null"
    for item in data:
        try:
            date = item.get("ca", {}).get("$date", 1)
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

    winhElo = 0
    drawhElo = 0
    losehElo = 0
    incompletehElo = 0

    for item in data:
        drawB = False
        incompleteB = False
        try:
            status = item.get('s',10)
            if status == 34 or status == 32:
                drawP1 += 1
                drawB = True
            elif status == 39 or status == 10 or status == 20 or status == 25 or status == 37:
                incompleteP1 += 1
                incompleteB = True
            else:
                wID = item.get('wid', "")
                if(wID == ""):
                    incompleteP1 += 1
                    incompleteB = True
                else:
                    PlayersID = item['us']
                    p1 = PlayersID[0]
                    if(p1 == wID):
                        winP1 += 1
                    else:
                        loseP1 += 1
            p1Elo = item.get('p0', {}).get('e', 1500)
            p2Elo = item.get('p1', {}).get('e', 1500)
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


    colours = ['g','y','r','black']
    drawBar(12,8,['g','y','r','black'],[winhElo,drawhElo,losehElo,incompletehElo],'Player One versus Player Two peformance',
            'Results','P1VP2.png',["P1 Win","P1 Draw","P1 Loss","incomplete"])

    drawBar(12,8,colours,[winhElo,drawhElo,losehElo,incompletehElo],'Higher Elo peformance against Lower Elo ',
            'Results','HigherEloPeformance.png',["Win","Draw","Loss","incomplete"])

def plotStackedBar(lib_games,w,d,l):
    plt.bar(lib_games,w, color='g', width=0.5, label='Wins')
    plt.bar(lib_games,d, bottom=w, color='y', width=0.5, label='Draws')
    plt.bar(lib_games,l, bottom=[i + j for i, j in zip(w, d)], color='r', width=0.5, label='Losses')

def p1VSp2All():

    lib0_games =[v for k,v in GAMES.items() if k[0] == 0]
    lib1_games = [v for k,v in GAMES.items() if k[0] == 1]
    lib2_games = [v for k,v in GAMES.items() if k[0] == 2 or k[0] == 3 or k[0] == 4]
    lib5_games = [v for k,v in GAMES.items() if k[0] == 5]
    lib6_games = [v for k,v in GAMES.items() if k[0] == 6]

    lib0_arr = [[0 for i in range(3)] for j in range(len(lib0_games))]
    lib1_arr = [[0 for i in range(3)] for j in range(len(lib1_games))]
    lib2_arr = [[0 for i in range(3)] for j in range(len(lib2_games))]
    lib5_arr = [[0 for i in range(3)] for j in range(len(lib5_games))]
    lib6_arr = [[0 for i in range(3)] for j in range(len(lib6_games))]

    incompleteGames = 0

    for item in data:
        try:
            lib = item.get('l',1)
            var = item.get('v',1)
            game = GAMES[lib,var]
            win = False
            loss = False
            draw = False
            status = item.get('s',10)
            if status == 34 or status == 32:
                draw = True
            elif status == 39 or status == 10 or status == 20 or status == 25 or status == 37:
                #Game isn't finished
                incompleteGames += 1  
            else:
                wID = item.get('wid', "")
                if(wID == ""):
                    incompleteGames += 1
                else:
                    PlayersID = item['us']
                    p1 = PlayersID[0]
                    if(p1 == wID):
                        win = True
                    else:
                        loss = True
            match(lib):
                case 0:
                    i = lib0_games.index(game)
                    if(win):
                        lib0_arr[i][0] += 1
                    elif(draw):
                        lib0_arr[i][1] += 1
                    else:
                        lib0_arr[i][2] += 1
                case 1:
                    i = lib1_games.index(game)
                    if(win):
                        lib1_arr[i][0] += 1
                    elif(draw):
                        lib1_arr[i][1] += 1
                    else:
                        lib1_arr[i][2] += 1
                case 2:
                    i = lib2_games.index(game)
                    if(win):
                        lib2_arr[i][0] += 1
                    elif(draw):
                        lib2_arr[i][1] += 1
                    else:
                        lib2_arr[i][2] += 1
                case 3:
                    i = lib2_games.index(game)
                    if(win):
                        lib2_arr[i][0] += 1
                    elif(draw):
                        lib2_arr[i][1] += 1
                    else:
                        lib2_arr[i][2] += 1
                case 4:
                    i = lib2_games.index(game)
                    if(win):
                        lib2_arr[i][0] += 1
                    elif(draw):
                        lib2_arr[i][1] += 1
                    else:
                        lib2_arr[i][2] += 1
                case 5:
                    i = lib5_games.index(game)
                    if(win):
                        lib5_arr[i][0] += 1
                    elif(draw):
                        lib5_arr[i][1] += 1
                    else:
                        lib5_arr[i][2] += 1
                case 6:
                    i = lib6_games.index(game)
                    if(win):
                        lib6_arr[i][0] += 1
                    elif(draw):
                        lib6_arr[i][1] += 1
                    else:
                        lib6_arr[i][2] += 1
                case _:
                    print("invalid value")
        except Exception as e:
            print(f"An error occurred: {e}")
    # plot for lib0
    plt.figure(figsize=(18,8))
    getProportion(lib0_arr)
    w = [lib0_arr[i][0] for i in range(len(lib0_arr))]
    d = [lib0_arr[i][1] for i in range(len(lib0_arr))]
    l = [lib0_arr[i][2] for i in range(len(lib0_arr))]
    plotStackedBar(lib0_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in lib0 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib0p1vsp2.png", format='png')
    plt.show()
    # plot for lib1
    plt.figure(figsize=(18,8))
    getProportion(lib1_arr)
    w = [lib1_arr[i][0] for i in range(len(lib1_arr))]
    d = [lib1_arr[i][1] for i in range(len(lib1_arr))]
    l = [lib1_arr[i][2] for i in range(len(lib1_arr))]
    plotStackedBar(lib1_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in lib1 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib1p1vsp2.png", format='png')
    plt.show()
    #plot for lib2
    plt.figure(figsize=(14,8))
    getProportion(lib2_arr)
    w = [lib2_arr[i][0] for i in range(len(lib2_arr))]
    d = [lib2_arr[i][1] for i in range(len(lib2_arr))]
    l = [lib2_arr[i][2] for i in range(len(lib2_arr))]
    plotStackedBar(lib2_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in lib2 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib2p1vsp2.png", format='png')
    plt.show()
    #plot for lib5
    plt.figure(figsize=(12,8))
    getProportion(lib5_arr)
    w = [lib5_arr[i][0] for i in range(len(lib5_arr))]
    d = [lib5_arr[i][1] for i in range(len(lib5_arr))]
    l = [lib5_arr[i][2] for i in range(len(lib5_arr))]
    plotStackedBar(lib5_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in lib5 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib5p1vsp2.png", format='png')
    plt.show()
    #plot for lib6
    plt.figure(figsize=(12,8))
    getProportion(lib6_arr)
    w = [lib6_arr[i][0] for i in range(len(lib6_arr))]
    d = [lib6_arr[i][1] for i in range(len(lib6_arr))]
    l = [lib6_arr[i][2] for i in range(len(lib6_arr))]
    plotStackedBar(lib6_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in lib6 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib6p1vsp2.png", format='png')
    plt.show()

def getProportion(lib_arr):
    for i in range(len(lib_arr)):
        try:
            total = 0
            wins = lib_arr[i][0]
            draws = lib_arr[i][1]
            losses = lib_arr[i][2]
            total = wins+ draws + losses
            lib_arr[i][0] = wins/total
            lib_arr[i][1] = draws/total
            lib_arr[i][2] = losses/total
        except:
            print("no games played")


def p1VSp2Rated():
    print("hi")
def p1VSp2Skilled():  
    lib0_games =[v for k,v in GAMES.items() if k[0] == 0]
    lib1_games = [v for k,v in GAMES.items() if k[0] == 1]
    lib2_games = [v for k,v in GAMES.items() if k[0] == 2 or k[0] == 3 or k[0] == 4]
    lib5_games = [v for k,v in GAMES.items() if k[0] == 5]
    lib6_games = [v for k,v in GAMES.items() if k[0] == 6]

    lib0_arr = [[0 for i in range(3)] for j in range(len(lib0_games))]
    lib1_arr = [[0 for i in range(3)] for j in range(len(lib1_games))]
    lib2_arr = [[0 for i in range(3)] for j in range(len(lib2_games))]
    lib5_arr = [[0 for i in range(3)] for j in range(len(lib5_games))]
    lib6_arr = [[0 for i in range(3)] for j in range(len(lib6_games))]

    incompleteGames = 0

    for item in data:
        try:
            p1Elo = item.get('p0', {}).get('e', 1500)
            p2Elo = item.get('p1', {}).get('e', 1500)
            if(p1Elo > 1500 and p2Elo > 1500):
                lib = item.get('l',1)
                var = item.get('v',1)
                game = GAMES[lib,var]
                win = False
                loss = False
                draw = False
                status = item.get('s',10)
                if status == 34 or status == 32:
                    draw = True
                elif status == 39 or status == 10 or status == 20 or status == 25 or status == 37:
                    #Game isn't finished
                    incompleteGames += 1  
                else:
                    wID = item.get('wid', "")
                    if(wID == ""):
                        incompleteGames += 1
                    else:
                        PlayersID = item['us']
                        p1 = PlayersID[0]
                        if(p1 == wID):
                            win = True
                        else:
                            loss = True
                match(lib):
                    case 0:
                        i = lib0_games.index(game)
                        if(win):
                            lib0_arr[i][0] += 1
                        elif(draw):
                            lib0_arr[i][1] += 1
                        else:
                            lib0_arr[i][2] += 1
                    case 1:
                        i = lib1_games.index(game)
                        if(win):
                            lib1_arr[i][0] += 1
                        elif(draw):
                            lib1_arr[i][1] += 1
                        else:
                            lib1_arr[i][2] += 1
                    case 2:
                        i = lib2_games.index(game)
                        if(win):
                            lib2_arr[i][0] += 1
                        elif(draw):
                            lib2_arr[i][1] += 1
                        else:
                            lib2_arr[i][2] += 1
                    case 3:
                        i = lib2_games.index(game)
                        if(win):
                            lib2_arr[i][0] += 1
                        elif(draw):
                            lib2_arr[i][1] += 1
                        else:
                            lib2_arr[i][2] += 1
                    case 4:
                        i = lib2_games.index(game)
                        if(win):
                            lib2_arr[i][0] += 1
                        elif(draw):
                            lib2_arr[i][1] += 1
                        else:
                            lib2_arr[i][2] += 1
                    case 5:
                        i = lib5_games.index(game)
                        if(win):
                            lib5_arr[i][0] += 1
                        elif(draw):
                            lib5_arr[i][1] += 1
                        else:
                            lib5_arr[i][2] += 1
                    case 6:
                        i = lib6_games.index(game)
                        if(win):
                            lib6_arr[i][0] += 1
                        elif(draw):
                            lib6_arr[i][1] += 1
                        else:
                            lib6_arr[i][2] += 1
                    case _:
                        print("invalid value")
        except Exception as e:
            print(f"An error occurred: {e}")
    # plot for lib0
    plt.figure(figsize=(18,8))
    getProportion(lib0_arr)
    w = [lib0_arr[i][0] for i in range(len(lib0_arr))]
    d = [lib0_arr[i][1] for i in range(len(lib0_arr))]
    l = [lib0_arr[i][2] for i in range(len(lib0_arr))]
    plotStackedBar(lib0_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in highly skilled (elo > 1500) lib0 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib0p1vsp2skilled.png", format='png')
    plt.show()
    # plot for lib1
    plt.figure(figsize=(18,8))
    getProportion(lib1_arr)
    w = [lib1_arr[i][0] for i in range(len(lib1_arr))]
    d = [lib1_arr[i][1] for i in range(len(lib1_arr))]
    l = [lib1_arr[i][2] for i in range(len(lib1_arr))]
    plotStackedBar(lib1_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in highly skilled (elo > 1500) lib1 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib1p1vsp2skilled.png", format='png')
    plt.show()
    #plot for lib2
    plt.figure(figsize=(14,8))
    getProportion(lib2_arr)
    w = [lib2_arr[i][0] for i in range(len(lib2_arr))]
    d = [lib2_arr[i][1] for i in range(len(lib2_arr))]
    l = [lib2_arr[i][2] for i in range(len(lib2_arr))]
    plotStackedBar(lib2_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in highly skilled (elo > 1500) lib2 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib2p1vsp2skilled.png", format='png')
    plt.show()
    #plot for lib5
    plt.figure(figsize=(12,8))
    getProportion(lib5_arr)
    w = [lib5_arr[i][0] for i in range(len(lib5_arr))]
    d = [lib5_arr[i][1] for i in range(len(lib5_arr))]
    l = [lib5_arr[i][2] for i in range(len(lib5_arr))]
    plotStackedBar(lib5_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in highly skilled (elo > 1500) lib5 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib5p1vsp2skilled.png", format='png')
    plt.show()
    #plot for lib6
    plt.figure(figsize=(12,8))
    getProportion(lib6_arr)
    w = [lib6_arr[i][0] for i in range(len(lib6_arr))]
    d = [lib6_arr[i][1] for i in range(len(lib6_arr))]
    l = [lib6_arr[i][2] for i in range(len(lib6_arr))]
    plotStackedBar(lib6_games,w,d,l)
    plt.xlabel('Games')
    plt.ylabel('Results')
    plt.title("Results for P1 VS P2 in highly skilled (elo > 1500) lib6 games")
    plt.tight_layout()
    plt.legend()
    plt.savefig("lib6p1vsp2skilled.png", format='png')
    plt.show()

def firstTurnAnalysis():
    print("enter 1 for all games")
    print("enter 2 for large rating difference games")
    print("enter 3 for skilled games over 1500")
    option = int(input("enter choice "))
    if option == 1:
        p1VSp2All()
    elif option == 2:
        p1VSp2Rated()
    elif option ==3:
        p1VSp2Skilled()
    else:
        print("not an option")

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
    elif choice == "first_turn":
        firstTurnAnalysis()
    else:
        print("no valid value entered")

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        with open('games_dev_2024_08_01.json', 'r') as file:
            data = json.load(file)
            options(args[0])






