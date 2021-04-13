import os
import json

root_folder = 'data'

#-------------------------------------------------------------------------------
# Prepare the 'files.js' file with all the content files
#-------------------------------------------------------------------------------
def get_subfolder_contents(folder):
	contents = []
	for root, dirs, files in os.walk(folder):
		contents.extend([os.path.join(root, file) for file in files])
	return contents

#-------------------------------------------------------------------------------
# Prepare any corpus files in .js form
#-------------------------------------------------------------------------------
def convert_corpus_to_js(corpus_file, js_file, varname='corpus'):
	corpus = {}
	with open(corpus_file, 'r', encoding="utf8") as fp:
		for line in fp:
			line = line.strip()
			if len(line)==0: continue

			parts = line.split('|')
			uttid = parts[0].replace('.wav', '')
			content = '|'.join(parts[1:])

			corpus[uttid] = content

	with open(js_file, 'w') as fp:
		fp.write(f'let {varname} = '+json.dumps(corpus, indent=4))


#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------

contents = get_subfolder_contents(root_folder)
# This is for Windows
contents = list(map(lambda f: f.replace('\\', '/'), contents))
with open('files.js', 'w') as fp:
	fp.write( 'let files = ' + json.dumps(contents, indent=4) )


convert_corpus_to_js(corpus_file='data/transcript.txt', js_file='transcript.js', varname='transcript')