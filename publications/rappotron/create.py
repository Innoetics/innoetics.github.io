import os
from os import listdir
from os.path import isfile, join
import re


os.system('cat template.html > index.html')
out = open('index.html', 'a')

songs = ['song_01', 'song_02', 'song_03', 'song_04', 'song_05', 'rap_song01', 'rap_song02']
speakers = ['US_TR_M1', 'US_TR_F1', 'US_TR_F2', 'KO_TR_F1', 'KO_TR_F2', 'US_AD_M1', 'KO_AD_M1', 'Mellotron']

# Speaker ground truths
out.write('<div class="sample-container">\n')
out.write('<h2>Speaker ground truth samples</h2>')
out.write('<div class="sample">\n')
# GT
out.write('<div class="mod-container">\n')
for spk in speakers:
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'spkgt_{spk}_gt\'))">{spk}</div>\n')
    out.write(f'<audio id="spkgt_{spk}_gt" controls preload="none">\n')
    out.write(f'<source src="audio/gt/{spk}.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
out.write('</div>\n')
out.write('</div>\n')

out.write('</div>\n')

# Songs
out.write('<div class="sample-container">\n')
out.write('<h2>Rapping/Singing speech synthesis</h2>')

for fname in songs:
    songname = fname.replace('song_', 'Song ').replace('rap_', 'Rap ').replace('song01', 'song 01').replace('song02', 'song 02')
    out.write('<div class="sample">\n')
    # GT
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="invisible axis">{songname}</div>\n')
    out.write('</div>\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'song_{fname}_gt\'))">Reference</div>\n')
    out.write(f'<audio id="song_{fname}_gt" controls preload="none">\n')
    out.write(f'<source src="audio/{fname}/Reference Track.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Speakers
    out.write('<div class="mod-container">\n')
    for spk_name in speakers:
        if spk_name == 'Mellotron' and fname == 'song_05':
            out.write('<span class="tooltip">\n')
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'song_{fname}_{spk_name}\'))">{spk_name}</div>\n')
        out.write(f'<audio id="song_{fname}_{spk_name}" controls preload="none">\n')
        out.write(f'<source src="audio/{fname}/{spk_name}.wav" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')
        if spk_name == 'Mellotron' and fname == 'song_05':
            out.write('<span class="tooltiptext">Synthesis Failed</span></span>')
    out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# 15-30
out.write('<div class="sample-container">\n')
out.write('<h2>Comparison of 15 vs 30 duration labels</h2>\n')

songs = ['Singing', 'Rapping']
speakers = ['US_TR_M1', 'US_TR_F1', 'US_TR_F2', 'KO_TR_F1', 'KO_TR_F2', 'US_AD_M1', 'KO_AD_M1']
modict = {
    'withoutPP': 'plain',
    'withPP': 'w/ post-proc'
}

for fname in songs:
    out.write(f'<h3>{fname}</h3>\n')
    out.write('<div class="sample">\n')
    # GT
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'30vs15_song_{fname}_gt\'))">Reference</div>\n')
    out.write(f'<audio id="30vs15_song_{fname}_gt" controls preload="none">\n')
    out.write(f'<source src="audio/30vs15/{fname}/Reference Track.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Speakers
    for moda in ['15', '30']:
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + speakers:
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                out.write(f'<div class="invisible axis">{moda}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'30vs15_song_{fname}_{spk_name}_{moda}\'))">{spk_name}</div>\n')
                out.write(f'<audio id="30vs15_song_{fname}_{spk_name}_{moda}" controls preload="none">\n')
                out.write(f'<source src="audio/30vs15/{fname}/{spk_name}_{moda}.wav" type="audio/wav">\n')
                out.write('Your browser does not support the audio element.\n')
                out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')

out.write('</div>\n')

# Sox no sox
out.write('<div class="sample-container">\n')
out.write('<h2>Assessment of Post-processing (WSOLA)</h2>\n')

songs = ['Singing', 'Rapping']
speakers = ['US_TR_M1', 'US_TR_F1', 'US_TR_F2', 'KO_TR_F1', 'KO_TR_F2', 'US_AD_M1', 'KO_AD_M1']
modict = {
    'withoutPP': 'plain',
    'withPP': 'w/ post-proc'
}

for fname in songs:
    out.write(f'<h3>{fname}</h3>\n')
    out.write('<div class="sample">\n')
    # GT
    out.write('<div class="mod-container">\n')
    out.write('<div class="sample-audio">\n')
    out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'sox_song_{fname}_gt\'))">Reference</div>\n')
    out.write(f'<audio id="sox_song_{fname}_gt" controls preload="none">\n')
    out.write(f'<source src="audio/sox_vs_nonsox/{fname}/Reference Track.wav" type="audio/wav">\n')
    out.write('Your browser does not support the audio element.\n')
    out.write('</audio>\n')
    out.write('</div>\n')
    out.write('</div>\n')
    # Speakers
    for moda in ['withoutPP', 'withPP']:
        out.write('<div class="mod-container">\n')
        for spk_name in ['dum'] + speakers:
            out.write('<div class="sample-audio">\n')
            if spk_name == 'dum':
                out.write(f'<div class="invisible axis">{modict[moda]}</div>\n')
            else:
                out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'sox_song_{fname}_{spk_name}_{moda}\'))">{spk_name}</div>\n')
                out.write(f'<audio id="sox_song_{fname}_{spk_name}_{moda}" controls preload="none">\n')
                out.write(f'<source src="audio/sox_vs_nonsox/{fname}/{spk_name}_{moda}.wav" type="audio/wav">\n')
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
