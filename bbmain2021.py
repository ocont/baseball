#!/usr/bin/python3

from pybaseball import batting_stats_bref
data = batting_stats_bref(2021)


#
## VARIABLES
#

Brett=["José Abreu","Matt Olson","J.D. Martinez","Michael A. Taylor"]
Gregg=["Mike Trout","Mookie Betts","Rhys Hoskins","Matt Chapman"]
Wee=["Freddie Freeman","Christian Yelich","Alex Bregman","Kyle Tucker"]
Randy=["Cody Bellinger","Joey Gallo","Xander Bogaerts","Carlos Correa"]
Dave=["Manny Machado","Nolan Arenado","Yordan Álvarez","Paul Goldschmidt"]
Tom=["Marcell Ozuna","Eugenio Suarez","Charlie Blackmon","Jorge Soler"]
Rob=["Bryce Harper","Rafael Devers","Michael Conforto","Giancarlo Stanton"]
Kevin=["Pete Alonso","Fernando Tatis Jr.","Ronald Acuna Jr.","Mike Moustakas"]
Angelo=["Vladimir Guerrero Jr.","Francisco Lindor","Aaron Judge","George Springer"]
Zee=["Anthony Rendon","Nelson Cruz","Josh Bell","Franmil Reyes"]
Arnie=["Juan Soto","CoreySeager","Eddie Rosario","Eric Hosmer"]
Efran=["Gleyber Torres","Javier Baez","Jose Ramirez","Trea Turner"]

email_addresses=["kjking10@gmail.com","howie.silverman923@gmail.com","kingr10178@gmail.com","eriver74@gmail.com","arnump50@gmail.com","neuby73@gmail.com","rayzerrenner@gmail.com","angelobartolotta67@gmail.com","mrozrandy@icloud.com","toconnelll@gmail.com","bretttheodore@gmail.com","gregg.wasserman@icloud.com"]


#
## FUNCTIONS
#

def create_output(NAME,LIST):
    try:
        playerdict={}
        playerrbitotal=0
        playercount=1
        for player in LIST:
            playerstats = data[data.Name == player ].head(2000)
            if playerstats.size != 0:
                playername=playerstats['Name'].values[0]
                playerteam=playerstats['Tm'].values[0]
                playerrbi=playerstats['RBI'].values[0]
                playerdict[playercount]=[playername,playerteam,playerrbi]
                playerrbitotal=playerrbitotal+playerrbi
                playercount=playercount+1
            else:
                playername=player
                playerteam="NO STATS"
                playerrbi=0
                playerdict[playercount]=[playername,playerteam,playerrbi]
                playerrbitotal=playerrbitotal+playerrbi
                playercount=playercount+1

        playerrbitotal=playerdict[1][2] + playerdict[2][2] + playerdict[3][2]

        print (NAME + "," + str(playerdict[1][0]) + "(" + str(playerdict[1][1]) + ")" + "," + str(playerdict[1][2]) + "," + playerdict[2][0] + "(" + str(playerdict[2][1]) + ")" + "," + str(playerdict[2][2]) + "," + playerdict[3][0] + "(" + str(playerdict[3][1]) + ")" + "," + str(playerdict[3][2]) + "," + str(playerrbitotal) + "," + playerdict[4][0] + "(" + str(playerdict[4][1]) + ")" + "," + str(playerdict[4][2]))
    except Exception as err:
        print (err)

#
## MAIN
#

print("Name,P1 Name,P1 RBI,P2 Name,P2 RBI,P3 Name,P3 RBI,Total,P4 Name,P4 RBI")
create_output("Brett",Brett)
create_output("Gregg",Gregg)
create_output("Wee",Wee)
create_output("Randy",Randy)
create_output("Dave",Dave)
create_output("Tom",Tom)
create_output("Rob",Rob)
create_output("Kevin",Kevin)
create_output("Angelo",Angelo)
create_output("Zee",Zee)
create_output("Arnie",Arnie)
create_output("Efran",Efran)

#print ("\n")
#for address in email_addresses:
#    print (address)
