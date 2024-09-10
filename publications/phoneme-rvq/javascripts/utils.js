const sp_sil = ['sp', 'sil'];
const gr_punctuation = [',', '.', '?', '!'];

const no_value = 1e10;
const punctuation = ['sil', 'sp'].concat(',.?!'.split(''));

function is_bool_true(value) {
	return (typeof value !== 'undefined') && !(value === false || value === 0 || value === '0' || value === 'False' || value === 'false' || value === 'FALSE');
}

function stringify(json, level = 0, maxchars = 1000) {
	let prefix = new Array(level).fill('\t');
	return (
		prefix +
		'{\n' +
		Object.keys(json)
			.map((key) => {
				let line = JSON.stringify(json[key]) || 'undefined';
				if (line.length > maxchars) line = line.slice(0, -(line.length - maxchars)) + '...';
				return `${prefix}\t"${key}": ${line}`;
			})
			.join(',\n') +
		prefix +
		'}\n'
	);
}

/*
Timing function.
Call it once at the beginning and once at the end. It will return the difference (in msec).
*/
var timer_t = new Date().getTime();
function timer() {
	var end = new Date().getTime();
	var dt = end - timer_t;
	timer_t = end;
	return dt;
}

// 'timeStart', 'timeEnd' are Date objects as returned by new Date()
function time_duration(timeStart, timeEnd) {
	return msec_to_duration(timeEnd - timeStart);
}

function msec_to_duration(dt) {
	// get total seconds between the times
	var delta = Math.abs(dt) / 1000;

	// calculate (and subtract) whole days
	var days = Math.floor(delta / 86400);
	delta -= days * 86400;

	// calculate (and subtract) whole hours
	var hours = Math.floor(delta / 3600) % 24;
	delta -= hours * 3600;

	// calculate (and subtract) whole minutes
	var minutes = Math.floor(delta / 60) % 60;
	delta -= minutes * 60;

	// what's left is seconds
	var seconds = Math.round(delta % 60); // in theory the modulus is not required

	const parts = { d: days, h: hours, m: minutes, s: seconds };
	let nonzero = false;
	return Object.keys(parts)
		.map((key) => {
			let value = parts[key];
			if (value > 0) {
				nonzero = true;
				return `${value}${key}`;
			} else {
				return nonzero ? `00${key}` : ``;
			}
		})
		.filter((p) => p.length)
		.join(':');
}

function sec_to_hours(delta) {
	// calculate (and subtract) whole hours
	var hours = Math.floor(delta / 3600);
	delta -= hours * 3600;

	// calculate (and subtract) whole minutes
	var minutes = Math.floor(delta / 60) % 60;
	delta -= minutes * 60;

	// what's left is seconds
	var seconds = Math.round(delta % 60); // in theory the modulus is not required

	const parts = { h: hours, m: minutes, s: seconds };
	let nonzero = false;
	return Object.keys(parts)
		.map((key) => {
			let value = parts[key];
			if (value > 0) {
				nonzero = true;
				return `${value}${key}`;
			} else {
				return nonzero ? `00${key}` : ``;
			}
		})
		.filter((p) => p.length)
		.join(':');
}

function rgba_from_val(val, stats, symmetric) {
	var cutoff_threshold = 4; //!!!!!!!!!!!!!!!!!!!

	val = (val - stats.mode) / (val < stats.mode ? stats.stdl : stats.stdr) / 4;

	if (symmetric == 0 && val > 0) val = 0;

	//return {red: (val<0 ? 0 : 255), green: 0, blue: (val<0 ? 255 : 0), alpha: Math.abs(val)};
	return Math.abs(val) >= 1 ? { red: 255, green: 0, blue: 0, alpha: 1 } : { red: 237, green: 125, blue: 49, alpha: Math.abs(val) };
}

function rgba_from_val2(val, max) {
	var rgba = { red: 237, green: 125, blue: 49, alpha: Math.abs(val / max) };
	return 'rgba(' + rgba.red + ',' + rgba.green + ',' + rgba.blue + ',' + rgba.alpha + ')';
}

//Trim starting and ending quotes
function trim_double_quotes(str) {
	return str.replace(/(^")|("$)/g, '');
}

const mapHtmlEntities = {
	'&': '&amp;',
	'<': '&lt;',
	'>': '&gt;',
	'"': '&quot;',
	"'": '&#039;',
	'\\': '&#92;',
	'/': '&#47;',
};
var regexpHtmlEntities = new RegExp('[' + escapeRegExp(Object.keys(mapHtmlEntities).join('')) + ']', 'g');
function htmlEntities(str) {
	return String(str).replace(regexpHtmlEntities, function (m) {
		return mapHtmlEntities[m];
	});
	//return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

//E.g. see: https://stackoverflow.com/questions/42068/how-do-i-handle-newlines-in-json
function jsonEscape(str) {
	return str.replace(/\n/g, '\\\\n').replace(/\r/g, '\\\\r').replace(/\t/g, '\\\\t');
}

var msg_t0 = new Date();
function msg(s, include_in_the_output, append_to_previous) {
	if (typeof include_in_the_output == 'undefined') include_in_the_output = true;
	if (typeof append_to_previous == 'undefined') append_to_previous = false;

	$('#msg').html(s);
	if (include_in_the_output) {
		if (append_to_previous) $('#output p:first').html($('#output p:first').html() + s);
		else {
			var now = new Date();
			now = new Date(now - msg_t0);
			var time =
				'<b>[' +
				('0' + now.getHours()).slice(-2) +
				':' +
				('0' + now.getMinutes()).slice(-2) +
				':' +
				('0' + now.getSeconds()).slice(-2) +
				'.' +
				('00' + now.getMilliseconds()).slice(-3) +
				']</b> ';
			$('#output').prepend("<p style='display:none; background-color: rgba(0,0,0,0.1);'>" + time + s + '</p>');
			$('#output>p:first').slideToggle('fast', function () {
				$(this).css('background-color', 'transparent').css('color', 'black');
			});
		}
	}
}

function nonempty(s) {
	return typeof s !== 'undefined' && s !== false ? s : '';
}

let audiotracker = {
	src: null,
	range: null,
	handler: (event) => {
		let audio = event.target;
		let played = audio.played;
		// Events that provide TimeRanges
		if (played.length && ['timeupdate', /*"ended",*/ 'pause'].includes(event.type)) {
			audiotracker.range = [played.start(played.length - 1), played.end(played.length - 1)];
			audiotracker.src = audio.src;
		}

		// Events that signify the end of playback
		if (audiotracker.range && [/*"ended",*/ 'abort', 'pause'].includes(event.type)) {
			audiotracker.event();
			audiotracker.range = null;
		}
	},

	hook: (elem) => {
		'abort,canplay,change,ended,pause,play,playing,progress,seeked,suspend,timeupdate,waiting'.split(',').forEach((event_type) => {
			elem.addEventListener(event_type, audiotracker.handler, false);
		});
	},

	event: () => {
		const url = new URL(audiotracker.src, `${window.location.protocol}//${window.location.hostname}`);
		const components = url.pathname.split('/');
		let obj = null;

		switch (components.slice(-1)[0]) {
			case 'audio':
				obj = {
					project: components.slice(-3, -2)[0],
					textgrid: components.slice(-2, -1)[0],
					from: audiotracker.range[0],
					to: audiotracker.range[1],
				};
				break;
			case 'audioseg':
				let from = parseFloat(url.searchParams.get('from'));
				obj = {
					project: components.slice(-3, -2)[0],
					textgrid: components.slice(-2, -1)[0],
					from: from + audiotracker.range[0],
					to: from + audiotracker.range[1],
				};
				break;
			default:
				// Probably TTS
				obj = {
					project: window.location.pathname.split('/').slice(-1)[0],
					textgrid: '[TTS]',
					from: audiotracker.range[0],
					to: audiotracker.range[1],
				};
				break;
		}
		obj.type = 'listen';
		// console.log(JSON.stringify(obj))
		fetch('/api/project/action', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ action: obj }) });
	},
};

