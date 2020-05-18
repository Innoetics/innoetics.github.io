import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

with open('audio/transcript.txt') as f:
    temp = [x.rstrip().split('\t') for x in f]
    transcript = {line[0].replace('r5_', ''): line[1] for line in temp}

with open('audio/transcript_gt.txt') as f:
    temp2 = [x.rstrip().split('\t') for x in f]
    transcript_gt = {line[0]: line[1] for line in temp2}

out.write('<div class="sample-container">\n')
for x in ['LJ011-0015', 'LJ014-0028', 'LJ012-0061', 'LJ008-0124']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript_gt[x])
    out.write('</div>\n')
    out.write('</div>\n')
    out.write('<div class="sample-audio">\n')
    # out.write(f'<div class="r-number">Groundtruth</div>\n')
    out.write('<audio controls>\n')
    out.write(f'<source src="audio/gt/{x}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>')
    out.write('</div>\n')
out.write('</div>\n')

out.write('<h2 style="text-align: left;">Generated Samples</h2>\n')
for i in range(1, len(temp) + 1):
    mypath = f'audio/bench{i}'
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    out.write('<div class="sample-container">\n')
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    fname = files[0]
    r = re.findall(r'r\d+_', fname)[0].replace('r', '').replace('_', '')
    out.write(transcript[fname.replace(f'r{r}_', '').replace('.wav', '')])
    out.write('</div>\n')
    out.write('</div>\n')
    allfiles = {}
    for fname in files:
        r = re.findall(r'r\d+_', fname)[0].replace('r', '').replace('_', '')
        allfiles[f'{r}'] = fname
    for r in ['2', '3', '5', '7', '10']:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number">r{r}</div>\n')
        out.write('<audio controls>\n')
        out.write(f'<source src="audio/bench{i}/{allfiles[r]}" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>')
    
    out.write('</div>\n')
    out.write('</div>\n')

out.write('</body>\n')
out.write('</html>\n')
out.close()
