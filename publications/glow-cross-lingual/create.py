import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

with open('audio/transcript.txt') as f:
    temp = [x.rstrip().split('\t') for x in f]
    transcript = {line[0].replace('.wav', ''): line[1] for line in temp}

gts = {}
gtwavs = {}
for dat in 'full lim'.split():
    for lang in 'en-US ko en-GB'.split():
        for gend in 'female male'.split():
            spk = f'{dat}_{lang}_{gend}'
            for k, v in transcript.items():
                if spk in k:
                    gts[spk] = v
                    gtwavs[spk] = f'{k}.wav'
                    break

out.write('<h3>Target language: en-US</h3>')
gtshow = 1
for fname in 'testenus1 testenus2 testenus3 testenus4'.split():
    out.write('<div class="sample">\n')
    # GT
    if gtshow == 1:
        # * GT full
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + 'full_en-US_female full_en-US_male full_ko_female full_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                pass
                # out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                spktit = spk_name.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{spk_name}_gt\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{spk_name}_gt" controls preload="none">\n')
                out.write(f'<source src="audio/{gtwavs[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        # * GT lim
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + 'lim_en-US_female lim_en-US_male lim_ko_female lim_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                pass
                # out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                spktit = spk_name.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{spk_name}_gt\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{spk_name}_gt" controls preload="none">\n')
                out.write(f'<source src="audio/{gtwavs[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        gtshow = 0
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    for system in 'TTS TTS-VC'.split():
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [system] + 'full_en-US_female full_en-US_male full_ko_female full_ko_male lim_en-US_female lim_en-US_male lim_ko_female lim_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if moda == system:
                out.write(f'<div class="invisible axis">{system}</div>\n')
            else:
                wav = f'{moda}_{fname}' if system == 'TTS' else f'{moda}_vc_{fname}'
                spktit = moda.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{system}_{moda}_{fname}\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{system}_{moda}_{fname}" controls preload="none">\n')
                out.write(f'<source src="audio/{wav}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Target language: ko</h3>')
gtshow = 1
for fname in 'testko1 testko3 testko5 testko6'.split():
    out.write('<div class="sample">\n')
    # GT
    if gtshow == 1:
        # * GT full
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + 'full_en-US_female full_en-US_male full_ko_female full_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                pass
                # out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                spktit = spk_name.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{spk_name}_gt\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{spk_name}_gt" controls preload="none">\n')
                out.write(f'<source src="audio/{gtwavs[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        # * GT lim
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + 'lim_en-US_female lim_en-US_male lim_ko_female lim_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                pass
                # out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                spktit = spk_name.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{spk_name}_gt\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{spk_name}_gt" controls preload="none">\n')
                out.write(f'<source src="audio/{gtwavs[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        gtshow = 0
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    for system in 'TTS TTS-VC'.split():
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [system] + 'full_en-US_female full_en-US_male full_ko_female full_ko_male lim_en-US_female lim_en-US_male lim_ko_female lim_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if moda == system:
                out.write(f'<div class="invisible axis">{system}</div>\n')
            else:
                wav = f'{moda}_{fname}' if system == 'TTS' else f'{moda}_vc_{fname}'
                spktit = moda.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{system}_{moda}_{fname}\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{system}_{moda}_{fname}" controls preload="none">\n')
                out.write(f'<source src="audio/{wav}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('<h3>Target language: en-GB</h3>')
gtshow = 1
for fname in 'testengb1 testengb2 testengb3 testengb4'.split():
    out.write('<div class="sample">\n')
    # GT
    if gtshow == 1:
        # * GT full
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + 'full_en-US_female full_en-US_male full_ko_female full_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                pass
                # out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                spktit = spk_name.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{spk_name}_gt\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{spk_name}_gt" controls preload="none">\n')
                out.write(f'<source src="audio/{gtwavs[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        # * GT lim
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + ['gt'] + 'lim_en-US_female lim_en-US_male lim_ko_female lim_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                pass
                # out.write(f'<div class="invisible"></div>\n')
            elif spk_name == 'gt':
                out.write(f'<div class="invisible axis">Ground Truth</div>\n')
            else:
                spktit = spk_name.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{spk_name}_gt\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{spk_name}_gt" controls preload="none">\n')
                out.write(f'<source src="audio/{gtwavs[spk_name]}" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        gtshow = 0
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')
    for system in 'TTS TTS-VC'.split():
        # Mods per speaker
        out.write('<div class="mod-container">\n')
        for moda in [system] + 'full_en-US_female full_en-US_male full_ko_female full_ko_male lim_en-US_female lim_en-US_male lim_ko_female lim_ko_male'.split():
            out.write('<div class="sample-audio">\n')
            if moda == system:
                out.write(f'<div class="invisible axis">{system}</div>\n')
            else:
                wav = f'{moda}_{fname}' if system == 'TTS' else f'{moda}_vc_{fname}'
                spktit = moda.replace("full", "Full").replace("lim", "Limited").split('_')
                out.write(f'<div class="gt speaker" onclick="togglePlay(document.getElementById(\'{system}_{moda}_{fname}\'))">{spktit[0]}</br>{spktit[1]}_{spktit[2]}</div>\n')
                out.write(f'<audio id="{system}_{moda}_{fname}" controls preload="none">\n')
                out.write(f'<source src="audio/{wav}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

# End
out.write('</body>\n')
out.write('</html>\n')
out.close()
