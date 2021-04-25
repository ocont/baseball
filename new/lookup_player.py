import json
import requests
import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--searchText', help='search text', required=True)
args = vars(parser.parse_args())

searchText = args['searchText']

url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='cespedes%25'"

r = requests.get(url, headers={"Content-Type": "application/json"})

data = eval(r.text)
name_first=data["search_player_all"]["queryResults"]["row"]["name_first"]
name_last=data["search_player_all"]["queryResults"]["row"]["name_last"]
name_last=data["search_player_all"]["queryResults"]["row"]["name_last"]
player_id=data["search_player_all"]["queryResults"]["row"]["player_id"]

print(name_first, name_last, player_id)
