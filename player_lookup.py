#!//usr/bin/python3

import json
import requests
#import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys


bb_year=2023
url = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=10000000&game_type='R'&season='" + str(bb_year) + "'&sort_column='rbi'"

def create_output():

    try:
        r = requests.get(url, headers={"Content-Type": "application/json"})
        data = eval(r.text)
        
        players=data["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]
        for player in players:
            name_display_first_last=player["name_display_first_last"]
            print(name_display_first_last)

    except Exception as err:
        print(err)
        sys.exit(1)

if __name__ == '__main__':

    create_output()
