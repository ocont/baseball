from pybaseball import batting_stats_bref
data2019 = batting_stats_bref(2019)
data2020 = batting_stats_bref(2020)

for player2020 in data2020['Name']:
    playerstats2020 = data2020[data2020.Name == player2020 ].head(2000)
    Name2020=playerstats2020['Name'].values[0]
    Age2020=playerstats2020['Age'].values[0]
    Tm2020=playerstats2020['Tm'].values[0]
    G2020=playerstats2020['G'].values[0]
    AB2020=playerstats2020['AB'].values[0]
    RBI2020=playerstats2020['RBI'].values[0]

    G2019=0
    AB2019=0
    RBI2019=0

    for player2019 in data2019['Name']:
        playerstats2019 = data2019[data2019.Name == player2019 ].head(2000)
        Name2019=playerstats2019['Name'].values[0]
        if Name2020 == Name2019:
            G2019=playerstats2019['G'].values[0]
            AB2019=playerstats2019['AB'].values[0]
            RBI2019=playerstats2019['RBI'].values[0]
            break

    RBIavg=(RBI2019+RBI2020)/2

    print (Name2020+";"+str(Age2020)+";"+str(Tm2020)+";"+str(G2019)+";"+str(AB2019)+";"+str(RBI2019)+";"+str(G2020)+";"+str(AB2020)+";"+str(RBI2020)+";"+str(RBIavg))
