import json
from datetime import datetime

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

with open('games_dev_2024_08_01.json', 'r') as file:
    data = json.load(file)


    for item in data:
        try:
            _id = item['_id']
            users = item['us']
            p0 = item['p0']
            p1 = item['p1']
            s = item['s']
            t = item['t']
            ca = parse_date(item['ca']['$date'])
            ua = parse_date(item['ua']['$date'])
            so = item['so']
            w = item['w']
            wid = item['wid']

            print(f"ID: {_id}")
            print(f"Users: {users}")
            print(f"P0: {p0}")
            print(f"P1: {p1}")
            print(f"S: {s}")
            print(f"T: {t}")
            print(f"Created At: {ca}")
            print(f"Updated At: {ua}")
            print(f"SO: {so}")
            print(f"W: {w}")
            print(f"WID: {wid}")

            print("")
            
        except:
            print("Invalid data entry")