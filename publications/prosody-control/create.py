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
out.write('<h2 style="text-align: left;">1) F0 modification based on offset from ground truth labels</h2>\n')
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
out.write('<h2 style="text-align: left;">2) Duration modification based on offset from ground truth labels</h2>\n')
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
out.write('<h2 style="text-align: left;">3) Joint model modification based on offset from ground truth labels</h2>\n')
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

# F0 single cluster
out.write('<h2 style="text-align: left;">4) F0 single cluster for all phonemes</h2>\n')
mypath = f'audio/f0-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
for fname in ['10-AWK', '10027-LCL', '10008-LCL']:
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
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'f0_asc_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="f0_asc_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Asc
    out.write('<div class="mod-container">\n')
    for moda in [f'{i}' for i in list(range(0, 12))]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_asc_{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="f0_asc_{fname}_{moda}" controls>\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Duration single cluster
out.write('<h2 style="text-align: left;">5) Duration single cluster for all phonemes (excluding extreme clusters because of instabilities)</h2>\n')
mypath = f'audio/dur-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
for fname in ['10-AWK', '10008-LCL', '10003-LCL']:
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
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'dur_asc_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="dur_asc_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Asc
    out.write('<div class="mod-container">\n')
    for moda in [f'{i}' for i in list(range(1, 14))]:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_asc_{fname}_{moda}\'))">{moda}</div>\n')
        out.write(f'<audio id="dur_asc_{fname}_{moda}" controls>\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Word augmentation
out.write('<h2 style="text-align: left;">6) Single word augmentation</h2>\n')
mypath = f'audio/f0-word-augm'
mypath_dur = f'audio/dur-word-augm'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
fname = '10-AWK'
for wordd in [0, 1, 2, 6]:
    word = str(wordd)
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    title = transcript[fname]
    title = title.split(' ')
    title[wordd] = '<span style="color:red">' + title[wordd] + '</span>' if ',' not in title[wordd] else '<span style="color:red">' + title[wordd].replace(',', '') + '</span>,'
    out.write(' '.join(title))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT-+0
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'word_augm_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="word_augm_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Asc - F0
    out.write('<div class="mod-container">\n')
    for moda in ['dum'] + [f'{i}' for i in list(range(0, 12))]:
        out.write('<div class="sample-audio">\n')
        if moda == 'dum':
            out.write(f'<div class="invisible axis">F0</div>\n')
        else:
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_augm_{fname}_{word}_{moda}\'))">{moda}</div>\n')
            out.write(f'<audio id="word_augm_{fname}_{word}_{moda}" controls>\n')
            out.write(f'<source src="{mypath}/{fname}_{word}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    # Asc - Dur
    out.write('<div class="mod-container">\n')
    for moda in ['dum'] + [f'{i}' for i in list(range(0, 15))]:
        out.write('<div class="sample-audio">\n')
        if moda == 'dum':
            out.write(f'<div class="invisible axis">Dur</div>\n')
        else:
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_augm_{fname}_{word}_{moda}_dur\'))">{moda}</div>\n')
            out.write(f'<audio id="word_augm_{fname}_{word}_{moda}_dur" controls>\n')
            out.write(f'<source src="{mypath_dur}/{fname}_{word}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Phoneme augmentation
out.write('<h2 style="text-align: left;">7) Single phoneme augmentation (SAMPA representation)</h2>\n')
mypath = f'audio/f0-phoneme'
mypath_dur = f'audio/dur-phoneme'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container">\n')
fname = '10003-LCL'
for idx, phonee in enumerate([0, 5]):
    phone = str(phonee)
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    title = transcript[fname]
    title = title.split(' ')
    if idx == 0:  # 0, 2
        title[0] = 'All (<span style="color:red">"Q</span> l)'
    elif idx == 1:
        title[2] = 'bad (b <span style="color:red">"{</span> d)'
    out.write(' '.join(title))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT-+0
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'phone_augm_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="phone_augm_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Asc - F0
    out.write('<div class="mod-container">\n')
    for moda in ['dum'] + [f'{i}' for i in list(range(0, 12))]:
        out.write('<div class="sample-audio">\n')
        if moda == 'dum':
            out.write(f'<div class="invisible axis">F0</div>\n')
        else:
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'phone_augm_{fname}_{phone}_{moda}\'))">{moda}</div>\n')
            out.write(f'<audio id="phone_augm_{fname}_{phone}_{moda}" controls>\n')
            out.write(f'<source src="{mypath}/{fname}_ph_{phone}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    # Asc - Dur
    out.write('<div class="mod-container">\n')
    for moda in ['dum'] + [f'{i}' for i in list(range(0, 15))]:
        out.write('<div class="sample-audio">\n')
        if moda == 'dum':
            out.write(f'<div class="invisible axis">Dur</div>\n')
        else:
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_augm_{fname}_{phone}_{moda}_dur\'))">{moda}</div>\n')
            out.write(f'<audio id="word_augm_{fname}_{phone}_{moda}_dur" controls>\n')
            out.write(f'<source src="{mypath_dur}/{fname}_ph_{phone}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
fname = '1000-MDW'
for idx, phonee in enumerate([8, 14]):
    phone = str(phonee)
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    title = transcript[fname]
    title = title.split(' ')
    if idx == 0:  # 0, 2
        title[2] = 'saw (s <span style="color:red">O:</span>)'
    elif idx == 1:
        title[4] = 'again (@ g <span style="color:red">E</span> n).'
    out.write(' '.join(title))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT-+0
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'phone_augm_{fname}_gt\'))">Ground Truth</div>\n')
    out.write(f'<audio id="phone_augm_{fname}_gt" controls>\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Asc - F0
    out.write('<div class="mod-container">\n')
    for moda in ['dum'] + [f'{i}' for i in list(range(0, 12))]:
        out.write('<div class="sample-audio">\n')
        if moda == 'dum':
            out.write(f'<div class="invisible axis">F0</div>\n')
        else:
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'phone_augm_{fname}_{phone}_{moda}\'))">{moda}</div>\n')
            out.write(f'<audio id="phone_augm_{fname}_{phone}_{moda}" controls>\n')
            out.write(f'<source src="{mypath}/{fname}_ph_{phone}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    # Asc - Dur
    out.write('<div class="mod-container">\n')
    for moda in ['dum'] + [f'{i}' for i in list(range(0, 15))]:
        out.write('<div class="sample-audio">\n')
        if moda == 'dum':
            out.write(f'<div class="invisible axis">Dur</div>\n')
        else:
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_augm_{fname}_{phone}_{moda}_dur\'))">{moda}</div>\n')
            out.write(f'<audio id="word_augm_{fname}_{phone}_{moda}_dur" controls>\n')
            out.write(f'<source src="{mypath_dur}/{fname}_ph_{phone}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Asc-desc
out.write('<h2 style="text-align: left;">8) Ascending-Descending samples</h2>\n')
mypath = f'audio/f0-ascdesc'
out.write('<div class="sample-container">\n')
fname = '1002-UTS'
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
out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'ascdesc_{fname}_gt\'))">Ground Truth</div>\n')
out.write(f'<audio id="ascdesc_{fname}_gt" controls>\n')
out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
# Asc
out.write('<div class="mod-container">\n')
for moda in ['asc', 'ascdesc', 'desc']:
    if moda == 'asc':
        text = 'Ascending F0'
    elif moda == 'ascdesc':
        text = 'Ascending-Descending F0'
    else:
        text = 'Descending F0'
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'f0_ascdesc_{fname}_{moda}\'))">{text}</div>\n')
    out.write(f'<audio id="f0_ascdesc_{fname}_{moda}" controls>\n')
    out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
out.write('</div>\n')
mypath = f'audio/dur-ascdesc'
out.write('<div class="mod-container">\n')
for moda in ['asc', 'ascdesc', 'desc']:
    if moda == 'asc':
        text = 'Ascending Duration'
    elif moda == 'ascdesc':
        text = 'Ascending-Descending Duration'
    else:
        text = 'Descending Duration'
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'dur_ascdesc_{fname}_{moda}\'))">{text}</div>\n')
    out.write(f'<audio id="dur_ascdesc_{fname}_{moda}" controls>\n')
    out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')

out.write('</body>\n')
out.write('</html>\n')
out.close()
