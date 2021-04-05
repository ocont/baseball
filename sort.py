#!/usr/bin/python3

import pandas as pd
import datetime

today = datetime.date.today()

infile="reports/output.csv"
outfile="reports/"+str(today)+".csv"

df = pd.read_csv(infile)
sorted_df = df.sort_values(by=["Total"], ascending=False)
sorted_df.to_csv(outfile, index=False)