function play_audio(url) {
	var audio = $('#audioplay');
	if (!audio.length) {
		$('body').append($("<audio id='audioplay' src='' autoplay></audio>"));
		audio = $('#audioplay');
		audiotracker.hook(audio[0]);
	} else {
		//Stop any previous audio (just so that it gets a pause event if it is currently playing, so that respective analytics are logged)
		if (!audio[0].ended) audio[0].pause();
	}
	//Before we switch to the new audio file, we give a chance for any 'pause' event to run on the previous audio file
	setTimeout(() => {
		audio.attr('src', url);
	});
}

function play_audio_plain(url) {
	var audio = $('#audioplay');
	if (!audio.length) {
		$('body').append($("<audio id='audioplay' src='' autoplay></audio>"));
		audio = $('#audioplay');
	} else {
		//Stop any previous audio (just so that it gets a pause event if it is currently playing, so that respective analytics are logged)
		if (!audio[0].ended) audio[0].pause();
	}
	//Before we switch to the new audio file, we give a chance for any 'pause' event to run on the previous audio file
	setTimeout(() => {
		audio.attr('src', url);
	});
}

function stop_audio() {
	var audio = $('#audioplay');
	if (!audio.length) return;
	audio.attr('src', '');
}

//Convert a version string into a float number (for sorting)
function ver2num(v) {
	if (!v) return 0;
	var num = 0,
		mul = 1;
	v.split('.').forEach(function (val) {
		num += mul * val;
		mul /= 1000;
	});
	return num;
}

function compareVersionNumbers(a, b) {
	if (a < b) return 1;
	if (a > b) return -1;
	return 0;
}

function compareVersionStrings(a, b) {
	return compareVersionNumbers(ver2num(a), ver2num(b));
}

//See: https://stackoverflow.com/questions/3115150/how-to-escape-regular-expression-special-characters-using-javascript
function escapeRegExp(text) {
	return text.replace(/[-[\]{}()*+?.,\/\\^$|#\s]/g, '\\$&');
}

// Copies a string to the clipboard. Must be called from within an
// event handler such as click. May return false if it failed, but
// this is not always possible. Browser support for Chrome 43+,
// Firefox 42+, Safari 10+, Edge and IE 10+.
// IE: The clipboard feature may be disabled by an administrator. By
// default a prompt is shown the first time the clipboard is
// used (per session).
// See: https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript#answer-33928558
function copyToClipboard(text) {
	if (window.clipboardData && window.clipboardData.setData) {
		// IE specific code path to prevent textarea being shown while dialog is visible.
		return clipboardData.setData('Text', text);
	} else if (document.queryCommandSupported && document.queryCommandSupported('copy')) {
		var textarea = document.createElement('textarea');
		textarea.textContent = text;
		textarea.style.position = 'fixed'; // Prevent scrolling to bottom of page in MS Edge.
		document.body.appendChild(textarea);
		textarea.select();
		try {
			return document.execCommand('copy'); // Security exception may be thrown by some browsers.
		} catch (ex) {
			console.warn('Copy to clipboard failed.', ex);
			return false;
		} finally {
			document.body.removeChild(textarea);
		}
	}
}

/*
Generate UUIDs.
See: https://stackoverflow.com/questions/105034/create-guid-uuid-in-javascript#answer-2117523
*/
function uuidv4() {
	return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
		var r = (Math.random() * 16) | 0,
			v = c == 'x' ? r : (r & 0x3) | 0x8;
		return v.toString(16);
	});
}

