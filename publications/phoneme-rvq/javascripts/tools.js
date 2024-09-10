//---------------------------------------------------------------------------------------------------
//
//---------------------------------------------------------------------------------------------------
const product = (param_name1, param_values1, arr) => param_values1.map((v1) => arr.map((obj) => ({ [param_name1]: v1, ...obj }))).flat();

/*
$(document).on("click", ".audio", (ev) => {
	let el = $(ev.target);
	// let src = el.attr('src');

	let expid = el.attr("experiment-id");
	let experiment_config = experiment_config_all[expid];

	let param_values = experiment_config.params.reduce((acc, p) => ({ ...acc, [p]: el.attr(`data-param-${p}`) }), {});
	// let src = `/api/listening-tests/file/${params_to_wav(experiment_config, param_values)}`;
	let src = params_to_wav(experiment_config, param_values);
	play_audio(src);
});

function params_to_wav(experiment_config, param_values) {
	// First try to see if 'experiment_config.wav_path_mapper' is actually function code
	let template = experiment_config.wav_path_mapper;
	try {
		template = eval(`(${experiment_config.wav_path_mapper})(${JSON.stringify(param_values)})`);
	} catch (ex) {}

	return mustache.render(template, param_values);
}
*/

$(document).on("click", ".audio", (ev) => {
	let elem = $(ev.target)
	play_audio(elem.attr('url'));
});

function find_changed_row_params(experiment_config, params1, params2) {
	let params = experiment_config.params_rows.slice().reverse();
	while (params.length && params1[params[0]] == params2[params[0]]) params.shift();
	return params.reverse();
}

function render_table(experiment_config, render_cell) {
	// Prepare all combination of the row values
	let row_values = [{}],
		col_values = [{}];
	for (p of experiment_config.params_rows) row_values = product(p, experiment_config.param_values[p], row_values);
	for (p of experiment_config.params_cols) col_values = product(p, experiment_config.param_values[p], col_values);

	let row_param_levels = experiment_config.params_rows.length - 1;

	return `
		<table class="samples">
			<tr>
				<th rowspan='${experiment_config.params_cols.length}' style="text-align: left; vertical-align: bottom;">${experiment_config.params_rows
			.slice()
			.reverse()
			.map((p, i) => `<span class="param_name" style="margin-left: ${i}em;">${p} <span class="arrow">&darr;</span></span>`)
			.join("<br>")}</th>
				${experiment_config.params_cols
			.map((cp, ip) => {
				let repeats = experiment_config.params_cols.slice(ip + 1).reduce((acc, cur) => acc * experiment_config.param_values[cur].length, 1);
				let spans = experiment_config.params_cols.slice(0, ip).reduce((acc, cur) => acc * experiment_config.param_values[cur].length, 1);
				let values = [];
				for (let i = 0; i < repeats; i++) values = values.concat(experiment_config.param_values[cp]);
				return (
					values.map((v) => `<th class='col-header' colspan='${spans}'>${v}</th>`).join("") +
					`<th style='text-align: left;'><span class="param_name"><span class="arrow">&larr;</span> ${cp}</span></th>`
				);
			})
			.reverse()
			.join("</tr><tr>")}
			</tr>
			${row_values
			.map((rvs, ir) => {
				let changed_params = find_changed_row_params(experiment_config, ir > 0 ? row_values[ir - 1] : [], row_values[ir]);
				return (
					changed_params
						.slice(1)
						.reverse()
						.map((p, i) => `<tr><th class='row-header' data-level='${row_param_levels - (changed_params.length - i) + 1}'>${rvs[p]}</th></tr>`)
						.join("") +
					`<tr>
							<th class='row-header deepest' data-level='${row_param_levels}'>${rvs[experiment_config.params_rows[0]]}</th>
							${col_values.map((cvs) => `<td>${render_cell({ ...rvs, ...cvs })}</td>`).join("")}
						</tr>`
				);
			})
			.join("")}
		</table>`;
}

function render_select(param, classname = null, selected_idx = 0) {
	let param_values = experiment_config.param_values[param];
	return `
		<span class="param_name" data-param-name="${param}">${param}</span><br>
		<select ${classname ? `class="${classname}"` : ``} data-param-name="${param}">
			${param_values.map((o, idx) => `<option value='${o}' ${idx == selected_idx ? "selected" : ""}>${o}</option>`).join("")}
		</select>`;
}

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

//----------------------------------------------------------
// Handlers of 'dropdown_2d' template elements
//----------------------------------------------------------
function render_page_dropdown_2d(expid, experiment_config, $el) {
	$el.html(
		// `<div class="section">` +
		// 	experiment_config.params_fixed
		// 		.map(
		// 			(param) =>
		// 				`<div class="container">
		// 					${render_select(param, "dropdown_2d__select")}
		// 				</div>`
		// 		)
		// 		.join("") +
		// 	`</div>
		// <div class="section">
		// 	<div class='dropdown_2d__table container'></div>
		// </div>`
		`
		<div class="section">
			<div class='dropdown_2d__table container'></div>
		</div>
		`
	);

	render_main_content_dropdown_2d(expid, experiment_config, $el);

	// Trigger 'change' event for all fixed variables
	$el.find(".dropdown_2d__select").each((idx, el) => {
		$(el).trigger("change");
	});
}

function render_main_content_dropdown_2d(expid, experiment_config, $el) {
	let fixed_param_values = {};

	experiment_config.params_fixed.forEach((p) => {
		fixed_param_values[p] = $(`.dropdown_2d__select[data-param-name="${p}"]`).find(":selected").val();
	});

	$el.find(".dropdown_2d__table").fadeToggle(100, () => {
		$el.find(".dropdown_2d__table").html(
			render_table(experiment_config, (v) => {
				let param_values = {
					...fixed_param_values,
					...v,
				};

				let title = "";
				try {
					title = htmlEntities(
						`<div style='text-align: left'>` +
						experiment_config.params
							.slice()
							.sort()
							.map((p) => `<b>${p}</b>: ${param_values[p]}`)
							.join("<br>") +
						`</div>`
					);
				} catch (ex) {
					console.log(ex);
				}
				return `
					<span class="audio"
						${experiment_config.params.map((p) => `data-param-${p}="${param_values[p]}"`).join(" ")}
						experiment-id="${expid}"
						title="${title}"
					>▶</span>`;
			})
		);
		$el.find(".dropdown_2d__table").fadeToggle(100, () => {
			tippy("[title]");
		});
	});
}

$(document).on("click", ".resizeable-image", (ev) => {
	let el = $(ev.target);
	el.toggleClass("full-width-image");
});
