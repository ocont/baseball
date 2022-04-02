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

url1 = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=3000&game_type='R'&season='" + str(date1) + "'&sort_column='rbi'"

url2 = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=3000&game_type='R'&season='" + str(date2) + "'&sort_column='rbi'"

r_1 = requests.get(url1, headers={"Content-Type": "application/json"})
data_1 = eval(r_1.text)
players_1=data_1["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]


r_2 = requests.get(url2, headers={"Content-Type": "application/json"})
data_2 = eval(r_2.text)
players_2=data_2["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]


for player_1 in players_1:
    ## GET PLAYERS AGE AND POSITION

    url_info = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id=" + str(player_1["player_id"])
    r_info = requests.get(url_info, headers={"Content-Type": "application/json"})
    data_info = eval(r_info.text)
    age = data_info["player_info"]["queryResults"]["row"]["age"]
    position = data_info["player_info"]["queryResults"]["row"]["primary_position_txt"]
    if position == "C" or position == "P":
        pass
    print(str(player_1["name_display_roster"]) +
          ";" +
          str(age) +
          ";" +
          str(position) +
          ";" +
          str(player_1["team_name"]) +
          ";" +
          str(player_1["ab"]) +
          ";" +
          str(player_1["rbi"]))
