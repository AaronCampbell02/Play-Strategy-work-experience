#!/usr/bin/env python

import json
from datetime import datetime
import sys

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
    all_arr = []
    dates = []
    lib_games =[v for k,v in GAMES.items()]
    for i in range(len(GAMES)):
        new_arr = [0]
        all_arr.append(new_arr)
    j = 0
    lastMonth = "null"
    for item in data:
        try:
            lib = item.get('l',10)
            var = item.get('v',1)
            if lib != 10:
                game = GAMES[lib,var]
                i = lib_games.index(game)
                date = item.get("ca", {}).get("$date", 1)
                date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
                all_arr[i][j] += 1

                if (lastMonth != "null" and lastMonth != date.month):
                    lastYear = str(date.strftime('%Y'))
                    lastMonth = str(date.strftime('%b'))
                    string = lastMonth + " " + lastYear
                    print("hi")
                    dates.append(string)
                    j += 1
                    for i in range(len(all_arr)):
                        all_arr[i].append(0)

                lastDate = date
                lastMonth = date.month
                lastYear = date.year
                
        except Exception as e:
            print(f"An error occurred: {e}")

    lastYear = str(date.strftime('%Y'))
    lastMonth = str(date.strftime('%b'))
    string = lastMonth + " " + lastYear
    dates.append(string)

    print((dates))
    outputData = {
        "dates": dates,
    }
    for j in range(len(lib_games)):
        name = lib_games[j]
        count = all_arr[j]
        outputData[name] = count

    with open('output_data.json', 'w') as json_file:
        json.dump(outputData, json_file, indent=4)



if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        with open('games_live_2024_08_01.json', 'r') as file:
            data = json.load(file)
            variantGames()
