const token_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];

let experiment_specific_data = {};
// experiment_specific_data["experiment-isolated-word"]

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

$(document).on("click", "#play-audio", (ev) => {
	let exp_name = $(ev.target).closest(".experiment").attr("data-experiment-name");
	play_audio(experiment_specific_data[exp_name].current_audio);
});

$(document).on("click", ".experiment-link", (ev) => {
	let el = $(ev.target);
	let exp_id = el.attr("data-experiment");

	// $(`[data-experiment-id='${exp_id}']`)[0].scrollIntoView(true);
	$([document.documentElement, document.body]).animate(
		{
			scrollTop: $(`[data-experiment-id='${exp_id}']`).offset().top - $(`#menus`).height() - 40,
		},
		500
	);
});

$(document).on("click", ".inline-menu-item", (ev) => {
	let el = $(ev.target);
	el.parent().find(".inline-menu-item").removeClass("selected");
	el.addClass("selected");
});

$(document).on("click", ".utt_id", (ev) => {
	let el = $(ev.target);
	let exp_name = $(ev.target).closest(".experiment").attr("data-experiment-name");
	experiment_specific_data[exp_name].utt_id = el.attr("data-utt-id");
	$(`[data-experiment-name='${exp_name}'] .menu-words`).html(
		Object.keys(data.gifs[experiment_specific_data[exp_name].utt_id])
			.filter(
				(word) =>
					(exp_name == "experiment-isolated-word" && word != "-1") ||
					(exp_name == "experiment-all-words" && word == "-1")
			)
			.map((word) => `<span class='word_id inline-menu-item' data-word='${word}'>${word}</span>`)
			.join("")
	);
	$(`[data-experiment-name='${exp_name}'] .menu-words .word_id:first`).trigger("click");
});

$(document).on("click", ".word_id", (ev) => {
	let el = $(ev.target);
	let exp_name = $(ev.target).closest(".experiment").attr("data-experiment-name");
	experiment_specific_data[exp_name].word_id = el.attr("data-word");
	let tokens = Object.keys(
		data.gifs[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id]
	);
	tokens.sort((a, b) => parseInt(a) - parseInt(b));
	$(`[data-experiment-name='${exp_name}'] .menu-tokens`).html(
		tokens.map((token) => `<span class='token_id inline-menu-item' data-token='${token}'>${token}</span>`).join("")
	);
	$(`[data-experiment-name='${exp_name}'] .menu-tokens .token_id:first`).trigger("click");
});

$(document).on("click", ".token_id", (ev) => {
	let el = $(ev.target);
	let exp_name = $(ev.target).closest(".experiment").attr("data-experiment-name");
	let token_id = el.attr("data-token");
	experiment_specific_data[exp_name].token_id = token_id;

	let values = Object.keys(
		data.audios[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id][token_id]
	);
	values.sort((a, b) => parseFloat(a) - parseFloat(b));

	experiment_specific_data[exp_name].values = values;

	// If there was already some value, preserve it
	let prev_v = null;
	if ($(`[data-experiment-name='${exp_name}'] #audio-files-range`).length)
		prev_v = $(`[data-experiment-name='${exp_name}'] #audio-files-range`).get()[0].value;

	let max_value = values.slice(-1)[0],
		min_value = values[0];

	$(`[data-experiment-name='${exp_name}'] .content`).html(`
		<div style="margin-bottom: 1em;">
			Weight change for Token #<b>${token_id}</b>: <span class="token-weight"></span><img id="play-audio" src='images/play.png'>
			<span class='range left'>${min_value}</span>
			<span class='range right'>${max_value}</span>
			<div class='colorbar'>
				<input id="audio-files-range" type="range" min="0" max="${values.length - 1}" style="cursor: hand; width:100%">
			</div>
		</div>

		<img class='image' src='${
			data.gifs[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id][token_id]
		}' data-mfp-src='${
		data.gifs[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id][token_id]
	}'></img>
			<img class='image' src='${
				data.pitches[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id][
					token_id
				]
			}' data-mfp-src='${
		data.pitches[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id][token_id]
	}'></img>
	`);

	if (prev_v != null && prev_v >= 0 && prev_v <= values.length - 1)
		$(`[data-experiment-name='${exp_name}'] #audio-files-range`).get()[0].value = prev_v;

	$(`[data-experiment-name='${exp_name}'] .content .image`).magnificPopup({ type: "image" });

	setTimeout(() => {
		$(`[data-experiment-name='${exp_name}'] #audio-files-range`).trigger("change");
	}, 100);
	$(`[data-experiment-name='${exp_name}'] #audio-files-range`).focus();
});

