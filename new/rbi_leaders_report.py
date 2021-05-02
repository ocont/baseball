import json
import requests
import pprint
import argparse

try:
    url = "http://lookup-service-prod.mlb.com/json/named.leader_hitting_repeater.bam?sport_code='mlb'&results=100000&game_type='R'&season='2021'&sort_column='rbi'"

    r = requests.get(url, headers={"Content-Type": "application/json"})
    data = eval(r.text)
    #pprint.pprint(data)
        

    players=data["leader_hitting_repeater"]["leader_hitting_mux"]["queryResults"]["row"]
    print(players)
    for player in players:
        name_display_first_last=player["name_display_first_last"]
        team_name=player["team_name"]
        rbi=player["rbi"]
        player_id=player["player_id"]

        print(name_display_first_last, team_name, rbi, player_id)
except Exception as err:
    print(err)
