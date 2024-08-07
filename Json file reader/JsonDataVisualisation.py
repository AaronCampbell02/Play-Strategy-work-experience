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
option = 0

def variantGames():
    games = {
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
    lib0_games =[
        "Standard",
        "960",
        "from pos",
        "King of the hill",
        "Three check",
        "Anti chess",
        "Atomic",
        "Horde",
        "Racing kings",
        "Crazyhouse",
        "Lines of Action",
        "Five check",
        "No Castling",
        "Scrambled Eggs",
        "Monster"
    ]
    lib1_games = [
        "Standard Draughts",
        "Draughts from pos",
        "Antidraughts",
        "Frysk",
        "BRKTHRGH",
        "Frisian",
        "Russian",
        "Brazilian",
        "Pool",
        "Portuguese",
        "English"
    ]
    lib2_games = [
        "Shogi",
        "Xiangqi",
        "Mini Xiangqi",
        "Mini Shogi",
        "Othello",
        "Grand Othello",
        "Amazons",
        "Breakthrough",
        "Mini Breakthrough"
    ]
    lib3_games = [
        "Oware"
    ]
    lib4_games = [
        "Togyzkumalak"
    ]
    lib5_games = [
        "Go9x9",
        "Go13x13",
        "Go19x19"
    ]
    lib6_games = [
        "Backgammon",
        "Nackgammon"
    ]

    
    x0 = [0] * 15
    x1 = [0] * 11
    x2 = [0] * 9
    x3 = [0]
    x4 = [0]
    x5 = [0] * 3
    x6 = [0] * 2
    for item in data:
        try:
            lib = item['l']
            try:
                var = item['v']
            except:
                var = 1
            game = games[lib,var]
            match(lib):
                case 0:
                    i = lib0_games.index(game)
                    x0[i] += 1
                case _:
                    print("hi")
        except:
            print("error in data")
    plt.figure(figsize=(18, 10))
    plt.bar(lib0_games, x0, color = 'r', width = 0.5, label = "Chess Variants")
    plt.xlabel('Chess variants')
    plt.ylabel('Count')
    plt.title('Chess variants')
    plt.legend()
    plt.tight_layout()
    plt.savefig('VariantGames.png', format='png')
    plt.show()

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

with open('games_dev_2024_08_01.json', 'r') as file:
    data = json.load(file)
    while(option != 7):
        option = int(input("enter option "))
        match(option):
            case 1:
                variantGames()
            case 2:
                userGames()
            case 3:
                playerAdvantage()
                eloAdvantage()
            case 4:
                averageMoves()
            case 5:
                timePerVariant()
            case 6:
                averageGameTime()
            case _:
                option = 7