$(document).on("change", "#audio-files-range", (ev) => {
	let v = ev.target.value;
	let exp_name = $(ev.target).closest(".experiment").attr("data-experiment-name");
	let token_id = experiment_specific_data[exp_name].token_id,
		value = experiment_specific_data[exp_name].values[v];
	$(`[data-experiment-name='${exp_name}'] .token-weight`).html(value);
	experiment_specific_data[exp_name].current_audio =
		data.audios[experiment_specific_data[exp_name].utt_id][experiment_specific_data[exp_name].word_id][token_id][
			value
		];
	play_audio(experiment_specific_data[exp_name].current_audio);
});

$(document).ready(() => {
	// Here, we assume that the data have already been loaded and is available in the 'data' object

	$("#main").append(`
		<!--

		<div class='experiment'>
			<h1>
				<span class="experiment-num"></span>
				<span class="subtitle">Model Evaluation</span><br>
				Subjective comparative evaluation of the model
			</h1>
			<p><span class='notes'>Pick pairs for comparison of Word-Style-Token vs Plain Non-attentive Tacotron. This would demonstrate the overall quality and the role of the Prior Encoder.</span></p>
			<p><span class='notes'>We must also include in the MOS, samples from sentences with altered style token weights (either for isolated words or for all the words), so that we can check whether they receive a (significantly) lower score than the unmodified ones. If not, then this means that the model offers effective style manipulation capabilities without significantly degrading the quality of the generated audio.</span></p>
			<p><span class='notes'>Run MOS on Mechanical Turk (also include ground-truth samples?).</span></p>
		</div>

		<div class='experiment'>
			<h1>
				<span class="experiment-num"></span>
				<span class="subtitle">Model Evaluation</span><br>
				Objective assessment of the model's generative behavior
			</h1>
			${
				`<table><tr>` +
				data["stats"]
					.slice(1)
					.map(
						(f, i) =>
							`<td style="width:33% !important; text-align: center;"><img class="image" style="width:100%" src="${f}" data-mfp-src="${f}"><br>Figure ${
								i + 1
							}</td>`
					)
					.join("") +
				`</tr></table>`
			}
			<p>The generative behavior of three models has been examined in terms of the acoustic properties of their generated audio files:
				<ol>
					<li>Plain non-attentive Tacotron model without any extra component for modeling styles;</li>
					<li>Non-attentive model including the Prior Encoder; and</li>
					<li>Non-attentive model including the Prior Encoder as well as the Word Linguistic Encoder</li>
				</ol>
			</p>
			<p>
				The properties examined were pitch and durations, which are essential parts of prosody. 
				More specifically, a Test Set of 1.000 utterances has been selected, which were not included in the training set, and inference was performed using each of these models.
				The generated audio files were then analyzed as follows:
				<ul>
					<li>An acoustic model has been trained on the full dataset, and descriptive statistics (mean and std) were extracted regarding phoneme durations for each phoneme class.</li>
					<li>The acoustic model was used to extract phoneme boundaries for all generated files through forced-alignment. This provided information for the phoneme durations which were then z-normalized using the statistics of the full dataset (subtracted mean value and divided by standard deviation for each phoneme class).</li>
					<li>The distribution of these normalized duration values for all phonemes in each of the three generated datasets is shown in Figure 1. The diffrent modes that are present in the distribution may be related to the fact that the alignment process used to calculate durations (both for preparing the training data and for analyzing the generated audio files) used 10 msec analysis frames, leading to all durations being quantized to multiples of 10 msec.</li>
					<li>The pitch contours of all generated files were calculated on a frame basis (excluding unvoiced frames). These were used to calculate the distributions of: (a) these raw values (Figure 2); as well as (b) the standard deviation of pitch per audio file (Figure 3)</li>
				</ul>
			</p>
			<p>Kernel-density estimation (KDE) was used to estimate each of the distributions above, using Gaussian kernels and empirically selected bandwidths in each case.</p>
			<p>
				As evident from the above figures:
				<ul>
					<li>The phoneme durations (Figure 1) in audio generated by models 2 and 3 which include style-related components are similar to those of the plain model 1. The right side of the distributions indicate that the plain model has a slighlty higher tendency to generate longer durations than the other models.</li>
					<li>The style-aware models 2 and 3 tend to generate speech with pitch spanning a higher range (Figure 2). Model 3 even more so compared to Model 2.</li>
					<li>The style-aware models 2 and 3 tend to generate higher pitch variation within each generated utterance (Figure 3). Model 3 even more so compared to Model 2.</li>
				</ul>
			</p>
			<p>These indicate that the style-aware models tend to generate richer pitch patterns than the plain model. This behavior may be partly attributed to the larger size of these models and their, thus, increased modeling capacity.</p>
		</div>

		<div class='experiment'>
			<h1>
				<span class="experiment-num"></span>
				<span class="subtitle">Robustness</span><br>
				Measuring the robustness of the model against known Tacotron issues
			</h1>
			<p><span class='notes'><span class='who'>Nikos</span> Perform ASR on synthesized utterances (using Kaldi) and calculate error rate at phoneme level. Then calculate "Unaligned duration ration (UDR)" (but on phonemes) and "Word Duration Ratio" (WDR)</span></p>
		</div>

		-->

		<div class='experiment' data-experiment-name='experiment-isolated-word'>
			<h1>
				<span class="experiment-num"></span>
				<span class="subtitle">Style Control</span><br>
				Direct manipulation of isolated word style token weights
			</h1>
			<p>In this experiment, the style token weights calculated by the Prior Encoder are used as baseline for all the words in a sentence. The weights of the second word's tokens are then progressively changed, one by one. Each image shows the effects of changing the <i>i</i>-th token's weight by adding to it a value in the interval [-0.075, 0.075].</p>
			<p>The image on the left shows how the MEL spectrum and pitch are affected as different values are added to the respective token for the second word. The image on the right shows the corresponding pitch contours. The pitch contours are not time-aligned, so that any changes in duration can be clearly observed. The colorbar shows which contour corresponds to which value added to the style token weight.
			<p>As shown, some style tokens (e.g. Token #10) are more tailored to altering the pitch (mean value, range and pattern) of the affected word, while others (e.g. Token #1) are more clearly affecting the word's duration. It should be noted that, in some cases, the models may also rearrange the pitch of the neighboring words which are not directly manipulated.
			Finally, some of the tokens (e.g. Token #4) seem to cause more composite changes, such as changing the spectral tilt or distribution of energy between higher/lower frequency bands. For instance, for Token #4, notice in the spectrogram the energy in high frequencies for the affected word.</p>
			<div style="border: 1px solid #eee;">
				<div class='menubar'>
					<div class='menu-utt-ids'></div>
					<div class='menu-words'></div>
					<div class='menu-tokens'></div>
				</div>
				<div class='content'>
				</div>
			</div>
		</div>

		<div class='experiment' data-experiment-name='experiment-all-words'>
			<h1>
				<span class="experiment-num"></span>
				<span class="subtitle">Style Control</span><br>
				Combined direct manipulation of all words' style token weights in a sentence
			</h1>
			<p>Same as previous samples, but now manipulating simlultaneously all the words of a sentence. In each case, the exact same changes are applied to the respective token weights of all the words.</p>
			<div style="border: 1px solid #eee;">
				<div class='menubar'>
					<div class='menu-utt-ids'></div>
					<div class='menu-words'></div>
					<div class='menu-tokens'></div>
				</div>
				<div class='content'>
				</div>
			</div>
		</div>

		<!--
		<div class='experiment'>
			<h1>
				<span class="experiment-num"></span>
				<span class="subtitle">Style transfer</span><br>
				Transferring word style token weights across sentences
			</h1>
			<p><span class='notes'><span class='who'>Konstantinos</span> Pick some examples of relatively successful transfers.</span></p>
		</div>
		-->

	`);

	// Initialize experiment-specific data
	$(".experiment[data-experiment-name]").each((idx, _el) => {
		let el = $(_el);
		let name = el.attr("data-experiment-name");
		experiment_specific_data[name] = {};
	});

	// Initialize page menus to select experiment
	$(".experiment").each((idx, el) => {
		$("#menus").append(`<a class="experiment-link menu-item" data-experiment="${idx + 1}">${idx + 1}</a>`);
	});

	$(".experiment").each((idx, _el) => {
		let el = $(_el);
		el.attr("data-experiment-id", idx + 1);
		el.find(".experiment-num").html(idx + 1);
	});

	// Inintialize the magnificPopup library
	$(".image").magnificPopup({ type: "image" });

	// Load data for isolated word experiment
	$(".menu-utt-ids").html(
		Object.keys(data.gifs)
			.map((uttid) => `<span class='utt_id inline-menu-item' data-utt-id='${uttid}'>${uttid}</span>`)
			.join("")
	);
	$(`[data-experiment-name='experiment-isolated-word'] .menu-utt-ids .utt_id:first`).trigger("click");

	$(`[data-experiment-name='experiment-all-words'] .menu-utt-ids .utt_id:first`).trigger("click");


	$(window).scrollTop( 0 )

	// Load data for all-word experiment
});
