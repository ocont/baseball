#!//usr/bin/python3

import json
import requests
#import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys

def create_output():

    try:
        url = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=100000&game_type='R'&season='2021'&sort_column='rbi'"

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
