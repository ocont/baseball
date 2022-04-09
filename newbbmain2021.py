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

Gregg=["Manny Machado", "Nolan Arenado", "Giancarlo Stanton", "Bo Bichette", "Josh Bell"]
Tom=["Vladimir Guerrero Jr.", "Austin Riley", "Kyle Tucker", "Eugenio Suarez", "Tyler O'Neill"]
Randy=["Rafael Devers", "Xander Bogaerts", "Rhys Hoskins", "Alex Bregman", "Matt Chapman"]
Chris=["Bryce Harper", "Freddie Freeman", "Paul Goldschmidt", "George Springer", "Mookie Betts"]
Brett=["Salvador Perez", "Adam Duvall", "Joey Votto", "Mitch Haniger", "Austin Meadows"]
Zee=["Juan Soto", "Mike Trout", "Shohei Ohtani", "Trea Turner", "Luis Robert"]
Efran=["Teoscar Hernandez", "Nick Castellanos", "Aaron Judge", "Jorge Polanco", "Jesus Aguilar"]
Wie=["Jose Abreu", "Yordan Alvarez", "Ozzie Albies", "Marcell Ozuna", "Javier Baez"]
Rob=["Pete Alonso", "Jose Ramirez", "Franmil Reyes", "Jared Walsh", "Eloy Jimenez"]
Kevin=["Matt Olson", "J.D. Martinez", "Joey Gallo", "Carlos Correa", "Max Muncy"]


def create_output(NAME,LIST):
    try:
        player_data = {}
        player_count = 1
        rbi_total = 0

        url = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=100000&game_type='R'&season='2022'&sort_column='rbi'"

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
        create_output("Randy",Randy)
        create_output("Tom",Tom)
        create_output("Chris",Chris)
        create_output("Brett",Brett)
        create_output("Wie",Wie)
        create_output("Zee",Zee)
        create_output("Efran",Efran)
        create_output("Rob",Rob)
        create_output("Kevin",Kevin)
       
        file.close()

        sort_report()

    except Exception as err:
        print(err)
        sys.exit(1)
