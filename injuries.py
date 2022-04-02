#!//usr/bin/python3

import json
import requests
import pprint
#import argparse
import csv
import pandas as pd
import datetime
import sys


url = "http://lookup-service-prod.mlb.com/fantasylookup/json/json/named.wsfb_news_injury.bam"

r = requests.get(url, headers={"Content-Type": "application/json"})
print(r.status_code)
data = eval(r.text)
#players_1=data_1["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]
