#!//usr/bin/python3

import json
import requests
import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys


url = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='2017'&player_id='493316'"

r = requests.get(url, headers={"Content-Type": "application/json"})
print(r.status_code)
data = eval(r.text)
player=data["sport_hitting_tm"]["queryResults"]["row"]["rbi"]
print(player)
