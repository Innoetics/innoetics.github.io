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
    'cathy_1113-UTS': 'cathy_1113-UTS_gt_gt.wav',
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
for fname in ['504-SLM', '833-EFR']:
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
    out.write(f'<source src="audio/gt/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
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
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/f0-offset-mod/{fname}_gt_f0.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
gtshow = 1
for fname in ['302-PER', '6697-TES']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    if gtshow == 1:
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
        gtshow = 0
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
out.write('<a href="#title2" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title2">2) Duration modification based on offset from ground truth labels</h2></a>\n')
mypath = f'audio/dur-offset-mod'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['249-SUM', '443-SLM']:
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
    out.write(f'<source src="audio/gt/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
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
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/dur-offset-mod/{fname}_gt_duration.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
gtshow = 1
for fname in ['1864-SLM', '4235-SNS']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    if gtshow == 1:
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
        gtshow = 0
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
out.write('<a href="#title3" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title3">3) F0 single cluster for all phonemes</h2></a>\n')
mypath = f'audio/f0-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['1492-EFR', '3544-SNS']:
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
    out.write(f'<source src="audio/gt/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
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
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/f0-ascending/{fname}_asc_f0.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
gtshow = 1
for fname in ['443-SLM', '1754-SLM']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    if gtshow == 1:
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
        gtshow = 0
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
out.write('<a href="#title4" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title4">4) Duration single cluster for all phonemes</h2></a>\n')
mypath = f'audio/dur-ascending'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
for fname in ['2943-PER', '6697-TES']:
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
    out.write(f'<source src="audio/gt/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
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
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/dur-ascending/{fname}_asc_duration.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
gtshow = 1
for fname in ['191-SNS', '1269-EFR']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    if gtshow == 1:
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
        gtshow = 0
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

# Word augmentation
out.write('<a href="#title5" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title5">5) Single word augmentation</h2></a>\n')
mypath = f'audio/word'
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
ph_dict = {
    '786-EFR': '01',
}
fname = '786-EFR'
for waugment in ['01', '03']:
    if waugment == '03':
        ph_dict[fname] = '03'
        trans = transcript[fname].split()
        trans[3] = '<span style="color:red">intensify</span>'
    else:
        ph_dict[fname] = '01'
        trans = transcript[fname].split()
        trans[1] = '<span style="color:red">prolong</span>'
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(' '.join(trans))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    spk_name = 'cathy-multi'
    orig_speaker = spk_name.split('-')[0]
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'word_{fname}_gt_{spk_name}\'))">Ground Truth</div>\n')
    out.write(f'<audio id="word_{fname}_gt_{spk_name}" controls preload="none">\n')
    out.write(f'<source src="audio/gt/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['F0'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            elif moda == 'F0':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">F0</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="word_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_f0_w_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/word/{fname}_gt_f0_w_{waugment}_t.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['Dur'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            elif moda == 'Dur':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">Dur</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="word_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_duration_w_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/word/{fname}_gt_duration_w_{waugment}_t.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
gtshow = 1
ph_dict = {
    '3199-LCL': '02',
    '1135-SUM': '02'
}
for fname in list(ph_dict.keys()):
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    trans = transcript[fname].split()
    if fname == '3199-LCL':
        trans[2] = '<span style="color:red">really</span>'
    else:
        trans[2] = '<span style="color:red">anything</span>'
    out.write(' '.join(trans))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    if gtshow == 1:
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + ['obama', 'jsj', 'lj', 'martha']:
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                orig_speaker = spk_name.split('-')[0]
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'word_{fname}_gt_{spk_name}\'))">{spk_name}</div>\n')
                out.write(f'<audio id="word_{fname}_gt_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="audio/gt/{gt[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        gtshow = 0
    for spk_name in ['obama-adapt', 'jsj-adapt', 'lj-adapt', 'martha-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['F0'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            elif moda == 'F0':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">F0</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="word_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_f0_w_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['Dur'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible"></div>\n')
            elif moda == 'Dur':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">Dur</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'word_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="word_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_duration_w_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# Phoneme augmentation
out.write('<a href="#title6" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title6">6) Single phoneme augmentation (SAMPA representation)</h2></a>\n')
mypath = f'audio/phoneme'
out.write('<div class="sample-container" style="display:none">\n')

out.write('<h3>Multispeaker/speaker adaptation same voice comparison</h3>')
ph_dict = {
    '786-EFR': '06',
    '1525-SLM': '23',
    '1700-PER': '03',
    '1700-PER2': '10'
}
for fname2 in ['786-EFR', '1525-SLM', '1700-PER', '1700-PER2']:
    if fname2 == '1700-PER2':
        fname = '1700-PER'
        ph_dict[fname] = '10'
    else:
        fname = fname2
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    trans = transcript[fname].split()
    if fname2 == '786-EFR':
        trans[1] = 'prolong (p r @ l <span style="color:red">Q</span> N)'
    elif fname2 == '1525-SLM':
        trans[8] = 'not (n <span style="color:red">Q</span> t)'
    elif fname2 == '1700-PER':
        trans[1] = 'had (h <span style="color:red">{</span> d)'
    else:
        trans[4] = 'fault (f <span style="color:red">O:</span> l t)'
    out.write(' '.join(trans))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    spk_name = 'cathy-multi'
    orig_speaker = spk_name.split('-')[0]
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'phoneme_{fname}_gt_{spk_name}\'))">Ground Truth</div>\n')
    out.write(f'<audio id="phoneme_{fname}_gt_{spk_name}" controls preload="none">\n')
    out.write(f'<source src="audio/gt/{orig_speaker}_{fname}_gt_gt.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['F0'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            elif moda == 'F0':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">F0</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'phoneme_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="phoneme_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_f0_ph_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/phoneme/{fname}_gt_f0_ph_{ph_dict[fname]}_t.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')
    for spk_name in ['cathy-multi', 'cathy-adapt']:
        orig_speaker = spk_name.split('-')[0]
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['Dur'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            elif moda == 'Dur':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">Dur</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'phoneme_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="phoneme_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_duration_ph_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('<div class="mod-container">\n')
    out.write(f'<div class="invisible"></div>\n')
    out.write(f'<img src="plots/phoneme/{fname}_gt_duration_ph_{ph_dict[fname]}_t.png" alt="Description for image" width="999" height="250">\n')
    out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Speaker adaptation</h3>')
gtshow = 1
ph_dict = {
    '1700-PER': '10',
    '1862-SLM': '04'
}
for fname in list(ph_dict.keys()):
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    trans = transcript[fname].split()
    if fname == '1700-PER':
        trans[4] = 'fault (f <span style="color:red">O:</span> l t)'
    else:
        trans[1] = 'cannot (k { n <span style="color:red">@</span> t)'
    out.write(' '.join(trans))
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    if gtshow == 1:
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + ['obama', 'jsj', 'lj', 'martha']:
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                orig_speaker = spk_name.split('-')[0]
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'phoneme_{fname}_gt_{spk_name}\'))">{spk_name}</div>\n')
                out.write(f'<audio id="phoneme_{fname}_gt_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="audio/gt/{gt[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        gtshow = 0
    for spk_name in ['obama-adapt', 'jsj-adapt', 'lj-adapt', 'martha-adapt']:
        orig_speaker = spk_name.split('-')[0]
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['F0'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible axis">{spk_name}</div>\n')
            elif moda == 'F0':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">F0</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'phoneme_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="phoneme_f0_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_f0_ph_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        out.write('<div class="mod-container">\n')
        for moda in [spk_name] + ['Dur'] + [f'{i}' for i in range(0, 15)]:
            out.write('<div class="sample-audio">\n')
            if moda == spk_name:
                out.write(f'<div class="invisible"></div>\n')
            elif moda == 'Dur':
                out.write(f'<div class="invisible axis" style="width:48px;background-color:rgb(160,160,253)">Dur</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'phoneme_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}\'))">{moda}</div>\n')
                out.write(f'<audio id="phoneme_dur_{fname}_{ph_dict[fname]}_{moda}_{spk_name}" controls preload="none">\n')
                out.write(f'<source src="{mypath}/{spk_name}_{fname}_gt_duration_ph_{ph_dict[fname]}_t_{int(moda):02d}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# Prosody predictor
out.write('<a href="#title7" class="custom-a-href"><h2 style="text-align: left;" onclick="showSample(event)" id="title7">7) Prosody prediction</h2></a>\n')
mypath = f'audio/prospred'
files = sorted([f for f in listdir(mypath) if isfile(join(mypath, f))])
out.write('<div class="sample-container" style="display:none">\n')

namedict = {
    'gt': 'Ground Truth',
    'gt-labels': 'GT Labels',
    'predictor': 'Predictor',
    'predictor-ptts': 'Predictor-adapt',
    'random-labels': 'Random Labels',
    'nonattentive': 'Plain'
}

for fname in ['179-SNS', '191-SNS', '249-SUM', '504-SLM']:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    # GT
    out.write('<div class="mod-container">\n')
    for spk_name in ['gt', 'gt-labels', 'predictor', 'predictor-ptts', 'random-labels', 'nonattentive']:
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="gt pred" onclick="togglePlay(document.getElementById(\'pred_{spk_name}_{fname}\'))">{namedict[spk_name]}</div>\n')
        out.write(f'<audio id="pred_{spk_name}_{fname}" controls preload="none">\n')
        out.write(f'<source src="{mypath}/{spk_name}_{fname}.wav" type="audio/wav">\n')
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
