import os
import json
import random

#Get new music filenames
sfiles = []
folder1 = 'ard'
for root, dirs, files in os.walk(folder1):
    for file in files:
        sfiles.append(root+'\\'+file)

print('Searching ...')
Text = 'Type '
for file in sfiles:
    f = open(file).read()
    if Text in f:
        x = f.find(Text)
        print(file, f[x:x+7].strip())
