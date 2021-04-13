function play_audio(url) {
	var audio = $("#audioplay");
	if (!audio.length) {
		$("body").append($("<audio id='audioplay' src='' autoplay></audio>"));
		audio = $("#audioplay");
	} else {
		//Stop any previous audio (just so that it gets a pause event if it is currently playing, so that respective analytics are logged)
		if (!audio[0].ended) audio[0].pause();
	}
	//Before we switch to the new audio file, we give a chance for any 'pause' event to run on the previous audio file
	setTimeout(() => {
		audio.attr("src", url);
	});
}


function get_matching_files(files, regex) {
	return files.filter(file => regex.test(file))
}


function get_param_values(files, regex, match_index='$1', fn_sort=null) {
	return [...new Set(files.filter(file => regex.test(file)).map(file => file.replace(regex, match_index)))].sort()
}


function render_samples_1d(files_, regex) {
	let files = get_matching_files(files_, regex)

	let values1 = [''],
		values2 = get_param_values(files, regex, '$1');

	let nrows = 1,
		ncols = values2.length

	const matrix = new Array(nrows).fill(0).map(() => new Array(ncols).fill(null));

	files.forEach(file => {
		[v1, v2] = file.replace(regex, '||$1').split('||')
		matrix[values1.indexOf(v1)][values2.indexOf(v2)] = file
	})

	let html = []
	
	html.push(`<table class='samples'>`)

	// Render column headers
	html.push('<tr>')
	html.push('<th></th>')
	for (let j in values2) {
		html.push(`<th>${j}</th>`)
	}
	html.push('</tr>')

	for (let i in values1) {
		html.push('<tr>')
		html.push(`<th>${values1[i]}</th>`)
		for (let j in values2) {
			html.push('<td>')
			let file = matrix[i][j]
			html.push(file ? `<span class='audio' src='${file}'>&#9654;</span>` : '-')
			html.push('</td>')
		}
		html.push('</tr>')
	}
	html.push('</table>')

	return html.join('')
}


// function render_samples_2d(files_, regex) {
// 	let files = get_matching_files(files_, regex)

// 	let values1 = get_param_values(files, regex, '$1'),
// 		values2 = get_param_values(files, regex, '$2');

// 	let nrows = values1.length,
// 		ncols = values2.length

// 	const matrix = new Array(nrows).fill(0).map(() => new Array(ncols).fill(null));

// 	files.forEach(file => {
// 		[v1, v2] = file.replace(regex, '$1||$2').split('||')
// 		matrix[values1.indexOf(v1)][values2.indexOf(v2)] = file
// 	})

// 	let html = []
	
// 	html.push(`<table class='samples'>`)

// 	// Render column headers
// 	html.push('<tr>')
// 	html.push('<th></th>')
// 	for (let j in values2) {
// 		html.push(`<th>${j}</th>`)
// 	}
// 	html.push('</tr>')

// 	for (let i in values1) {
// 		html.push('<tr>')
// 		html.push(`<th>${values1[i]}</th>`)
// 		for (let j in values2) {
// 			html.push('<td>')
// 			let file = matrix[i][j]
// 			html.push(file ? `<span class='audio' src='${file}'>&#9654;</span>` : '-')
// 			html.push('</td>')
// 		}
// 		html.push('</tr>')
// 	}
// 	html.push('</table>')

// 	return html.join('')
// }


function render_samples_2d(files_, regex, params=['$1', '$2']) {
	let files = get_matching_files(files_, regex)

	let values1 = get_param_values(files, regex, params[0]),
		values2 = get_param_values(files, regex, params[1]);

	let nrows = values1.length,
		ncols = values2.length

	const matrix = new Array(nrows).fill(0).map(() => new Array(ncols).fill(null));

	files.forEach(file => {
		[v1, v2] = file.replace(regex, `${params[0]}||${params[1]}`).split('||')
		matrix[values1.indexOf(v1)][values2.indexOf(v2)] = file
	})

	let html = []
	
	html.push(`<table class='samples'>`)

	// Render column headers
	html.push('<tr>')
	html.push('<th></th>')
	for (let j of values2) {
		html.push(`<th>${j}</th>`)
	}
	html.push('</tr>')

	for (let i in values1) {
		html.push('<tr>')
		html.push(`<th>${values1[i]}</th>`)
		for (let j in values2) {
			html.push('<td>')
			let file = matrix[i][j]
			html.push(file ? `<span class='audio' src='${file}'>&#9654;</span>` : '-')
			html.push('</td>')
		}
		html.push('</tr>')
	}
	html.push('</table>')

	return html.join('')
}

