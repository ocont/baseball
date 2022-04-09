#!//usr/bin/python3

import json
import requests
import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys



date1 = 2021
date2 = 2020

url_current = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=3000&game_type='R'&season='" + str(date1) + "'&sort_column='rbi'"

r_current = requests.get(url_current, headers={"Content-Type": "application/json"})
data_current = eval(r_current.text)
players_current=data_current["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]

print("Name;Age;Position;Team;AB;RBI;SLG")
for player_current in players_current:
    avg = 0
    player_id = player_current["player_id"]
    name_display_roster = player_current["name_display_roster"]
    team_abbrev_current = player_current["team_abbrev"]
    ab_current = player_current["ab"]
    rbi_current = player_current["rbi"]
    slg_current = player_current["slg"]

    url_info = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id=" + str(player_current["player_id"])
    r_info = requests.get(url_info, headers={"Content-Type": "application/json"})
    data_info = eval(r_info.text)
    age = data_info["player_info"]["queryResults"]["row"]["age"]
    position = data_info["player_info"]["queryResults"]["row"]["primary_position_txt"]

    #if position == "C" or position == "P":
    if position == "P":
        pass
    else:

        print(str(name_display_roster) +
            ";" +
            str(age) +
            ";" +
            str(position) +
            ";" +
            str(team_abbrev_current) +
            ";" +
            str(ab_current) +
            ";" +
            str(rbi_current) +
            ";" +
            str(slg_current))