/*
Removes diacritics from a (UTF) string, i.e. it reduces its characters to the closest ascii coutnerpart.
See: https://stackoverflow.com/questions/286921/efficiently-replace-all-accented-characters-in-a-string/#18160397
*/
function removeDiacritics(str) {
	var defaultDiacriticsRemovalMap = [
		{
			base: 'A',
			letters: /[\u0041\u24B6\uFF21\u00C0\u00C1\u00C2\u1EA6\u1EA4\u1EAA\u1EA8\u00C3\u0100\u0102\u1EB0\u1EAE\u1EB4\u1EB2\u0226\u01E0\u00C4\u01DE\u1EA2\u00C5\u01FA\u01CD\u0200\u0202\u1EA0\u1EAC\u1EB6\u1E00\u0104\u023A\u2C6F]/g,
		},
		{ base: 'AA', letters: /[\uA732]/g },
		{ base: 'AE', letters: /[\u00C6\u01FC\u01E2]/g },
		{ base: 'AO', letters: /[\uA734]/g },
		{ base: 'AU', letters: /[\uA736]/g },
		{ base: 'AV', letters: /[\uA738\uA73A]/g },
		{ base: 'AY', letters: /[\uA73C]/g },
		{ base: 'B', letters: /[\u0042\u24B7\uFF22\u1E02\u1E04\u1E06\u0243\u0182\u0181]/g },
		{ base: 'C', letters: /[\u0043\u24B8\uFF23\u0106\u0108\u010A\u010C\u00C7\u1E08\u0187\u023B\uA73E]/g },
		{ base: 'D', letters: /[\u0044\u24B9\uFF24\u1E0A\u010E\u1E0C\u1E10\u1E12\u1E0E\u0110\u018B\u018A\u0189\uA779]/g },
		{ base: 'DZ', letters: /[\u01F1\u01C4]/g },
		{ base: 'Dz', letters: /[\u01F2\u01C5]/g },
		{
			base: 'E',
			letters: /[\u0045\u24BA\uFF25\u00C8\u00C9\u00CA\u1EC0\u1EBE\u1EC4\u1EC2\u1EBC\u0112\u1E14\u1E16\u0114\u0116\u00CB\u1EBA\u011A\u0204\u0206\u1EB8\u1EC6\u0228\u1E1C\u0118\u1E18\u1E1A\u0190\u018E]/g,
		},
		{ base: 'F', letters: /[\u0046\u24BB\uFF26\u1E1E\u0191\uA77B]/g },
		{ base: 'G', letters: /[\u0047\u24BC\uFF27\u01F4\u011C\u1E20\u011E\u0120\u01E6\u0122\u01E4\u0193\uA7A0\uA77D\uA77E]/g },
		{ base: 'H', letters: /[\u0048\u24BD\uFF28\u0124\u1E22\u1E26\u021E\u1E24\u1E28\u1E2A\u0126\u2C67\u2C75\uA78D]/g },
		{ base: 'I', letters: /[\u0049\u24BE\uFF29\u00CC\u00CD\u00CE\u0128\u012A\u012C\u0130\u00CF\u1E2E\u1EC8\u01CF\u0208\u020A\u1ECA\u012E\u1E2C\u0197]/g },
		{ base: 'J', letters: /[\u004A\u24BF\uFF2A\u0134\u0248]/g },
		{ base: 'K', letters: /[\u004B\u24C0\uFF2B\u1E30\u01E8\u1E32\u0136\u1E34\u0198\u2C69\uA740\uA742\uA744\uA7A2]/g },
		{ base: 'L', letters: /[\u004C\u24C1\uFF2C\u013F\u0139\u013D\u1E36\u1E38\u013B\u1E3C\u1E3A\u0141\u023D\u2C62\u2C60\uA748\uA746\uA780]/g },
		{ base: 'LJ', letters: /[\u01C7]/g },
		{ base: 'Lj', letters: /[\u01C8]/g },
		{ base: 'M', letters: /[\u004D\u24C2\uFF2D\u1E3E\u1E40\u1E42\u2C6E\u019C]/g },
		{ base: 'N', letters: /[\u004E\u24C3\uFF2E\u01F8\u0143\u00D1\u1E44\u0147\u1E46\u0145\u1E4A\u1E48\u0220\u019D\uA790\uA7A4]/g },
		{ base: 'NJ', letters: /[\u01CA]/g },
		{ base: 'Nj', letters: /[\u01CB]/g },
		{
			base: 'O',
			letters: /[\u004F\u24C4\uFF2F\u00D2\u00D3\u00D4\u1ED2\u1ED0\u1ED6\u1ED4\u00D5\u1E4C\u022C\u1E4E\u014C\u1E50\u1E52\u014E\u022E\u0230\u00D6\u022A\u1ECE\u0150\u01D1\u020C\u020E\u01A0\u1EDC\u1EDA\u1EE0\u1EDE\u1EE2\u1ECC\u1ED8\u01EA\u01EC\u00D8\u01FE\u0186\u019F\uA74A\uA74C]/g,
		},
		{ base: 'OI', letters: /[\u01A2]/g },
		{ base: 'OO', letters: /[\uA74E]/g },
		{ base: 'OU', letters: /[\u0222]/g },
		{ base: 'P', letters: /[\u0050\u24C5\uFF30\u1E54\u1E56\u01A4\u2C63\uA750\uA752\uA754]/g },
		{ base: 'Q', letters: /[\u0051\u24C6\uFF31\uA756\uA758\u024A]/g },
		{ base: 'R', letters: /[\u0052\u24C7\uFF32\u0154\u1E58\u0158\u0210\u0212\u1E5A\u1E5C\u0156\u1E5E\u024C\u2C64\uA75A\uA7A6\uA782]/g },
		{ base: 'S', letters: /[\u0053\u24C8\uFF33\u1E9E\u015A\u1E64\u015C\u1E60\u0160\u1E66\u1E62\u1E68\u0218\u015E\u2C7E\uA7A8\uA784]/g },
		{ base: 'T', letters: /[\u0054\u24C9\uFF34\u1E6A\u0164\u1E6C\u021A\u0162\u1E70\u1E6E\u0166\u01AC\u01AE\u023E\uA786]/g },
		{ base: 'TZ', letters: /[\uA728]/g },
		{
			base: 'U',
			letters: /[\u0055\u24CA\uFF35\u00D9\u00DA\u00DB\u0168\u1E78\u016A\u1E7A\u016C\u00DC\u01DB\u01D7\u01D5\u01D9\u1EE6\u016E\u0170\u01D3\u0214\u0216\u01AF\u1EEA\u1EE8\u1EEE\u1EEC\u1EF0\u1EE4\u1E72\u0172\u1E76\u1E74\u0244]/g,
		},
		{ base: 'V', letters: /[\u0056\u24CB\uFF36\u1E7C\u1E7E\u01B2\uA75E\u0245]/g },
		{ base: 'VY', letters: /[\uA760]/g },
		{ base: 'W', letters: /[\u0057\u24CC\uFF37\u1E80\u1E82\u0174\u1E86\u1E84\u1E88\u2C72]/g },
		{ base: 'X', letters: /[\u0058\u24CD\uFF38\u1E8A\u1E8C]/g },
		{ base: 'Y', letters: /[\u0059\u24CE\uFF39\u1EF2\u00DD\u0176\u1EF8\u0232\u1E8E\u0178\u1EF6\u1EF4\u01B3\u024E\u1EFE]/g },
		{ base: 'Z', letters: /[\u005A\u24CF\uFF3A\u0179\u1E90\u017B\u017D\u1E92\u1E94\u01B5\u0224\u2C7F\u2C6B\uA762]/g },
		{
			base: 'a',
			letters: /[\u0061\u24D0\uFF41\u1E9A\u00E0\u00E1\u00E2\u1EA7\u1EA5\u1EAB\u1EA9\u00E3\u0101\u0103\u1EB1\u1EAF\u1EB5\u1EB3\u0227\u01E1\u00E4\u01DF\u1EA3\u00E5\u01FB\u01CE\u0201\u0203\u1EA1\u1EAD\u1EB7\u1E01\u0105\u2C65\u0250]/g,
		},
		{ base: 'aa', letters: /[\uA733]/g },
		{ base: 'ae', letters: /[\u00E6\u01FD\u01E3]/g },
		{ base: 'ao', letters: /[\uA735]/g },
		{ base: 'au', letters: /[\uA737]/g },
		{ base: 'av', letters: /[\uA739\uA73B]/g },
		{ base: 'ay', letters: /[\uA73D]/g },
		{ base: 'b', letters: /[\u0062\u24D1\uFF42\u1E03\u1E05\u1E07\u0180\u0183\u0253]/g },
		{ base: 'c', letters: /[\u0063\u24D2\uFF43\u0107\u0109\u010B\u010D\u00E7\u1E09\u0188\u023C\uA73F\u2184]/g },
		{ base: 'd', letters: /[\u0064\u24D3\uFF44\u1E0B\u010F\u1E0D\u1E11\u1E13\u1E0F\u0111\u018C\u0256\u0257\uA77A]/g },
		{ base: 'dz', letters: /[\u01F3\u01C6]/g },
		{
			base: 'e',
			letters: /[\u0065\u24D4\uFF45\u00E8\u00E9\u00EA\u1EC1\u1EBF\u1EC5\u1EC3\u1EBD\u0113\u1E15\u1E17\u0115\u0117\u00EB\u1EBB\u011B\u0205\u0207\u1EB9\u1EC7\u0229\u1E1D\u0119\u1E19\u1E1B\u0247\u025B\u01DD]/g,
		},
		{ base: 'f', letters: /[\u0066\u24D5\uFF46\u1E1F\u0192\uA77C]/g },
		{ base: 'g', letters: /[\u0067\u24D6\uFF47\u01F5\u011D\u1E21\u011F\u0121\u01E7\u0123\u01E5\u0260\uA7A1\u1D79\uA77F]/g },
		{ base: 'h', letters: /[\u0068\u24D7\uFF48\u0125\u1E23\u1E27\u021F\u1E25\u1E29\u1E2B\u1E96\u0127\u2C68\u2C76\u0265]/g },
		{ base: 'hv', letters: /[\u0195]/g },
		{ base: 'i', letters: /[\u0069\u24D8\uFF49\u00EC\u00ED\u00EE\u0129\u012B\u012D\u00EF\u1E2F\u1EC9\u01D0\u0209\u020B\u1ECB\u012F\u1E2D\u0268\u0131]/g },
		{ base: 'j', letters: /[\u006A\u24D9\uFF4A\u0135\u01F0\u0249]/g },
		{ base: 'k', letters: /[\u006B\u24DA\uFF4B\u1E31\u01E9\u1E33\u0137\u1E35\u0199\u2C6A\uA741\uA743\uA745\uA7A3]/g },
		{ base: 'l', letters: /[\u006C\u24DB\uFF4C\u0140\u013A\u013E\u1E37\u1E39\u013C\u1E3D\u1E3B\u017F\u0142\u019A\u026B\u2C61\uA749\uA781\uA747]/g },
		{ base: 'lj', letters: /[\u01C9]/g },
		{ base: 'm', letters: /[\u006D\u24DC\uFF4D\u1E3F\u1E41\u1E43\u0271\u026F]/g },
		{ base: 'n', letters: /[\u006E\u24DD\uFF4E\u01F9\u0144\u00F1\u1E45\u0148\u1E47\u0146\u1E4B\u1E49\u019E\u0272\u0149\uA791\uA7A5]/g },
		{ base: 'nj', letters: /[\u01CC]/g },
		{
			base: 'o',
			letters: /[\u006F\u24DE\uFF4F\u00F2\u00F3\u00F4\u1ED3\u1ED1\u1ED7\u1ED5\u00F5\u1E4D\u022D\u1E4F\u014D\u1E51\u1E53\u014F\u022F\u0231\u00F6\u022B\u1ECF\u0151\u01D2\u020D\u020F\u01A1\u1EDD\u1EDB\u1EE1\u1EDF\u1EE3\u1ECD\u1ED9\u01EB\u01ED\u00F8\u01FF\u0254\uA74B\uA74D\u0275]/g,
		},
		{ base: 'oi', letters: /[\u01A3]/g },
		{ base: 'ou', letters: /[\u0223]/g },
		{ base: 'oo', letters: /[\uA74F]/g },
		{ base: 'p', letters: /[\u0070\u24DF\uFF50\u1E55\u1E57\u01A5\u1D7D\uA751\uA753\uA755]/g },
		{ base: 'q', letters: /[\u0071\u24E0\uFF51\u024B\uA757\uA759]/g },
		{ base: 'r', letters: /[\u0072\u24E1\uFF52\u0155\u1E59\u0159\u0211\u0213\u1E5B\u1E5D\u0157\u1E5F\u024D\u027D\uA75B\uA7A7\uA783]/g },
		{ base: 's', letters: /[\u0073\u24E2\uFF53\u00DF\u015B\u1E65\u015D\u1E61\u0161\u1E67\u1E63\u1E69\u0219\u015F\u023F\uA7A9\uA785\u1E9B]/g },
		{ base: 't', letters: /[\u0074\u24E3\uFF54\u1E6B\u1E97\u0165\u1E6D\u021B\u0163\u1E71\u1E6F\u0167\u01AD\u0288\u2C66\uA787]/g },
		{ base: 'tz', letters: /[\uA729]/g },
		{
			base: 'u',
			letters: /[\u0075\u24E4\uFF55\u00F9\u00FA\u00FB\u0169\u1E79\u016B\u1E7B\u016D\u00FC\u01DC\u01D8\u01D6\u01DA\u1EE7\u016F\u0171\u01D4\u0215\u0217\u01B0\u1EEB\u1EE9\u1EEF\u1EED\u1EF1\u1EE5\u1E73\u0173\u1E77\u1E75\u0289]/g,
		},
		{ base: 'v', letters: /[\u0076\u24E5\uFF56\u1E7D\u1E7F\u028B\uA75F\u028C]/g },
		{ base: 'vy', letters: /[\uA761]/g },
		{ base: 'w', letters: /[\u0077\u24E6\uFF57\u1E81\u1E83\u0175\u1E87\u1E85\u1E98\u1E89\u2C73]/g },
		{ base: 'x', letters: /[\u0078\u24E7\uFF58\u1E8B\u1E8D]/g },
		{ base: 'y', letters: /[\u0079\u24E8\uFF59\u1EF3\u00FD\u0177\u1EF9\u0233\u1E8F\u00FF\u1EF7\u1E99\u1EF5\u01B4\u024F\u1EFF]/g },
		{ base: 'z', letters: /[\u007A\u24E9\uFF5A\u017A\u1E91\u017C\u017E\u1E93\u1E95\u01B6\u0225\u0240\u2C6C\uA763]/g },
	];

	for (var i = 0; i < defaultDiacriticsRemovalMap.length; i++) {
		str = str.replace(defaultDiacriticsRemovalMap[i].letters, defaultDiacriticsRemovalMap[i].base);
	}

	return str;
}

