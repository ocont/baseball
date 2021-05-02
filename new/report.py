### https://appac.github.io/mlb-data-api-docs/#player-data-player-info-get

import json
import requests
import pprint

year = 2021

Brett = ['547989', '621566', '502110', '572191']
Gregg = ['545361', '605141', '656555', '656305']
Wie = ['518692', '592885', '608324', '663656']
Randy = ['641355', '608336', '593428', '621043']
Dave = ['592518', '571448', '670541', '502671']
Tom = ['542303', '553993', '453568', '624585']
Rob = ['547180', '646240', '624424', '519317']
Kevin = ['624413', '665487', '660670', '519058']
Angelo = ['665489', '596019', '592450', '543807']
Zee = ['543685', '443558', '605137', '614177']
Arnie = ['665742', '608369', '592696', '543333']
Efran = ['650402', '595879', '608070', '607208']

def create_output(NAME,LIST):
    try:
        for player_id in LIST:
            url_stats = "http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season=" + str(year) + "&player_id=" + str(player_id)

            url_profile = "http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id=" + str(player_id)
            r_stats = requests.get(url_stats, headers={"Content-Type": "application/json"})
            r_profile = requests.get(url_profile, headers={"Content-Type": "application/json"})

            data_stats = eval(r_stats.text)
            data_profile = eval(r_profile.text)

            team_short=data_stats["sport_hitting_tm"]["queryResults"]["row"]["team_short"]
            rbi=data_stats["sport_hitting_tm"]["queryResults"]["row"]["rbi"]
            name_first=data_profile["player_info"]["queryResults"]["row"]["name_first"]
            name_last=data_profile["player_info"]["queryResults"]["row"]["name_last"]
            name_display_first_lastt=data_profile["player_info"]["queryResults"]["row"]["name_display_first_last"]

            print(name_display_first_lastt, team_short, rbi)

    except Exception as err:
        print(err)

#create_output("Brett",Brett)
#create_output("Gregg",Gregg)
#create_output("Wie",Wie)
#create_output("Randy",Randy)
#create_output("Dave",Dave)
#create_output("Tom",Tom)
#create_output("Rob",Rob)
#create_output("Kevin",Kevin)
create_output("Angelo",Angelo)
create_output("Zee",Zee)
create_output("Arnie",Arnie)
create_output("Efran",Efran)
