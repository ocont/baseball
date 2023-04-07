#!/bin/bash

./bpools2023-backup.py 
git add reports/*
git commit -am "adding modules"
git push origin