/*
Given a key and a value, call a settings wrapper, to persist the choice. Currently we are
using local storage, but as the client-side call(s) will not be modified we can switch
to any implemenation later.
*/
function update_user_setting(key, value) {
	localStorage.setItem(key, value);
}

/*
Given a key, retrieve the value stored in the local storage
 */
function retrieve_user_setting(key) {
	return localStorage.getItem(key);
}

/*
Dynamically load a js/css file.
Examples:
    loadjscssfile("myscript.js", "js") //dynamically load and add this .js file
    loadjscssfile("javascript.php", "js") //dynamically load "javascript.php" as a JavaScript file
    loadjscssfile("mystyle.css", "css") ////dynamically load and add this .css file
See: http://www.javascriptkit.com/javatutors/loadjavascriptcss.shtml
*/
function loadjscssfile(filename, filetype, callback = null) {
	if (filetype == 'js') {
		//if filename is a external JavaScript file
		var fileref = document.createElement('script');
		fileref.setAttribute('type', 'text/javascript');
		fileref.setAttribute('src', filename);
		fileref.addEventListener('load', () => callback && callback());
	} else if (filetype == 'css') {
		//if filename is an external CSS file
		var fileref = document.createElement('link');
		fileref.setAttribute('rel', 'stylesheet');
		fileref.setAttribute('type', 'text/css');
		fileref.setAttribute('href', filename);
	}
	if (typeof fileref != 'undefined') document.getElementsByTagName('head')[0].appendChild(fileref);
}

/*
Dynamically unload a js/css file
Examples:
    removejscssfile("somescript.js", "js") //remove all occurences of "somescript.js" on page
    removejscssfile("somestyle.css", "css") //remove all occurences "somestyle.css" on page
See: http://www.javascriptkit.com/javatutors/loadjavascriptcss.shtml
*/
function removejscssfile(filename, filetype) {
	var targetelement = filetype == 'js' ? 'script' : filetype == 'css' ? 'link' : 'none'; //determine element type to create nodelist from
	var targetattr = filetype == 'js' ? 'src' : filetype == 'css' ? 'href' : 'none'; //determine corresponding attribute to test for
	var allsuspects = document.getElementsByTagName(targetelement);
	for (var i = allsuspects.length; i >= 0; i--) {
		//search backwards within nodelist for matching elements to remove
		if (allsuspects[i] && allsuspects[i].getAttribute(targetattr) != null && allsuspects[i].getAttribute(targetattr).indexOf(filename) != -1)
			allsuspects[i].parentNode.removeChild(allsuspects[i]); //remove element by calling parentNode.removeChild()
	}
}

