#!//usr/bin/python3

import json
import requests
import pprint
import argparse

Brett=["Jose Abreu","Matt Olson","J.D. Martinez","Michael A. Taylor"]
Gregg=["Mike Trout","Matt Chapman","Rhys Hoskins","Mookie Bett"]
Wie=["Freddie Freeman","Christian Yelich","Kyle Tucker", "Alex Bregman"]
Randy=["Carlos Correa","Joey Gallo","Xander Bogaerts","Cody Bellinger"]
Dave=["Manny Machado","Nolan Arenado","Yordan Alvarez","Paul Goldschmidt"]
Tom=["Marcell Ozuna","Eugenio Suarez","Charlie Blackmon","Jorge Soler"]
Rob=["Bryce Harper","Rafael Devers","Giancarlo Stanton", "Michael Conforto"]
Kevin=["Pete Alonso","Fernando Tatis Jr.","Ronald Acuna Jr.","Mike Moustakas"]
Angelo=["Vladimir Guerrero Jr.","Francisco Lindor","Aaron Judge","George Springer"]
Zee=["Franmil Reyes","Nelson Cruz","Josh Bell","Anthony Rendon"]
Arnie=["Juan Soto","Eric Hosmer","Eddie Rosario","Corey Seager"]
Efran=["Gleyber Torres","Javier Baez","Jose Ramirez","Trea Turner"]

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

        print(
                NAME +
                "," +
                player_data[1]["player"] +
                "(" +
                player_data[1]["team_abbrev"] +
                ")," +
                str(player_data[1]["rbi"]) +
                "," +
                player_data[2]["player"] +
                "(" +
                player_data[2]["team_abbrev"] +
                ")," +
                str(player_data[2]["rbi"]) +
                "," +
                player_data[3]["player"] +
                "(" +
                player_data[3]["team_abbrev"] +
                ")," +
                str(player_data[3]["rbi"]) +
                "," +
                str(rbi_total) +
                "," +
                player_data[4]["player"] +
                "(" +
                player_data[4]["team_abbrev"] +
                ")," +
                str(player_data[4]["rbi"])
             )

    except Exception as err:
        print(err)

print("Name,P1 Name,P1 RBI,P2 Name,P2 RBI,P3 Name,P3 RBI,Total,P4 Name,P4 RBI")
create_output("Brett",Brett)
create_output("Gregg",Gregg)
#create_output("Wie",Wie)
create_output("Randy",Randy)
create_output("Dave",Dave)
reate_output("Tom",Tom)
create_output("Rob",Rob)
create_output("Kevin",Kevin)
create_output("Angelo",Angelo)
create_output("Zee",Zee)
create_output("Arnie",Arnie)
create_output("Efran",Efran)

## Randy Cody Bellinger, Carlos Correa
### Gregg Mookie Bett, Matt Chapman
### Rob Michael Conforto, Giancarlo Stanton
### Zee Anthony Rendon, Franmil Reyes
### Arnie Corey Seager, Eric Hosmer
### Wie Alex Bregman, Kyle Tucker
