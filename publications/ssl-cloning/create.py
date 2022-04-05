import os
from os import listdir
from os.path import isfile, join
import re

os.system('cat template.html > index.html')
out = open('index.html', 'a')
#bench_1400_0001_len10 -> test_sentence_1
#bench_1400_0002_len8 -> test_sentence_2
#bench_1400_0003_len4 -> test_sentence_3
#bench_1400_0004_len13 -> test_sentence_4
#bench_1400_0026_len12  -> test_sentence_5
#bench_1400_0013_len7 -> test_sentence_6
#bench_1400_0015_len8 -> test_sentence_7
text_corpus = "transcript.txt"

with open(text_corpus) as f:
    transcript = {line.rstrip().split('#')[0].rstrip(): line.rstrip().split('#')[1].lstrip() for line in f}

# with open('corpus_full.txt') as f:
#     temp = [x.rstrip().split('\t') for x in f]
#     transcript = {line[0]: line[1] for line in temp}

audio_path = "audios"
all_files = os.listdir(audio_path)

clean_sentences = [f for f in all_files if 'reg' in f]
noisy_sentences = [f for f in all_files if 'extra' in f and f[0:3] !='aws']
ref_sents = [f for f in all_files if f[0:3] == 'aws']

#exp_names = list(set([f.split("-")[0] for f in clean_sentences]))
exp_names_dic = {'vctk_non_attentive_plain': 'BYOL-A', 'vctk_non_attentive_augms_half_less_sems': 'BYOL-A + Pros', 'vctk_non_attentive_all_noises' : "BYOL-A + Noise", "vctk_non_attentive_one_with_everything_half_less_sems":"BYOL-A + Pros + Noise",
                  'd_vectors_vctk': "d-vectors VCTK", 'd_vectors_vox': "d-vectors Vox"}
exp_names = list(exp_names_dic.keys())
clean_fnames = list(set([f.split("-")[-1].replace('.wav', '') for f in clean_sentences]))
out.write('<h2>Voice Cloning from unseen clean utterances. </h2>\n')


#out.write('<div class="sample-container" style="display:none">\n')
for fname in clean_fnames:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')

    clean_sents_fname = [f for f in clean_sentences if fname in f]
    spks = list(set([f.split('-')[2] for f in clean_sents_fname]))

    for spk in spks:     
        ref_fname = [f for f in ref_sents if spk in f][0]
        out.write('<div class="mod-container">\n')
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'{ref_fname}\'))">Reference Speaker</div>\n')
        out.write(f'<audio id="{ref_fname}" controls preload="none">\n')
        out.write(f'<source src="{audio_path}/{ref_fname}" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')

        out.write('<div class="mod-container">\n')
        for exp in exp_names:
            exp_fname = [f for f in clean_sents_fname if spk in f and exp in f][0]
            exp_name = exp_names_dic[exp]
            out.write('<div class="sample-audio">\n')
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'{exp_fname}\'))">{exp_name}</div>\n')
            out.write(f'<audio id="{exp_fname}" controls preload="none">\n')
            out.write(f'<source src="{audio_path}/{exp_fname}" type="audio/wav">\n')
            out.write('Your browser does not support the audio element.\n')
            out.write('</audio>\n')
            out.write('</div>\n')
        out.write('</div>\n')
        out.write('</div>\n')
    out.write('</div>\n')
#out.write('</div>\n')

noisy_fnames = list(set([f.split("-")[-1].replace('.wav', '') for f in noisy_sentences]))
out.write('<h2>Voice Cloning from unseen noisy utterances with SNR 5. </h2>\n')

for fname in noisy_fnames:
    out.write('<div class="sample">\n')
    out.write('<div class="sample-title">\n')
    out.write('<span class="quotation">&ldquo;</span>\n')
    out.write('<div class="transcript">')
    out.write(transcript[fname])
    out.write('</div>\n')
    out.write('</div>\n')

    noisy_sents_fname = [f for f in noisy_sentences if fname in f]
    spks = list(set([f.split('-')[2] for f in noisy_sents_fname]))

    for spk in spks:     
        ref_fname = [f for f in ref_sents if spk in f][0]
        out.write('<div class="mod-container">\n')
        out.write('<div class="sample-audio">\n')
        out.write(f'<div class="gt" onclick="togglePlay(document.getElementById(\'{ref_fname}\'))">Reference Speaker</div>\n')
        out.write(f'<audio id="{ref_fname}" controls preload="none">\n')
        out.write(f'<source src="{audio_path}/{ref_fname}" type="audio/wav">\n')
        out.write('Your browser does not support the audio element.\n')
        out.write('</audio>\n')
        out.write('</div>\n')

        out.write('<div class="mod-container">\n')
        for exp in exp_names:
            exp_fname = [f for f in noisy_sents_fname if spk in f and exp in f][0]
            exp_name = exp_names_dic[exp]
            out.write('<div class="sample-audio">\n')
            out.write(f'<div class="r-number" onclick="togglePlay(document.getElementById(\'{exp_fname}\'))">{exp_name}</div>\n')
            out.write(f'<audio id="{exp_fname}" controls preload="none">\n')
            out.write(f'<source src="{audio_path}/{exp_fname}" type="audio/wav">\n')
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