/*
Reads the text contents of a TextGrid file into an array object of the form:
	obj[TierName][ItemIndex]
where each array element is of the form:
	{ 'from': _, 'to': _, 'label': '_' }
*/
const parse_textgrid_content = (content) => {
	var results = [];

	//var lines = fs.readFileSync(filename).toString().split("\n");
	var lines = content.split('\n');

	var idx = 0;
	//Throw away until you find the "<exists>" line
	while (lines[idx++].trim() != '<exists>') {}

	var nTiers = parseInt(lines[idx++]);

	for (var tier = 0; tier < nTiers; tier++) {
		//Throw "IntervalTier" line
		idx++;

		//Read the name of the tier
		tierName = lines[idx++].trim();
		//tierName = tierName.replace (/(^")|("$)/g, ''); //Trim starting and ending quotes
		tierName = trim_double_quotes(tierName); //Trim starting and ending quotes

		results[tierName] = [];

		//Throw away start and end times
		idx += 2;

		//Read number of tier items
		var tierCount = parseInt(lines[idx++]);
		for (var item = 0; item < tierCount; item++) {
			var from = Number(parseFloat(lines[idx++]).toFixed(3)); //Keep only 3 decimals
			var to = Number(parseFloat(lines[idx++]).toFixed(3)); //Keep only 3 decimals

			var label = lines[idx++].trim();
			//label = label.replace (/(^")|("$)/g, ''); //Trim starting and ending quotes
			label = trim_double_quotes(label); //Trim starting and ending quotes

			results[tierName].push({ from: from, to: to, label: label });
		}
	}

	let tg = results;

	//Restructure the information from tier-based to a proper javascript object, grouping phones into the respective words.
	//This will lead to a layered structure in the form:
	//  textgrid
	//      words[]
	//          phones[]
	//Store the new structure in [data_tg]
	var data_tg = {
		sentence: '',
		words: [],
	};

	var sentence = '';
	tg['Words'].forEach(function (word, widx) {
		word.phones = [];
		data_tg.words.push(word);
		sentence += word.label + ' '; //Generate aggregate sentence
	});
	data_tg.sentence = sentence;

	//Find the min and max times that appear in any of the items in any of the tiers.
	//These will be used to insert empty words at the beginning and/or at the end, if necessary, to host orphan phones.
	var tmin = 1e10,
		tmax = -1e10;
	for (var tier in tg) {
		if (!tg.hasOwnProperty(tier)) continue;
		tg[tier].forEach(function (item, ii) {
			if (tmin > item.from) tmin = item.from;
			if (tmax < item.to) tmax = item.to;
		});
	}

	//If the first word starts later than tmin, insert a dummy word at the beginning.
	//If the last word ends before tmax, add a dummy word at the end.
	if (!data_tg.words.length) {
		data_tg.words.push({ from: tmin, to: tmax, label: '', phones: [] });
	} else {
		if (data_tg.words[0].from > tmin) data_tg.words.unshift({ from: tmin, to: data_tg.words[0].from, label: '', phones: [] });
		if (data_tg.words[data_tg.words.length - 1].to < tmax) data_tg.words.push({ from: data_tg.words[data_tg.words.length - 1].to, to: tmax, label: '', phones: [] });
	}

	//For each tier other than [Words]...
	//I.e. ["Phones", "Scores", "PValues", "IValues"]
	for (var tier in tg) {
		if (!tg.hasOwnProperty(tier) || tier == 'Words') continue;
		if (['Phones', 'Scores', 'PValues', 'IValues'].indexOf(tier) == -1) continue;
		//...for each item in that tier...
		tg[tier].forEach(function (item, idx) {
			//...find which word it should be placed in
			var widx = data_tg.words.findIndex(function (word) {
				return word.from <= item.from && word.to >= item.to;
			});
			if (widx == -1) {
				//The item belong to no word. Somethong is wrong... Throw an error.
				console.log('Item [' + idx + '] in tier [' + tier + '] does not belong to a word. Skipped!');
				console.log(item);
				return;
			}

			//So, the item belongs to the widx-th word.
			//Find if that word already has a phone with the same time interval as the specific item.
			var jdx = -1;
			if (tier == 'Phones') {
				//If we are processing the Phones tier, just add the phone!
				jdx = data_tg.words[widx].phones.push(item) - 1;
			} else {
				jdx = data_tg.words[widx].phones.findIndex(function (phone) {
					return phone.from == item.from && phone.to == item.to;
				});
				if (jdx == -1) {
					//No matching phone there. So add it (with an empty label)!
					jdx = data_tg.words[widx].phones.push({ from: item.from, to: item.to, label: '' }) - 1;
				}
				//Add a property to it with the same name as the tier (but lowercased)
				data_tg.words[widx].phones[jdx][tier.toLowerCase()] = tier == 'Scores' ? parseFloat(trim_double_quotes(item.label)) : item.label;
			}
		});
	}

	//Calculate phones durations.
	//Also, ensure that all phones (including pauses) have pitch values
	data_tg.words.forEach((word, widx) => {
		data_tg.words[widx].phones.forEach((phone, pidx) => {
			data_tg.words[widx].phones[pidx].durations = phone.to - phone.from;

			if (!phone.pvalues) {
				data_tg.words[widx].phones[pidx].pvalues = '0|0|0|0|0';
				if (!data_tg.words[widx].phones[pidx].warnings) data_tg.words[widx].phones[pidx].warnings = [];
				data_tg.words[widx].phones[pidx].warnings.push('No pitch points included');
			}
		});
	});

	//Take care of any special symbols, such as syllable boundaries, which should become flags rather than separate phones.
	//If they have a duration, then that will be merged into the following phone.
	/*
    data_tg.words.forEach((word,widx) => {
		word.phones = word.phones.filter((phone,pidx)=>{
			if (phone.label!=".")
				return true
			if (pidx==word.phones.length-1) { //No next phone to merge into. Merge into the previous, if any.
				console.log(`Found special phone [${phone.label}] at the end of the word which is unexpected.`)
				if (pidx>0) {
					console.log(`Merged into the previous phone.`)
					word.phones[pidx-1].to = phone.to
					word.phones[pidx-1].durations = phone.to - word.phones[pidx-1].from
					return false
				}
				console.log(`No next or previous phone to merge into. Ignoring special phone.`)
				return  false
			}
			//console.log(`Merged special phone [${phone.label}] into the next phone.`)
			word.phones[pidx+1].from = phone.from
			word.phones[pidx+1].durations = word.phones[pidx+1].to - phone.from
			word.phones[pidx+1].flags = {syllinitial: true}

			if (pidx>0)
				word.phones[pidx-1].flags = Object.assign({}, word.phones[pidx-1].flags, {syllfinal: true})
			return false
		})
	})
	*/

	data_tg.words.forEach((word, widx) => {
		let newphones = [];
		let specialphones = [];

		//First, go through all the phones and attach each one that is special to the following non-special phone
		word.phones.forEach((phone, pidx) => {
			let special = false;
			for (let sidx = 0; sidx < special_phone_prefixes.length; sidx++) {
				if (phone.label.indexOf(special_phone_prefixes[sidx].prefix) != 0) continue;
				special = true;
				specialphones.push(phone);
				break;
			}

			if (!special) {
				if (specialphones.length) phone.specialphones = specialphones;
				newphones.push(phone);
				specialphones = [];
				return;
			}

			specialphones.push(phone);
		});

		if (specialphones.length)
			console.log(
				`Some special phoneme prefixes could not by associated to a phone and are ignored: [${specialphones.map((p) => p.prefix).join('')}], in word [${
					word.label
				}}|${widx}].`,
			);

		//Now, go through the new phones and attach the necessary flags to the non-special phones
		newphones.forEach((phone, pidx) => {
			if (!phone.specialphones) return;

			//Merge the interval occupied by the all special phones into the phone
			phone.from = phone.specialphones[0].from;
			phone.durations = phone.to - phone.from;

			//Add to the phoneme (and its prev and next ones, if applicable) the respective flags
			phone.specialphones.forEach((special_phone) => {
				let def = special_phone_prefixes.find((s) => s.prefix == special_phone.label);
				if (def.flag) phone.flags = Object.assign({}, phone.flags, { [def.flag]: true });
				if (def.flagprev && pidx > 0) newphones[pidx - 1].flags = Object.assign({}, newphones[pidx - 1].flags, { [def.flagprev]: true });
				if (def.flagnext && pidx < newphones.length - 1) newphones[pidx + 1].flags = Object.assign({}, newphones[pidx + 1].flags, { [def.flagnext]: true });
			});
		});

		word.phones = newphones;
	});

	return data_tg;
};

