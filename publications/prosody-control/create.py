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
out.write('<a href="#title1" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title1">1) F0 modification based on offset from ground truth labels</h2></a>\n')
mypath = f'audio/f0-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="f0_mod_{fname}_gt" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    moda = '+0'
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_{moda}\'))">{moda}</div>\n')
    out.write(f'<audio id="f0_mod_{fname}_{moda}" controls preload="none">\n')
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
        out.write(f'<audio id="f0_mod_{fname}_{moda}" controls preload="none">\n')
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
        out.write(f'<audio id="f0_mod_{fname}_{moda}" controls preload="none">\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Duration offsets from ground truth
out.write('<a href="#title2" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title2">2) Duration modification based on offset from ground truth labels</h2></a>\n')
mypath = f'audio/dur-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="dur_mod_{fname}_gt" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{fname}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    moda = '+0'
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_{moda}\'))">{moda}</div>\n')
    out.write(f'<audio id="dur_mod_{fname}_{moda}" controls preload="none">\n')
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
        out.write(f'<audio id="dur_mod_{fname}_{moda}" controls preload="none">\n')
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
        out.write(f'<audio id="dur_mod_{fname}_{moda}" controls preload="none">\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Joint model
out.write('<a href="#title3" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title3">3) Joint model modification based on offset from ground truth labels</h2></a>\n')
mypath = f'audio/joint-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="joint_mod_{fname}_gt" controls preload="none">\n')
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
                out.write(f'<audio id="joint_mod_{fname}_{moda1}_{moda2}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{fname}_{moda1}_{moda2}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
                out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# F0 single cluster
out.write('<a href="#title4" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title4">4) F0 single cluster for all phonemes</h2></a>\n')
mypath = f'audio/f0-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="f0_asc_{fname}_gt" controls preload="none">\n')
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
        out.write(f'<audio id="f0_asc_{fname}_{moda}" controls preload="none">\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Duration single cluster
out.write('<a href="#title5" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title5">5) Duration single cluster for all phonemes (excluding extreme clusters because of instabilities)</h2></a>\n')
mypath = f'audio/dur-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="dur_asc_{fname}_gt" controls preload="none">\n')
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
        out.write(f'<audio id="dur_asc_{fname}_{moda}" controls preload="none">\n')
        out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Word augmentation
out.write('<a href="#title6" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title6">6) Single word augmentation</h2></a>\n')
mypath = f'audio/f0-word-augm'
mypath_dur = f'audio/dur-word-augm'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="word_augm_{fname}_gt" controls preload="none">\n')
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
            out.write(f'<audio id="word_augm_{fname}_{word}_{moda}" controls preload="none">\n')
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
            out.write(f'<audio id="word_augm_{fname}_{word}_{moda}_dur" controls preload="none">\n')
            out.write(f'<source src="{mypath_dur}/{fname}_{word}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Phoneme augmentation
out.write('<a href="#title7" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title7">7) Single phoneme augmentation (SAMPA representation)</h2></a>\n')
mypath = f'audio/f0-phoneme'
mypath_dur = f'audio/dur-phoneme'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')
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
    out.write(f'<audio id="phone_augm_{fname}_gt" controls preload="none">\n')
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
            out.write(f'<audio id="phone_augm_{fname}_{phone}_{moda}" controls preload="none">\n')
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
            out.write(f'<audio id="word_augm_{fname}_{phone}_{moda}_dur" controls preload="none">\n')
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
    out.write(f'<audio id="phone_augm_{fname}_gt" controls preload="none">\n')
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
            out.write(f'<audio id="phone_augm_{fname}_{phone}_{moda}" controls preload="none">\n')
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
            out.write(f'<audio id="word_augm_{fname}_{phone}_{moda}_dur" controls preload="none">\n')
            out.write(f'<source src="{mypath_dur}/{fname}_ph_{phone}_{moda}.wav" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    out.write('</div>\n')
out.write('</div>\n')

# Asc-desc
out.write('<a href="#title8" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title8">8) Ascending-Descending samples</h2></a>\n')
mypath = f'audio/f0-ascdesc'
out.write('<div class="sample-container" style="display:none">\n')
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
out.write(f'<audio id="ascdesc_{fname}_gt" controls preload="none">\n')
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
    out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'f0_ascdesc_{fname}_{moda}\'))">{text}</div>\n')
    out.write(f'<audio id="f0_ascdesc_{fname}_{moda}" controls preload="none">\n')
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
    out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'dur_ascdesc_{fname}_{moda}\'))">{text}</div>\n')
    out.write(f'<audio id="dur_ascdesc_{fname}_{moda}" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{fname}_{moda}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')

# Musical notes
out.write('<a href="#title9" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title9">9) Musical notes control</h2></a>\n')
mypath = f'audio/notes'
out.write('<div class="sample-container" style="display:none">\n')

# Utt 1
utt = 'utt1'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('The main umbrella group representing political and armed opposition factions, the High Negotiations Committee, meanwhile said it was granteed guarantees on the implementation of the truce deal before endorsing it.')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Do La Sol Fa Do - Do La Sol Fa Re - Re Sib La Sol Fa</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
# Utt 2
utt = 'utt2'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('The Reformation was a schism in Western Christianity initiated by Martin Luther and continued by Huldrych Zwingli, John Calvin and other Protestant Reformers in sixteenth century Europe.')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Do Mi Sol Do</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
# Utt 3
utt = 'utt3'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('Do Re Mi Fa Sol La Si Do Si La Sol Fa Mi Re Do')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Do Re Mi Fa Sol La Si Do Si La Sol Fa Mi Re Do</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
# Lala1
utt = 'lala1'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('Lalalala Lalalala.')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Fa Fa Fa Do - La La La Do</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
# Lala2
utt = 'lala2'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('Lalalala Lalalala.')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Fa Fa Fa Do - La La La Fa</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
# Cmajor
utt = 'cmajor'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('Lala Lala Lala Lala.')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Do Mi Sol Do</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')
# Fmajor
utt = 'fmajor'
out.write('<div class="sample">\n')
out.write('<div class="sample-title">\n')
out.write('<span class="quotation">&ldquo;</span>\n')
out.write('<div class="transcript">')
out.write('Lalala Lalala Lalala.')
out.write('</div>\n')
out.write('</div>\n')
out.write('<div class="mod-container">\n')
out.write('<span class="quotation">&sung;</span>\n')
out.write('<div class="sample-audio" style="padding-left:0px">\n')
out.write(f'<div class="note" onclick="togglePlay(document.getElementById(\'{utt}\'))">Fa La Do</div>\n')
out.write(f'<audio id="{utt}" controls preload="none">\n')
out.write(f'<source src="{mypath}/{utt}.wav" type="audio/wav">\n')
out.write('Your browser does not support the audio element.\n')
out.write('</audio>\n')
out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')

out.write('</div>\n')

# End
out.write('</body>\n')
out.write('</html>\n')
out.close()
