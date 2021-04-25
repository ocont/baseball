### https://appac.github.io/mlb-data-api-docs/#player-data-player-info-get

import json
import requests
import pprint

url_stats = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season=2021&player_id=453568"

url_profile = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id=453568"
r_stats = requests.get(url_stats, headers={"Content-Type": "application/json"})
r_profile = requests.get(url_profile, headers={"Content-Type": "application/json"})

data_stats = eval(r_stats.text)
data_profile = eval(r_profile.text)

team_short=data_stats["sport_hitting_tm"]["queryResults"]["row"]["team_short"]
rbi=data_stats["sport_hitting_tm"]["queryResults"]["row"]["rbi"]
name_first=data_profile["player_info"]["queryResults"]["row"]["name_first"]
name_last=data_profile["player_info"]["queryResults"]["row"]["name_last"]




with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])