/*
Convert TTS output XML to Praat TextGrid format
*/
function xml2tg(xmldata) {
	const flatten$ = (obj) => (!obj.$ ? obj : _.omit(_.extend(obj, obj.$), '$'));

	let warnings = [];

	let xmlDoc = $($.parseXML(xmldata));

	let sentences = xmlDoc
		.find('s[module="PSOLA"]')
		.map(function () {
			let sentence = {};
			// get sentence attributes
			//$.each(this.attributes, function(i, attrib){sentence[attrib.name] = attrib.value})
			// get sentence words
			sentence.words = $(this)
				.find('div[text]')
				.map(function () {
					let w = {};
					// get word attributes
					$.each(this.attributes, function (i, attrib) {
						w[attrib.name] = attrib.value;
					});
					// get word phonemes
					w.ph = $(this)
						.find('ph')
						.map(function () {
							let p = {};
							// phone attributes
							$.each(this.attributes, function (i, attrib) {
								p[attrib.name] = attrib.value;
							});
							return p;
						})
						.get();
					// get word diphones
					w.diphone = $(this)
						.find('diphone')
						.map(function () {
							let d = {};
							$.each(this.attributes, function (i, attrib) {
								d[attrib.name] = attrib.value;
							});
							return d;
						})
						.get()
						.map((d) => {
							// parse times
							let dnew = d;
							const props = ['startTime', 'midTime', 'endTime'];
							props.forEach((prop) => {
								dnew[prop] = parseFloat(dnew[prop]);
							});
							return dnew;
						});
					// check for empty diphones
					if (!w.diphone.length) {
						warnings.push(`No diphones in word [${w.text}]. Phonemes: ${w.ph.map((p) => `[${p.name}]`).join(' ')}`);
						return null;
					}
					return w;
				})
				.get();
			return sentence;
		})
		.get();

	if (warnings.length) alert(warnings.join('\n'));

	let textgrid = [];
	let startTime = sentences[0].words[0].diphone[0].startTime,
		endTime = sentences.slice(-1)[0].words.slice(-1)[0].diphone.slice(-1)[0].endTime;

	textgrid.push(
		'File type = "ooTextFile short"',
		'"TextGrid"',
		startTime,
		endTime,
		'<exists>',
		2, //# tiers
	);

	//-------------------------
	//Phones tier
	let phones = [{ label: '_', from: 0, to: 0 }];
	sentences.forEach((s) => {
		s.words.forEach((w) => {
			w.diphone.forEach((d) => {
				phones[phones.length - 1].to = d.midTime;
				phones.push({ label: d.rph, from: d.midTime, to: d.endTime });
			});
		});
	});
	textgrid.push(
		'IntervalTier',
		'Phones',
		startTime,
		endTime,
		phones.length, //# of items in the tier (phones)
	);
	phones.forEach((p) => {
		textgrid.push(p.from, p.to, `"${p.label}"`);
	});

	//-------------------------
	//Words tier
	let words = [];
	sentences.forEach((s) => {
		s.words.forEach((w) => {
			if (words.length) words[words.length - 1].to = w.diphone[0].midTime;
			words.push({ label: w.text, from: w.diphone[0].midTime, to: w.diphone.slice(-1)[0].endTime });
		});
	});
	textgrid.push(
		'IntervalTier',
		'Words',
		startTime,
		endTime,
		words.length, //# of items in the tier (words)
	);
	words.forEach((w) => {
		textgrid.push(w.from, w.to, `"${w.label}"`);
	});

	return textgrid.join('\n');
}

function parse_phoneme_types(buff) {
	const regex = /^(\S+)\s+(\S+)$/;
	let phone_types_info = {};

	buff.split('\n').forEach((line, iline) => {
		line = line.trim();
		if (!line.length) return;

		//Parse line
		let matches = line.match(regex);
		if (!matches) {
			console.error(`\tCould not parse line [${iline}]: ${line}`);
			return;
		}
		phone_types_info[matches[1]] = matches[2];
	});
	return phone_types_info;
}

//------------------------------------------------------------------------------------------
// BEGINNING OF DEEP MERGING/CLONING
/**
 * Deep merging/cloning of Object(s)
 * Based on: https://github.com/KyleAMathews/deepmerge
 */
function defaultIsMergeableObject(value) {
	return isNonNullObject(value) && !isSpecial(value);
}

function isNonNullObject(value) {
	return !!value && typeof value === 'object';
}

function isSpecial(value) {
	var stringValue = Object.prototype.toString.call(value);

	return stringValue === '[object RegExp]' || stringValue === '[object Date]' || isReactElement(value);
}

// see https://github.com/facebook/react/blob/b5ac963fb791d1298e7f396236383bc955f916c1/src/isomorphic/classic/element/ReactElement.js#L21-L25
var canUseSymbol = typeof Symbol === 'function' && Symbol.for;
var REACT_ELEMENT_TYPE = canUseSymbol ? Symbol.for('react.element') : 0xeac7;

function isReactElement(value) {
	return value.$$typeof === REACT_ELEMENT_TYPE;
}

function emptyTarget(val) {
	return Array.isArray(val) ? [] : {};
}

function cloneUnlessOtherwiseSpecified(value, options) {
	return options.clone !== false && options.isMergeableObject(value) ? deepmerge(emptyTarget(value), value, options) : value;
}

