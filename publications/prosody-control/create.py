import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

with open('audio/transcript.txt') as f:
    temp = [x.rstrip().split('|') for x in f]
    transcript = {line[0].replace('.wav', ''): line[1] for line in temp}

# F0 offsets from ground truth
out.write('<h2 style="text-align: left;">F0 modification based on offset from ground truth labels</h2>\n')
mypath = f'audio/f0-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
for fname in ['10-AWK', '10-CHS', '10-ECO']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT-+0
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="f0_mod_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    moda = '+0'
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_{moda}\'))">{moda}</div>\n')
    out.write(f'<audio id="f0_mod_{fname}_{moda}" controls>\n')
    out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Minus
    out.write('<div class="mod-container">\n')
    for moda in [f'-{i}' for i in list(range(1, 9))]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="f0_mod_{fname}_{moda}" controls>\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    # Plus
    out.write('<div class="mod-container">\n')
    for moda in [f'+{i}' for i in list(range(1, 9))]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="f0_mod_{fname}_{moda}" controls>\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Duration offsets from ground truth
out.write('<h2 style="text-align: left;">Duration modification based on offset from ground truth labels</h2>\n')
mypath = f'audio/dur-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
for fname in ['10-AWK', '10-CHS', '10-ECO']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT-+0
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="dur_mod_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    moda = '+0'
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_{moda}\'))">{moda}</div>\n')
    out.write(f'<audio id="dur_mod_{fname}_{moda}" controls>\n')
    out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Minus
    out.write('<div class="mod-container">\n')
    for moda in [f'-{i}' for i in list(range(1, 9))]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="dur_mod_{fname}_{moda}" controls>\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    # Plus
    out.write('<div class="mod-container">\n')
    for moda in [f'+{i}' for i in list(range(1, 9))]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="dur_mod_{fname}_{moda}" controls>\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Joint model
out.write('<h2 style="text-align: left;">Joint model modification based on offset from ground truth labels</h2>\n')
mypath = f'audio/joint-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
for fname in ['10-AWK', '10-CHS', '10-ECO']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'joint_mod_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="joint_mod_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Minus
    rang = 4
    for moda1 in ['dum'] + [f'-{i}' for i in list(range(rang, 0, -1))] + ['+0'] + [f'+{i}' for i in list(range(1, rang + 1))]:
        out.write('<div class="mod-container">\n')
        out.write('<div class="sample-audio">\n')
        if moda1 == '+0':
            out.write(f'<div class="invisible axis">F0</div>\n')
        else:
            out.write(f'<div class="invisible"></div>\n')
        out.write('</div>\n')
        for moda2 in [f'-{i}' for i in list(range(rang, 0, -1))] + ['+0'] + [f'+{i}' for i in list(range(1, rang + 1))]:
            if moda1 == 'dum':
                out.write('<div class="sample-audio">\n')
                if moda2 == '+0':
                    out.write(f'<div class="invisible axis">Dur</div>\n')
                else:
                    out.write(f'<div class="invisible"></div>\n')
                out.write('</div>\n')
            else:
                out.write('<div class="sample-audio">\n')
                out.write(f'<div class="r-number-aug" onclick="togglePlay(document.getElementById(\'joint_mod_{fname}_{moda1}_{moda2}\'))">{moda1}_{moda2}</div>\n')
                out.write(f'<audio id="joint_mod_{fname}_{moda1}_{moda2}" controls>\n')
                out.write(f'<source src="{mypath}/{fname}_{moda1}_{moda2}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
                out.write('</div>\n')
        out.write('</div>\n')

    out.write('</div>\n')
out.write('</div>\n')

out.write('</body>\n')
out.write('</html>\n')
out.close()
