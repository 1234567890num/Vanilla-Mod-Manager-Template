import os
import json
import random

sfiles = []
folder1 = 'ard'
for root, dirs, files in os.walk(folder1):
    for file in files:
        sfiles.append(root+'\\'+file)

Text = 'SetProgressFlag 0x106F'
print('Searching for '+Text+'...')
for file in sfiles:
    f = open(file).read()
    if Text in f:
        x = f.find(Text)
        x = ''
        print(file, x)
