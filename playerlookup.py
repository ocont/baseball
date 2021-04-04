#!/usr/bin/python

from pybaseball import batting_stats_bref
data = batting_stats_bref(2017)

for i in data['Name']:
    print (i)