function defaultArrayMerge(target, source, options) {
	return target.concat(source).map(function (element) {
		return cloneUnlessOtherwiseSpecified(element, options);
	});
}

function mergeObject(target, source, options) {
	var destination = {};
	if (options.isMergeableObject(target)) {
		Object.keys(target).forEach(function (key) {
			destination[key] = cloneUnlessOtherwiseSpecified(target[key], options);
		});
	}
	Object.keys(source).forEach(function (key) {
		if (!options.isMergeableObject(source[key]) || !target[key]) {
			destination[key] = cloneUnlessOtherwiseSpecified(source[key], options);
		} else {
			destination[key] = deepmerge(target[key], source[key], options);
		}
	});
	return destination;
}

function deepmerge(target, source, options) {
	options = options || {};
	options.arrayMerge = options.arrayMerge || defaultArrayMerge;
	options.isMergeableObject = options.isMergeableObject || defaultIsMergeableObject;

	var sourceIsArray = Array.isArray(source);
	var targetIsArray = Array.isArray(target);
	var sourceAndTargetTypesMatch = sourceIsArray === targetIsArray;

	if (!sourceAndTargetTypesMatch) {
		return cloneUnlessOtherwiseSpecified(source, options);
	} else if (sourceIsArray) {
		return options.arrayMerge(target, source, options);
	} else {
		return mergeObject(target, source, options);
	}
}

deepmerge.all = function deepmergeAll(array, options) {
	if (!Array.isArray(array)) {
		throw new Error('first argument should be an array');
	}

	return array.reduce(function (prev, next) {
		return deepmerge(prev, next, options);
	}, {});
};

function mergeDeep(target, ...sources) {
	return deepmerge.all([target, ...arguments]);
}

function cloneDeep(source) {
	return deepmerge({}, source);
}
// END OF DEEP MERGING/CLONING
//------------------------------------------------------------------------------------------

function normalizeVoiceName(voicename) {
	return removeDiacritics(voicename).replace(/[^0-9a-zA-Z/-]/g, '_');
}

// See: https://stackoverflow.com/questions/15762768/javascript-math-round-to-two-decimal-places#answer-15762794
function roundTo(n, digits) {
	if (digits === undefined) {
		digits = 0;
	}

	var multiplicator = Math.pow(10, digits);
	n = parseFloat((n * multiplicator).toFixed(11));
	var test = Math.round(n) / multiplicator;
	return +test.toFixed(digits);
}

// Ses: https://stackoverflow.com/questions/3916191/download-data-url-file/45905238
function downloadURI(uri, name) {
	var link = document.createElement('a');
	link.download = name;
	link.href = uri;
	document.body.appendChild(link);
	link.click();
	document.body.removeChild(link);
	delete link;
}

/*
Download a file from a URL, monitor progress and call the provided callback when finished (done/failed/aborted)
Notes:
- 'local_filename' will be used as the local filename. However, in Chrome this is overriden by the 'filename'
	response header, if provided by the server
- If the file is big - it will be saved in the memory of the browser before the browser will write it to the disk
	(while with the regular download, files are being saved directly to the disk, which saves a lot of memory on big files).
- In order for the lengthComputable to be true - the server must send the Content-Length header with the size of the file.
*/
function downloadURI_progress(url, local_filename, progress_callback, callback) {
	let req = new XMLHttpRequest();
	req.open('GET', url, true);
	if (progress_callback) {
		req.addEventListener(
			'progress',
			(evt) => {
				if (evt.lengthComputable) {
					let percentComplete = (100 * evt.loaded) / evt.total;
					progress_callback(Math.round(percentComplete));
				}
			},
			false,
		);
	}

	const cb = (evt_tag, evt) => {
		switch (evt_tag) {
			case 'load':
				return callback && callback();
			case 'error':
				return callback && callback(new Error('ERROR: ' + JSON.stringify(evt)));
			case 'abort':
				return callback && callback(new Error('ABORT: ' + JSON.stringify(evt)));
		}
	};

	req.addEventListener('load', (evt) => cb('load', evt), false);
	req.addEventListener('error', (evt) => cb('error', evt), false);
	req.addEventListener('abort', (evt) => cb('abort', evt), false);

	req.responseType = 'blob';
	req.onreadystatechange = () => {
		if (req.readyState === 4 && req.status === 200) {
			var link = document.createElement('a');
			link.href = window.URL.createObjectURL(req.response);
			link.download = local_filename;
			link.click();
		}
	};

	req.send();
}

function approx_filesize(nBytes, isbytes = true) {
	var aMultiples = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

	if (!isbytes) aMultiples = aMultiples.map((m) => m.substr(0, m.length - 1));

	// Code for multiples approximation
	var sOutput = nBytes + ' bytes';
	for (var nMultiple = 0, nApprox = nBytes / 1024; nApprox > 0.8; nApprox /= 1024, nMultiple++) sOutput = nApprox.toFixed(2) + ' ' + aMultiples[nMultiple];

	let p = sOutput.split(' ');
	if (!isbytes) {
		p[0] = p[0].split('.')[0];
	}
	return p[0] + `<span style="font-size:0.75em; letter-spacing:-0.1em;"> ${p[1]}</span>`;
}

const rebase_paths = (obj, pathFrom, pathTo) => {
	let res = { ...obj };
	Object.keys(res).forEach((key) => {
		const type = typeof obj[key];
		if (type == 'string') res[key] = res[key].replace(pathFrom, pathTo);
		else if (type == 'object') res[key] = rebase_paths(res[key], pathFrom, pathTo);
	});
	return res;
};

const calc_avg_field = (arr, field, abs = false) => {
	let n = 0,
		sum = 0;
	arr.forEach((p) => {
		if (!(field in p)) return;
		sum += abs ? Math.abs(p[field]) : p[field];
		n += 1;
	});
	return n ? sum / n : no_value;
};

//
// Calculate aggregate score of a word.
// It is the minimum of the average 'zscores' and average abs('zdurations') of its phones,
// taking into account only non-break phones.
//
function word_score(w) {
	if (!w.phones) return no_value;

	let p_filtered = w.phones.filter((p) => !punctuation.includes(p.label) && 'zscores' in p);
	// if (p_filtered.length <= 1) return no_value;
	if (!p_filtered.length) return no_value;

	let avg_zscore = calc_avg_field(p_filtered, 'zscores'),
		avg_zdur = calc_avg_field(p_filtered, 'zdurations', true);

	// Bin the data
	// return Math.round(Math.min(avg_zscore, -avg_zdur));

	return Math.min(avg_zscore, -avg_zdur);
}

