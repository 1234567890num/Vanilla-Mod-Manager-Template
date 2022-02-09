import os
import json
import random

sfiles = []
folder1 = 'ard'
for root, dirs, files in os.walk(folder1):
    for file in files:
        sfiles.append(root+'\\'+file)

Text = 'SetJump Type 0'
print('Searching ...')
for file in sfiles:
    f = open(file).read()
    if Text in f:
        x = f.find(Text)
        x = ''
        print(file, x)
