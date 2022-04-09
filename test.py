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


#url = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='2017'&player_id='493316'"

#r = requests.get(url, headers={"Content-Type": "application/json"})
#print(r.status_code)
#data = eval(r.text)
#player=data["sport_hitting_tm"]["queryResults"]["row"]["rbi"]
#print(player)

#url_current = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=5&game_type='R'&season='" + str(date1) + "'&sort_column='rbi'"

#r_current = requests.get(url_current, headers={"Content-Type": "application/json"})
#data_current = eval(r_current.text)
#players_current=data_current["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]

#pprint.pprint(players_current)

url_current = "http://lookup-service-prod.mlb.com/json/named.proj_pecota_batting.bam?season='2022'&player_id='547989'"

r_current = requests.get(url_current, headers={"Content-Type": "application/json"})
data_current = eval(r_current.text)
print(data_current)
#players_current=data_current["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]

#pprint.pprint(players_current)

