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

season_year = 2023
today = datetime.date.today()

Gregg = ["Teoscar Hernandez","Rafael Devers", "Freddie Freeman", "Aaron Judge", "Jose Abreu"]
Efrain =  ["Vladimir Guerrero Jr.", "Francisco Lindor", "Juan Soto", "Xander Bogaerts", "Gleyber Torres"]
Zee = ["Pete Alonso", "Austin Riley", "Randy Arozarena", "Eloy Jimenez", "Mike Trout"]
#Tom = ["Jose Ramirez", "Kyle Tucker", "Shohei Ohtani", "Adolis Garcia", "Mookie Betts"]
Tom = ["Adolis Garcia", "Kyle Tucker", "Shohei Ohtani", "Jose Ramirez", "Mookie Betts"]
Wie	= ["Matt Olson", "Manny Machado", "Giancarlo Stanton", "C.J. Cron", "Adam Duvall"]
Angelo = ["Nolan Arenado", "Kyle Schwarber", "Dansby Swanson", "Charlie Blackmon", "Trayce Thompson"]
Brett = ["Bo Bichette", "Yordan Alvarez", "Alex Bregman", "Paul Goldschmidt", "Trea Turner"]
Replacement = ["Aaron Judge", "Jose Ramirez", "Paul Goldschmidt", "C.J. Cron", "Mike Trout"]
table = []

def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

def get_player_id_name(name):
    try:
        player = statsapi.lookup_player(name, gameType=None, season=season_year, sportId=1)
        id = player[0]['id']
        firstLastName = player[0]['firstLastName']
        if name in Replacement:
            return id, strike(firstLastName)
        else:
            return id, firstLastName

    except Exception as err:
        print(err)
        sys.exit(1)


def get_stats(id, name):
    try:
        player = statsapi.player_stat_data(id, group = 'hitting')
        current_team = player['current_team']
        rbi = player['stats'][0]['stats']['rbi']
        if name in Replacement:
            return current_team, strike(str(rbi))
        else:
            return current_team, rbi

    except Exception as err:
        print(err)
        sys.exit(1)


def get_team_short_name(team, name):
    try:
        t = statsapi.lookup_team(team)
        fileCode = t[0]['fileCode'].upper()
        if name in Replacement:
            return strike(fileCode)
        else:
            return fileCode

    except IndexError:
        return "Minors"

    except Exception as err:
        print(err)
        sys.exit(1)


def main(name, player_list):
    try:
        temp_list = [name]

        for i in player_list:
            id, firstLastName = get_player_id_name(i)
            current_team, rbi = get_stats(id, i)
            fileCode = get_team_short_name(current_team, i)
            temp_list.append(firstLastName + "(" + fileCode + ")")
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
    try:
        main("Tom", Tom)
        main("Gregg", Gregg)
        main("Efrain", Efrain)
        main("Zee", Zee)
        main("Wie", Wie)
        main("Angelo", Angelo)
        main("Brett", Brett)

        write_report()

        sys.exit()

    except Exception as err:
        print(err)
        sys.exit(1)
