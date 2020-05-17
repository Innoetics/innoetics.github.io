from os import listdir
from os.path import isfile, join

with open('transcript.txt') as f:
    temp = [x.rstrip().split('\t') for x in f]
    transcript = {line[0]: line[1] for line in temp}
    print(transcript)
for i in range(1,3):
    mypath = f'bench{i}' 
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    print(files)