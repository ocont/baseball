#!//usr/bin/python3

import statsapi
import pprint
import sys
from tabulate import tabulate
from operator import itemgetter
import smtplib
from email.mime.text import MIMEText
import sys
import datetime
import csv
import pandas as pd

today = datetime.date.today()

Gregg = ["Aaron Judge","Rafael Devers", "Freddie Freeman", "Teoscar Hernandez", "Jose Abreu"]
Efran =  ["Vladimir Guerrero Jr.", "Francisco Lindor", "Juan Soto", "Xander Bogaerts", "Gleyber Torres"]
Zee = ["Pete Alonso", "Austin Riley", "Mike Trout", "Eloy Jimenez", "Randy Arozarena"]
Tom = ["Jose Ramirez", "Kyle Tucker", "Shohei Ohtani", "Adolis Garcia", "Mookie Betts"]
Wie	= ["Matt Olson", "Manny Machado", "C.J. Cron", "Giancarlo Stanton", "Adam Duvall"]
Angelo = ["Nolan Arenado", "Kyle Schwarber", "Dansby Swanson", "Charlie Blackmon", "Trayce Thompson"]
Brett = ["Paul Goldschmidt", "Yordan Alvarez",	"Alex Bregman", "Bo Bichette", "Trea Turner"]

table = []

def get_player_id_name(name):
    try:
        #print(name)
        player = statsapi.lookup_player(name)
        #print(player)
        id = player[0]['id']
        firstLastName = player[0]['firstLastName']
        return id, firstLastName

    except Exception as err:
        print(err)
        sys.exit(1)


def get_stats(id):
    try:
        player = statsapi.player_stat_data(id, group = 'hitting')
        #pprint.pprint(player)
        current_team = player['current_team']
        rbi = player['stats'][0]['stats']['rbi']
        return current_team, rbi

    except Exception as err:
        print(err)
        sys.exit(1)


def get_team_short_name(team):
    try:
        t = statsapi.lookup_team(team)
        shortName = t[0]['shortName']
        return shortName

    except Exception as err:
        print(err)
        sys.exit(1)


def main(name, player_list):
    try:
        temp_list = [name]

        for i in player_list:
            id, firstLastName = get_player_id_name(i)
            current_team, rbi = get_stats(id)
            shortName = get_team_short_name(current_team)
            temp_list.append(firstLastName + "(" + shortName + ")")
            temp_list.append(rbi)
        rbi_total = temp_list[2] + temp_list[4] + temp_list[6]
        temp_list.append(rbi_total)

        table.append(temp_list)

    except Exception as err:
        print(err)
        sys.exit(1)


def write_report():
    try:
        outfile="reports/"+str(today)+".csv"
        latestfile="reports/latest.csv"
        table.sort(key=lambda x: x[11], reverse=True)
        table.insert(0, ['Name', 'Player1', 'RBI', 'Player2', 'RBI', 'Player3', 'RBI', 'Player4', 'RBI', 'Player5', 'RBI', 'TOTAL'])
        df = pd.DataFrame(table)
        df.to_csv(outfile, index=False, header=False)
        df.to_csv(latestfile, index=False, header=False)

    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':
    main("Tom", Tom)
    main("Gregg", Gregg)
    main("Efran", Efran)
    main("Zee", Zee)
    main("Wie", Wie)
    main("Angelo", Angelo)
    main("Brett", Brett)

    write_report()

    sys.exit()
