#!//usr/bin/python3

import json
import requests
#import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys

today = datetime.date.today()
bb_year=2023
url = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=1000000&game_type='R'&season='" + str(bb_year) + "'&sort_column='rbi'"

Gregg = ["Aaron Judge","Rafael Devers", "Freddie Freeman", "Teoscar Hernandez", "Jose Abreu"]
Efran =  ["Vladimir Guerrero Jr.", "Francisco Lindor", "Juan Soto", "Xander Bogaerts", "Gleyber Torres"]
Zee = ["Pete Alonso", "Austin Riley", "Mike Trout", "Eloy Jimenez", "Randy Arozarena"]
Tom = ["Jose Ramirez", "Kyle Tucker", "Shohei Ohtani", "Adolis Garcia", "Mookie Betts"]
Wie	= ["Matt Olson", "Manny Machado", "C.J. Cron", "Giancarlo Stanton", "Adam Duvall"]
Angelo = ["Nolan Arenado", "Kyle Schwarber", "Dansby Swanson", "Charlie Blackmon", "Trayce Thompson"]
Brett = ["Paul Goldschmidt", "Yordan Alvarez",	"Alex Bregman", "Bo Bichette", "Trea Turner"]

Replacement = []


def strike(text):
    return ''.join([u'\u0336{}'.format(c) for c in text])

def create_output(NAME,LIST):
    try:
        player_data = {}
        player_count = 1
        rbi_total = 0

        r = requests.get(url, headers={"Content-Type": "application/json"})
        data = eval(r.text)
        
        players=data["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]

        for name in LIST:
            player_found = "None"
            for player in players:
                name_display_first_last=player["name_display_first_last"]
                if name == name_display_first_last:
                    player_found = "Found"
                    team_name=player["team_name"]
                    team_abbrev=player["team_abbrev"]
                    rbi=player["rbi"]
                    player_id=player["player_id"]
                    player_data[player_count] = { 
                                                   "player": name_display_first_last,
                                                   "team_abbrev": team_abbrev,
                                                   "rbi": int(rbi),
                                                   "player_id": player_id
                                               }
                    player_count = player_count + 1
                    break
            
            if player_found == "None":
                team_name="NA"
                team_abbrev="NA"
                rbi=0
                player_id=0
                player_data[player_count] = {
                                               "player": name,
                                               "team_abbrev": team_abbrev,
                                               "rbi": int(rbi),
                                               "player_id": player_id
                                           }
                player_count = player_count + 1

        rbi_total = player_data[1]["rbi"] + player_data[2]["rbi"] + player_data[3]["rbi"]
       
        if player_data[4]["player"] in Replacement:
            player_data[4]["player"] = strike(player_data[4]["player"])
            player_data[4]["team_abbrev"] = strike(player_data[4]["team_abbrev"])
            player_data[4]["rbi"] = strike(str(player_data[4]["rbi"]))

        if player_data[5]["player"] in Replacement:
            player_data[5]["player"] = strike(player_data[5]["player"])
            player_data[5]["team_abbrev"] = strike(player_data[5]["team_abbrev"])
            player_data[5]["rbi"] = strike(str(player_data[5]["rbi"]))

        
        out.writerow( [ NAME, 
                        player_data[1]["player"] + "(" + str(player_data[1]["team_abbrev"]) + ")",
                        str(player_data[1]["rbi"]),
                        player_data[2]["player"] + "(" + str( player_data[2]["team_abbrev"]) + ")",
                        str(player_data[2]["rbi"]),
                        player_data[3]["player"] + "(" + str(player_data[3]["team_abbrev"]) + ")",
                        str(player_data[3]["rbi"]),
                        str(rbi_total),
                        player_data[4]["player"] + "(" + str(player_data[4]["team_abbrev"]) + ")",
                        str(player_data[4]["rbi"]),
                        player_data[5]["player"] + "(" + str(player_data[5]["team_abbrev"]) + ")",
                        str(player_data[5]["rbi"]) ] )

    except Exception as err:
        print(err)
        sys.exit(1)

def sort_report():
    try:
        infile="reports/output.csv"
        outfile="reports/"+str(today)+".csv"
        latestfile="reports/latest.csv"

        df = pd.read_csv(infile)
        sorted_df = df.sort_values(by=["Total"], ascending=False)
        sorted_df.to_csv(outfile, index=False)
        sorted_df.to_csv(latestfile, index=False)

    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':

    try:
        file = open("reports/output.csv", "w")
        out = csv.writer(file)
        out.writerow( ['Name', 'P1 Name', 'P1 RBI', 'P2 Name', 'P2 RBI', 'P3 Name' , 'P3 RBI', 'Total', 'P4 Name', 'P4 RBI', 'P5 Name', 'P5 RBI'])

        create_output("Gregg",Gregg)
        create_output("Tom",Tom)
        create_output("Brett",Brett)
        create_output("Wie",Wie)
        create_output("Zee",Zee)
        create_output("Efran",Efran)
        create_output("Angelo",Angelo)
       
        file.close()

        sort_report()

    except Exception as err:
        print(err)
        sys.exit(1)
