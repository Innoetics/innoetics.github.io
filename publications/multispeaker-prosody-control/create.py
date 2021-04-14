import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

with open('audio/transcript.txt') as f:
    temp = [x.rstrip().split('|') for x in f]
    transcript = {line[0].replace('.wav', ''): line[1] for line in temp}

gt = {
    'cathy_1529-PER': 'cathy_1529-PER_gt_gt.wav',
    'cathy_302-SUM': 'cathy_302-SUM_gt_gt.wav',
    'jsj': 'jsj_2501-2600-60_gt_gt.wav',
    'lj': 'lj_LJ002-0017_gt_gt.wav',
    'martha': 'martha_neutral-2080-2099-9_gt_gt.wav',
    'obama': 'obama_01-7_gt_gt.wav'
}

# F0 offsets from ground truth
out.write('<a href="#title1" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title1">1) F0 modification based on offset from ground truth labels</h2></a>\n')
mypath = f'audio/f0-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['1529-PER', '302-SUM']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    spk_name = 'cathy-multi'
    orig_speaker = spk_name.split('-')[0]
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_gt_{spk_name}\'))">Ground Truth</div>\n')
    out.write(f'<audio id="f0_mod_{fname}_gt_{spk_name}" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'-{i}' for i in list(range(11, 0, -1))] + ['+0'] + [f'+{i}' for i in list(range(1, 12))]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="f0_mod_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_f0_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
for fname in ['302-SUM']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    out.write('<div class="mod-container">\n')
    for spk_name in ['dum'] + ['gt'] + ['obama', 'jsj', 'lj', 'martha']:
        out.write('<div class="sample-audio">\n')
        if spk_name == 'dum':
            out.write(f'<div class="invisible"></div>\n')
        elif spk_name == 'gt':
            out.write(f'<div class="invisible axis">Ground Truth</div>\n')
        else:
            orig_speaker = spk_name.split('-')[0]
            out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_gt_{spk_name}\'))">{spk_name}</div>\n')
            out.write(f'<audio id="f0_mod_{fname}_gt_{spk_name}" controls preload="none">\n')
            out.write(f'<source src="audio/gt/{gt[spk_name]}" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['obama-adapt', 'jsj-adapt', 'lj-adapt', 'martha-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'-{i}' for i in list(range(11, 0, -1))] + ['+0'] + [f'+{i}' for i in list(range(1, 12))]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_mod_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="f0_mod_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_f0_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# Dur offsets from ground truth
out.write('<a href="#title2" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title1">2) Duration modification based on offset from ground truth labels</h2></a>\n')
mypath = f'audio/dur-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['471-SUM', '863-LP']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    spk_name = 'cathy-multi'
    orig_speaker = spk_name.split('-')[0]
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_gt_{spk_name}\'))">Ground Truth</div>\n')
    out.write(f'<audio id="dur_mod_{fname}_gt_{spk_name}" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'-{i}' for i in list(range(11, 0, -1))] + ['+0'] + [f'+{i}' for i in list(range(1, 12))]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="dur_mod_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_duration_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
for fname in ['863-LP']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    out.write('<div class="mod-container">\n')
    for spk_name in ['dum'] + ['gt'] + ['obama', 'jsj', 'lj', 'martha']:
        out.write('<div class="sample-audio">\n')
        if spk_name == 'dum':
            out.write(f'<div class="invisible"></div>\n')
        elif spk_name == 'gt':
            out.write(f'<div class="invisible axis">Ground Truth</div>\n')
        else:
            orig_speaker = spk_name.split('-')[0]
            out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_gt_{spk_name}\'))">{spk_name}</div>\n')
            out.write(f'<audio id="dur_mod_{fname}_gt_{spk_name}" controls preload="none">\n')
            out.write(f'<source src="audio/gt/{gt[spk_name]}" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['obama-adapt', 'jsj-adapt', 'lj-adapt', 'martha-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'-{i}' for i in list(range(11, 0, -1))] + ['+0'] + [f'+{i}' for i in list(range(1, 12))]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_mod_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="dur_mod_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_duration_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# F0 ascending
out.write('<a href="#title3" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title1">3) F0 single cluster for all phonemes</h2></a>\n')
mypath = f'audio/f0-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['978-SUM', '996-SUM']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    spk_name = 'cathy-multi'
    orig_speaker = spk_name.split('-')[0]
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'f0_asc_{fname}_gt_{spk_name}\'))">Ground Truth</div>\n')
    out.write(f'<audio id="f0_asc_{fname}_gt_{spk_name}" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_asc_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="f0_asc_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_asc_f0_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
for fname in ['996-SUM']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    out.write('<div class="mod-container">\n')
    for spk_name in ['dum'] + ['gt'] + ['obama', 'jsj', 'lj', 'martha']:
        out.write('<div class="sample-audio">\n')
        if spk_name == 'dum':
            out.write(f'<div class="invisible"></div>\n')
        elif spk_name == 'gt':
            out.write(f'<div class="invisible axis">Ground Truth</div>\n')
        else:
            orig_speaker = spk_name.split('-')[0]
            out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'f0_asc_{fname}_gt_{spk_name}\'))">{spk_name}</div>\n')
            out.write(f'<audio id="f0_asc_{fname}_gt_{spk_name}" controls preload="none">\n')
            out.write(f'<source src="audio/gt/{gt[spk_name]}" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['obama-adapt', 'jsj-adapt', 'lj-adapt', 'martha-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'f0_asc_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="f0_asc_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_asc_f0_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# Dur ascending
out.write('<a href="#title4" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title1">4) Duration single cluster for all phonemes</h2></a>\n')
mypath = f'audio/dur-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['1864-SLM', '567-RWV']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    spk_name = 'cathy-multi'
    orig_speaker = spk_name.split('-')[0]
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'dur_asc_{fname}_gt_{spk_name}\'))">Ground Truth</div>\n')
    out.write(f'<audio id="dur_asc_{fname}_gt_{spk_name}" controls preload="none">\n')
    out.write(f'<source src="{mypath}/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_asc_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="dur_asc_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_asc_duration_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
for fname in ['567-RWV']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    out.write('<div class="mod-container">\n')
    for spk_name in ['dum'] + ['gt'] + ['obama', 'jsj', 'lj', 'martha']:
        out.write('<div class="sample-audio">\n')
        if spk_name == 'dum':
            out.write(f'<div class="invisible"></div>\n')
        elif spk_name == 'gt':
            out.write(f'<div class="invisible axis">Ground Truth</div>\n')
        else:
            orig_speaker = spk_name.split('-')[0]
            out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'dur_asc_{fname}_gt_{spk_name}\'))">{spk_name}</div>\n')
            out.write(f'<audio id="dur_asc_{fname}_gt_{spk_name}" controls preload="none">\n')
            out.write(f'<source src="audio/gt/{gt[spk_name]}" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
        out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['obama-adapt', 'jsj-adapt', 'lj-adapt', 'martha-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'dur_asc_{fname}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="dur_asc_{fname}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_asc_duration_{moda}.wav" type="audio/wav">\n')
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