function isNumeric(str) {
	if (typeof str != "string") return false // we only process strings!  
	return !isNaN(str) && // use type coercion to parse the _entirety_ of the string (`parseFloat` alone does not do this)...
		   !isNaN(parseFloat(str)) // ...and ensure strings of whitespace fail
}

function sort_values(values) {
	// If all values are numeric, sort them as numbers, else use default sorting
	values.sort(values.every(v => isNumeric(v)) ? (a,b) => parseFloat(a)-parseFloat(b) : undefined)
	return values
}


function get_variables(files, regex) {
	let vars = {}
	let matches = []
	let excluded_keys = ['0', 'index', 'input', 'groups']

	files.forEach(file => {
		let match = file.match(regex)
		if (!match) return

		let keys = Object.keys(match).filter(k => !excluded_keys.includes(k))

		let entry = { file }
		for (key of keys) entry[key] = match[key]
		matches.push(entry)

		for (key of keys) {
			if (!(key in vars))
				vars[key] = []
			if (!vars[key].includes(match[key]))
				vars[key].push(match[key])
		}
	})

	for (key in vars)
		vars[key] = sort_values(vars[key])

	return {matches, vars}
}


function render_matches_array(matches, specs) {
	let nspecs = specs.length
	if (nspecs<1 || nspecs>2) {
		alert(`ERROR in render_matches_array(): Only 1 or 2 dimensions can be used, not ${specs.length}.`)
		return
	}

	let values = {}
	specs.forEach(spec => values[spec.match_index]=[])

	let var1, var2
	if (nspecs==1) {
		var1 = '_'
		values['_'] = ['']
		var2 = specs[0].match_index
	}
	else {
		var1 = specs[0].match_index,
		var2 = specs[1].match_index
	}

	matches.forEach(m => {
		([var1, var2]).forEach(v => {
			if (v!='_' && !values[v].includes(m[v]))
				values[v].push(m[v])
		})
	})

	for (key in values) 
		values[key] = sort_values(values[key])

	let nrows = values[var1].length
	let ncols = values[var2].length

	let matrix = new Array(nrows).fill(0).map(() => new Array(ncols).fill(null));

	matches.forEach(m => {
		let i = var1=='_' ? 0 : values[var1].indexOf(m[var1]),
			j = values[var2].indexOf(m[var2])
		matrix[i][j] = m.file
	})


	let html = []
	
	html.push(`<table class='samples'>`)

	// Render column headers
	html.push('<tr>')
	html.push('<th></th>')
	for (let j of values[var2]) 
		html.push(`<th>${j}</th>`)
	html.push('</tr>')

	for (let i in values[var1]) {
		html.push('<tr>')
		html.push(`<th>${values[var1][i]}</th>`)
		for (let j in values[var2]) {
			html.push('<td>')
			let file = matrix[i][j]
			html.push(file ? `<span class='audio' src='${file}'>&#9654;</span>` : '-')
			html.push('</td>')
		}
		html.push('</tr>')
	}
	html.push('</table>')

	return html.join('')
}



function render_samples(files, regex, specs=[{match_index: 1, type: 'section', dict: transcript}, {match_index: 2}]) {
	let { matches, vars } = get_variables(files, regex)

	if (specs.length!=Object.keys(vars).length) 
		alert(`WARNING in render_samples(): Number of specs differs from number of capture groups in regulr exception...`)

	let param_values = specs.map(spec => vars[spec.match_index])

	// return render_matches_array(matches, specs)


	html = []
	if (specs[0].type && specs[0].type=='section') {
		for (let v of param_values[0]) {
			html.push(`<div class='section'>`)
			html.push(`<div class='title'>${v}</div>`)

			if (specs[0].dict && v in specs[0].dict)
				html.push(`<div class='descr'>${specs[0].dict[v]}</div>`)

			html.push(render_matches_array(matches, specs.slice(1)))

			html.push(`</div>`)
		}
	} else {
		html.push(render_matches_array(matches, specs))
	}

	return html.join('')
}


$(document).on("click", ".audio", (ev) => {
	let el = $(ev.target),
		src = el.attr('src')
	play_audio(src);
});


