#!//usr/bin/python3

import json
import requests
#import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys

#Brett=["Jose Abreu","Matt Olson","J.D. Martinez","Michael A. Taylor"]
#Gregg=["Mike Trout","Matt Chapman","Rhys Hoskins","Mookie Betts"]
#Wie=["Freddie Freeman","Christian Yelich","Kyle Tucker", "Alex Bregman"]
#Randy=["Carlos Correa","Joey Gallo","Xander Bogaerts","Cody Bellinger"]
#Tom=["Jorge Soler","Eugenio Suarez","Charlie Blackmon","Marcell Ozuna"]
#Rob=["Bryce Harper","Rafael Devers","Giancarlo Stanton", "Michael Conforto"]
#Kevin=["Pete Alonso","Fernando Tatis Jr.","Ronald Acuna Jr.","Mike Moustakas"]
Angelo=["Vladimir Guerrero Jr.","Francisco Lindor","Aaron Judge","George Springer"]
#Zee=["Franmil Reyes","Nelson Cruz","Josh Bell","Anthony Rendon"]
#Melissa=["Juan Soto","Eric Hosmer","Eddie Rosario","Corey Seager"]
#Efran=["Trea Turner","Javier Baez","Jose Ramirez","Gleyber Torres"]

today = datetime.date.today()

Tom=["Jorge Soler","Eugenio Suarez","Charlie Blackmon","Marcell Ozuna", "Mookie Betts"]
Gregg=["Mike Trout","Matt Chapman","Rhys Hoskins","Nelson Cruz", "Juan Soto"]
Randy=["Carlos Correa","Joey Gallo","Xander Bogaerts","Cody Bellinger", "Aaron Judge"]

def create_output(NAME,LIST):

    try:
        player_data = {}
        player_count = 1
        rbi_total = 0

        url = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=100000&game_type='R'&season='2021'&sort_column='rbi'"

        r = requests.get(url, headers={"Content-Type": "application/json"})
        data = eval(r.text)
        
        players=data["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]
        
        for name in LIST:
            for player in players:
                name_display_first_last=player["name_display_first_last"]
                #print(name_display_first_last)
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
        rbi_total = player_data[1]["rbi"] + player_data[2]["rbi"] + player_data[3]["rbi"]
        print(rbi_total)

        #out.writerow( [ NAME, player_data[1]["player"], player_data[1]["team_abbrev"], str(player_data[1]["rbi"]), player_data[2]["player"], player_data[2]["team_abbrev"], str(player_data[2]["rbi"]), player_data[3]["player"],  player_data[3]["team_abbrev"], str(player_data[3]["rbi"]), str(rbi_total), player_data[4]["player"], player_data[4]["team_abbrev"], str(player_data[4]["rbi"]), player_data[5]["player"], player_data[5]["team_abbrev"], str(player_data[5]["rbi"]) ] )
        
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

        df = pd.read_csv(infile)
        sorted_df = df.sort_values(by=["Total"], ascending=False)
        sorted_df.to_csv(outfile, index=False)

    except Exception as err:
        print(err)
        sys.exit(1)


if __name__ == '__main__':

    try:
        file = open("reports/output.csv", "w")
        #out = csv.writer(file, delimiter=";")
        out = csv.writer(file)
        out.writerow( ['Name', 'P1 Name', 'P1 RBI', 'P2 Name', 'P2 RBI', 'P3 Name' , 'P3 RBI', 'Total', 'P4 Name', 'P4 RBI', 'P5 Name', 'P5 RBI'])

        create_output("Gregg",Gregg)
        create_output("Randy",Randy)
        create_output("Tom",Tom)

        file.close()

        #create_output("Brett",Brett)
        #create_output("Wie",Wie)
        #create_output("Melissa",Melissa)
        #create_output("Rob",Rob)
        #create_output("Kevin",Kevin)
        #create_output("Angelo",Angelo)
        #create_output("Zee",Zee)
        #create_output("Arnie",Arnie)
        #create_output("Efran",Efran)
        
        sort_report()

    except Exception as err:
        print(err)
        sys.exit(1)
