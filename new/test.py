import json
import requests
import pprint
import argparse


Brett=["Jose Abreu","Matt Olson","J.D. Martinez","Michael A. Taylor"]
Gregg=["Mike Trout","Mookie Betts","Rhys Hoskins","Matt Chapman"]
Wie=["Freddie Freeman","Christian Yelich","Alex Bregman","Kyle Tucker"]
Randy=["Cody Bellinger","Joey Gallo","Xander Bogaerts","Carlos Correa"]
Dave=["Manny Machado","Nolan Arenado","Yordan Alvarez","Paul Goldschmidt"]
Tom=["Marcell Ozuna","Eugenio Suarez","Charlie Blackmon","Jorge Soler"]
Rob=["Bryce Harper","Rafael Devers","Michael Conforto","Giancarlo Stanton"]
Kevin=["Pete Alonso","Fernando Tatis Jr.","Ronald Acuna Jr.","Mike Moustakas"]
Angelo=["Vladimir Guerrero Jr.","Francisco Lindor","Aaron Judge","George Springer"]
Zee=["Anthony Rendon","Nelson Cruz","Nelson Cruz","Franmil Reyes"]
Arnie=["Juan Soto","Corey Seager","Eddie Rosario","Eric Hosmer"]
Efran=["Gleyber Torres","Javier Baez","Yu Chang","Trea Turner"]

def create_output(NAME,LIST):
    try:
        temp_list=[]
        for i in LIST:
            url = "http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='"+str(i)+"%25'"
            r = requests.get(url, headers={"Content-Type": "application/json"})
            data = eval(r.text)
            name_first=data["search_player_all"]["queryResults"]["row"]["name_first"]
            name_last=data["search_player_all"]["queryResults"]["row"]["name_last"]
            name_last=data["search_player_all"]["queryResults"]["row"]["name_last"]
            player_id=data["search_player_all"]["queryResults"]["row"]["player_id"]
            team_full=data["search_player_all"]["queryResults"]["row"]["team_full"]

            #print(NAME,name_first, name_last, team_full, player_id)
            temp_list.append(player_id)
            
        print(NAME + str(" ="),temp_list)
            #print(data)
    except Exception as err:
        print(err)

create_output("Brett",Brett)
create_output("Gregg",Gregg)
create_output("Wie",Wie)
create_output("Randy",Randy)
create_output("Dave",Dave)
create_output("Tom",Tom)
create_output("Rob",Rob)
create_output("Kevin",Kevin)
create_output("Angelo",Angelo)
create_output("Zee",Zee)
create_output("Arnie",Arnie)
create_output("Efran",Efran)
