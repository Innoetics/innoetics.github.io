// η μορφη ειναι: model_speaker_targetlang_uttid
const lang_names = {
	'en': 'American English', 
	'fr': 'French',
	'it': 'Italian',
	'de': 'German',
	'es': 'Spanish',
	'el': 'Greek',
}
const voice_names = {
	'DE-DE-female-2015-v1.0': 'DE Female',
	'ES-SP-female-2014-v1.0': 'ES Female',
	'horan-v1.0': 'KO Female',
	'Stephanie-v94.0': 'EN Female',
	'FR-FR-female-2014-v1.0': 'FR Female'
}


$(document).on('click', '#toc-icon', () => {
	$('#toc').toggle()
})

$(document).on('click', '.toc1,.toc2,.toc3', () => {
	$('#toc').toggle()
})

$(document).on('click', (ev) => {
	if (!$('#toc').is(':visible')) return

	let el = $(ev.target)
	if (el.closest('#menubar').length!=0) return

	$('#toc').toggle()
})

$(document).ready(() => {

	$('#content').append('<h1>1. Cross-Lingual Speaker Adaptation</h1>')
	
	let sections = [
		{speaker: 'karajohn', lang: 'en', heading: '<h2>Seen Adaptation Language</h2>'},
		{speaker: 'aimilios', lang: 'el', heading: '<h2>Unseen Adaptation Language</h2>'},
	]
	for (let section of sections) {
		$('#content').append(`<h2>${section.heading}</h2>`)
		$('#content').append(`<p><b>${lang_names[section.lang]}</b> - Target Speaker ground truth audio: <span class='audio' src='data/${section.speaker}_gt.wav'}>&#9654;</span></p>`)


		let str = `.*${section.speaker}-from-all-(\\d+)_${section.speaker}-ptts_([^_]+)_(\\d+).wav`
		let langs = get_variables(files, new RegExp(str)).vars[2]

		let html = []
		for (let lang of langs) {
			html.push(`<div class='experiment'>`)

			let str = `.*${section.speaker}-from-all-(\\d+)_${section.speaker}-ptts_${lang}_(\\d+).wav`
			let {matches, vars} = get_variables(files, new RegExp(str))

			html.push(`<h3>Target Language: ${lang_names[lang]}</h3>`)

			let utterances = vars[2].map(uttid => `<b>${uttid}</b>: ${transcript[lang+'_'+uttid]}`).join('<br>')
			html.push(`<p>${utterances}</p>`)

			html.push(
				render_matches_array(matches, [{match_index: 1}, {match_index: 2}])
			)				
			html.push(`</div>`)
		}
		
		$('#content').append(html.join(''))	
	}
		


	$('#content').append('<h1>2. Cross-Lingual Text-to-Speech</h1>')
	for (targetlang of ['en', 'fr', 'it', 'de', 'es']) {
		let html = []

		html.push(`<div class='experiment'>`)

		let uttids = get_variables(files, new RegExp(`.*/[^/]+_${targetlang}_([^_/]+)\.wav`)).vars[1]

		let utterances = uttids.map(uttid => `<b>${uttid}</b>: ${transcript[targetlang+'_'+uttid]}`).join('<br>')

		html.push(`<h3><b>Target Language</b>: ${lang_names[targetlang]}</h3>`)
		html.push(`<p>${utterances}</p>`)

		html.push(`<table><tr><th>Training<br>language(s)</th><th>Test<br>voice</th>${uttids.map(uttid => `<th>${uttid}</th>`).join('')}</tr>`)

		let training_langs = get_variables(files, new RegExp(`\.*\/([^_\\d]+)_[^_]+_${targetlang}_[^_\/]+.wav`)).vars[1]
		for (let idx_training_lang in training_langs) {
			training_lang = training_langs[idx_training_lang]

			let voices = get_variables(files, new RegExp(`\.*\/${training_lang}_([^_]+)_${targetlang}_[^_\/]+.wav`)).vars[1]
			for (let idx_voice in voices) {
				let voice = voices[idx_voice]
				html.push(`<tr><td>${idx_voice=='0' ? `<b>${training_lang}</b>` : ''}</td><td>${voice_names[voice]}</td>`)
				
				let matches3 = get_variables(files, new RegExp(`\.*\/${training_lang}_${voice}_${targetlang}_([^_\/]+).wav`)).matches
				for (let uttid of uttids) {
					let _files = matches3.filter(m => m.file.indexOf(`/${training_lang}_${voice}_${targetlang}_${uttid}.wav`)!=-1).map(m => m.file)
					html.push(`<td>${_files.length>0 ? `<span class='audio' src='${_files[0]}'>&#9654;</span>` : ''}</td>`)
				}
				html.push('</tr>')
			}
		}
		html.push('</table>')
		html.push('</div>')

		$('#content').append(html.join(''))
	}
	


	// Dynamically generate a TOC
	let toc_html = []
	$('h1,h2,h3').each((idx, el_) => {
		let el = $(el_)
		el.html(`<a class='offset-anchor' id='heading_${idx}'></a>${el.html()}`)
		toc_html.push(`<div class='${el[0].localName.replace('h', 'toc')}'><a href='#heading_${idx}'>${el.text()}</a></div>`)
	})

	$('#toc').html(toc_html.join(''))

})

