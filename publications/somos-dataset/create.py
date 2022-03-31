import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

with open('audio/transcript.txt') as f:
    temp = [x.rstrip().split('|') for x in f]
    transcript = {line[0]: line[1] for line in temp}

all_utterances = {k: [] for k in transcript.keys()}
for aud in os.listdir('audio'):
    if '.wav' in aud:
        all_utterances[aud.rsplit('_',1)[0]].append(aud)
all_utterances = {k: sorted(all_utterances[k]) for k in all_utterances.keys()}

for fname in transcript.keys():
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    out.write('<div class="mod-container">\n')
    for moda in [v[-7:-4] for v in all_utterances[fname]]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="{fname}_{moda}" controls preload="none">\n')
        out.write(f'<source src="audio/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/{fname}.png" alt="{fname}" width="1633" height="300">\n')
    out.write('</div>\n')
    out.write('<br>\n')
    out.write('<br>\n')

# End
out.write('</body>\n')
out.write('</html>\n')
out.close()

