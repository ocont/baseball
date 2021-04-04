#!/usr/bin/python3

#import csv
#data_in = csv.reader(open('output.csv'), delimiter=',')
#srt= sorted(data_in, key=lambda x: int(x[7]), reverse=True)

#print("Name,P1 Name,P1 RBI,P2 Name,P2 RBI,P3 Name,P3 RBI,Total,P4 Name,P4 RBI")
#for i in srt:
#    print(*i)

import pandas as pd
df = pd.read_csv("output.csv")
sorted_df = df.sort_values(by=["Total"], ascending=False)
sorted_df.to_csv('report.csv', index=False)
