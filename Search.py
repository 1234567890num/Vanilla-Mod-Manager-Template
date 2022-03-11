import os
import json
import random

sfiles = []
folder1 = 'ard'
for root, dirs, files in os.walk(folder1):
    for file in files:
        sfiles.append(root+'\\'+file)

Text = 'Unk1d'
print('Searching for '+Text+'...')
for file in sfiles:
    f = open(file).read()
    if Text in f and ('Unk06' in f or 'BattleLevel' in f):
        x = f.find(Text)
        x = ''
        print(file, x)