//--------------------------------------------------------------------------------------------------------
// Align a corpus utterance to a seg utterance.
// On error it will raise an exception.
// The function:
//	- copies the 'utt.text' into 'seg_utt.sentence'
//	- for each pair of matched words, calls the provided match_func(word, seg_word). The function is optional
//		and, if provided, it must return a seg_word that will replace the existing seg_word at that location.
//--------------------------------------------------------------------------------------------------------
function align_seg_corpus_utt(seg_utt, utt, match_func = null) {
	let error = null;

	let uttid = utt.id;

	/*
	If the words in the corpus utterance are of the form
		"words": [
			{ "text": "Hmm,", "phones": "hm|,", "pos": "prp" },
			...
		]
	turn them into the following form to make them more directly comparable to seg words:
		"words": [
			{
				"label": "Hmm,",
				"pos": "prp",
				"phones": [
					{ "label": "hm" },
					{ "label": "," }
				]
			},
			...
		]
	*/
	if (typeof utt['words'][0]['phones'] == 'string') {
		// Convert from a corpus-like format to a seg-like format.
		// Also change the field names of words/phones to match those of segmentation (e.g. word/phone/'text' -> word/phone/'label')
		utt.words = utt.words.map((word) => ({
			label: word.text,
			pos: word.pos || undefined,
			phones: word.phones
				.split('|')
				// Remove empty phones at the end (e.g. as in "l|u1|k|s|")
				.filter((p) => p.length)
				// Remove syllable boundaries '.' (e.g. as in "t|w|e1|n|.t|ii|")
				.map((p) => ({ label: p.length > 1 && p[0] == '.' ? p.slice(1) : p })),
		}));
	}

	let iseg = 0,
		icor = 0;
	let nseg = seg_utt['words'].length,
		ncor = utt['words'].length;

	let output_seg_utt = Object.assign(JSON.parse(JSON.stringify(seg_utt)), { words: [] });
	let unmatched_word_idx = [];

	while (!error && (iseg < nseg || icor < ncor)) {
		if (iseg < nseg && icor >= ncor) {
			// There is an extra word at the end of segmentation. Maybe it is a silence word.
			if (seg_utt['words'][iseg].label == '' && seg_utt['words'][iseg]['phones'].length == 1 && sp_sil.includes(seg_utt['words'][iseg]['phones'])) {
				unmatched_word_idx.push(iseg);
				output_seg_utt['words'].push(JSON.parse(JSON.stringify(seg_utt['words'][iseg])));
				iseg++;
				continue;
			} else {
				error = `[${uttid}]: Word [${iseg}] in segmentation is unmatched to the corpus`;
				break;
			}
		}

		if (iseg >= nseg && icor < ncor) {
			// There is an extra word in the corpus. That's unexpected!
			error = `[${uttid}]: Word [${icor}] in corpus is unmatched to the segmentation`;
			break;
		}

		// So, now we know that both iseg<nseg and icor<ncor.

		let wseg = seg_utt['words'][iseg],
			wcor = utt['words'][icor];

		let cor_phones = wcor['phones'].map((p) => p.label);
		let seg_phones = wseg['phones'].map((p) => p.label);

		// It the current segmentation word has the same phonemes with the current corpus word, merge them.
		if (seg_phones.filter((p) => !sp_sil.includes(p)).join('|') == cor_phones.filter((p) => !gr_punctuation.includes(p)).join('|')) {
			output_seg_utt['words'].push(match_func ? match_func(wcor, wseg) : JSON.parse(JSON.stringify(seg_utt['words'][iseg])));
			iseg += 1;
			icor += 1;
			continue;
		}

		// If the current segmentation word is silence (having only a silence phone), insert it in the current location of the corpus utt.
		// This should be quite common for the initial silence of an utterance.
		if (seg_utt['words'][iseg]['label'] == '' && seg_utt['words'][iseg]['phones'].length == 1 && sp_sil.includes(seg_utt['words'][iseg]['phones'][0]['label'])) {
			output_seg_utt['words'].push(JSON.parse(JSON.stringify(seg_utt['words'][iseg])));
			iseg++;
			continue;
		}

		// Could not align current words. Raise an error for the whole utterance
		error = `[${seg_utt.id}]: Error aligning words at positions: cor=${icor} | seg=${iseg}`;
		break;
	}

	return output_seg_utt;
}



function object_is(obj, spec) {
	for (k in spec) {
		if (typeof spec[k] != typeof obj[k]) return false;
		if (typeof spec[k] == 'object') {
			if (!object_is(obj[k], spec[k])) return false;
		} else {
			if (spec[k] != obj[k]) return false;
		}
	}
	return true;
}

function array_intersection(array1, array2) {
	return array1.filter((value) => array2.includes(value));
}

function array_has_all(array1, array2) {
	return array_intersection(array1, array2).length == array2.length;
}


function object_to_html(obj) {
	return typeof(obj)=='object' && !Array.isArray(obj) ? Object.keys(obj).sort().map(k => `<b>${k}</b>: ${JSON.stringify(obj[k])}`).join('\n') : JSON.stringify(obj)
}


// Check if entity has a history item compatible with the provided properties
function entity_has_history(entity, prop) {
	// if (!entity.history || !entity.history.length) return false;
	// return entity.history.find((h) => object_is(h, prop)) ? true : false;

	if (entity.history && entity.history.length && entity.history.find((h) => object_is(h, prop)))
		return true

	if (entity.running_jobs) 
		if (Object.keys(entity.running_jobs).some((jobid) => object_is({
			params: entity.running_jobs[jobid].params,
			recipe: entity.running_jobs[jobid].recipe || entity.running_jobs[jobid].task,
			}, prop)
		))
			return true
	
	return false
}

// Check if entity is currently running a recipe/task compatible with the provided properties
function entity_is_running(entity, prop) {
	if (!entity.running_jobs || !Object.keys(entity.running_jobs).length) return false;
	return Object.keys(entity.running_jobs).find((k) => object_is(entity.running_jobs[k], prop)) ? true : false;
}

// Check if entity has the given properties and, optionally, has the specified history item
function entity_is(entity, props, hist) {
	return (
		!Object.keys(props).some((p) => {
			if (typeof props[p] == 'object' && Array.isArray(props[p])) return !entity[p] || !array_has_all(entity[p], props[p]);
			else return entity[p] != props[p];
		}) &&
		(!hist || entity_has_history(entity, hist) || entity_is_running(entity, hist))
	);
}


if (typeof exports != 'undefined') {
	if (typeof special_phone_prefixes == 'undefined') {
		special_phone_prefixes = require('./definitions').special_phone_prefixes;
	}

	exports.stringify = stringify;

	exports.timer = timer;
	exports.time_duration = time_duration;

	exports.ver2num = ver2num;
	exports.htmlEntities = htmlEntities;
	exports.escapeRegExp = escapeRegExp;
	exports.parse_textgrid_content = parse_textgrid_content;
	exports.normalizeVoiceName = normalizeVoiceName;

	exports.removeDiacritics = removeDiacritics;
	exports.parse_phoneme_types = parse_phoneme_types;

	exports.mergeDeep = mergeDeep;
	exports.cloneDeep = cloneDeep;

	exports.roundTo = roundTo;

	exports.approx_filesize = approx_filesize;

	exports.rebase_paths = rebase_paths;

	exports.no_value = no_value;
	exports.punctuation = punctuation;
	exports.calc_avg_field = calc_avg_field;
	exports.word_score = word_score;

	exports.align_seg_corpus_utt = align_seg_corpus_utt;

	exports.object_is = object_is;
	exports.array_intersection = array_intersection;
	exports.array_has_all = array_has_all;
	exports.entity_has_history = entity_has_history;
	exports.entity_is_running = entity_is_running;
	exports.entity_is = entity_is;
}






