import json
import requests
import pprint
import argparse


url = "http://lookup-service-prod.mlb.com/json/named.roster_40.bam?team_id='114'"
r = requests.get(url, headers={"Content-Type": "application/json"})
data = eval(r.text)

pprint.pprint(data)
