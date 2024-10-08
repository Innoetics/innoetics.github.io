const corpus = {
	"chatbot_510112": "I thought it was pretty clear.",
	"chatbot_510149": "I'm not a fan of that word.",
	"chatbot_510178": "I wonder why that is so interesting.",
	"chatbot_510306": "Can you give me more information.",
	"chatbot_510378": "I like meeting any new human being.",
	"Bixby_NLG_W_3002033": "Actually, we've already been receiving notifications during calls.",
	"Bixby_NLG_W_3002482": "Okay, let's choose a time to send it.",
	"Bixby_NLG_W_3002497": "OK, let's choose what you want here.",
	"Bixby_NLG_W_3002530": "Looks like you don't have any messages.",
	"Bixby_NLG_W_3002577": "Hmm, I can't block this.",
	"Bixby_44840": "Both chicken and egg exist alongside each other in parallel universes: Drawn ever closer yet never touching, they remain forever bound in the abyss of Zeno's paradox, thus representing the boundless refractions and circularity of time.",
	"Bixby_44918": "The word of the day, is Japanese, and is the answer to this riddle: An expression that is two-fold, rhymes, and means to find beauty in imperfections, and to accept the cycle of life and death.",
	"Bixby_45203": "Zedoary; the dried rhizome of an Indian plant, Curcuma zedoaria, of the ginger family, that has a bitter taste and is used medicinally, especially as an intestinal stimulant and carminative.",
	"Bixby_45221": "Looks like it's time for the word of the day: Macadamize; to construct or finish by compacting into a solid mass, a layer of small broken stone, on a convex, well-drained roadbed. And using a binder, such as cement or asphalt, for the mass.",
	"Bixby_45378": "An aimless, semiconscious plucking at the bedclothes, observed in conditions of exhaustion or stupor, or in high fevers; hmm, and I just thought \"carphology\" was the study of cars.",
	"Bixby_19702": "It's King if I'm not mistaken.",
	"Bixby_19703": "Hey Tony Ieraci.",
	"Bixby_19704": "So, Papa is what I should call you?",
	"Bixby_19705": "So, Jay is what I should call you?",
	"Bixby_19706": "So, A is what I should call you?",
	"00363": " She was always a bookish child.",
	"00399": " Do you know how to program a computer?",
	"00448": " Most students in this class are fifteen.",
	"00627": " It started to happen as Thursday's game wore on.",
	"00947": " John and Mary are in love.",
	"customer_320371": "Say the message you want to send, or say something like, Never mind, to cancel.",
	"dialog_decl_400305": "The good and the great are only separated by their willingness to sacrifice.",
	"dialog_prompt_420511": "Charlotte's given us until noon tomorrow before she goes to another designer.",
	"dialog_yes_no_090042": "Did you know that you can now see the environmental impact, your printing has?",
	"movsum_0333": "A man takes on a mission that could bring equality to the polarized worlds.",
	"news_what_082864": "Why should people here try to sabotage these Games in the spirit of friendship?",
	"news_what_083040": "What has led to the increase in turnovers created by Green Bay's defense?",
	"news_yes_no_080816": "Does it mean that a military withdrawal merely has to start, by that date?"
}

const spkid_to_name = {
	"spk0": "john",
	"spk1": "stephanie",
	"spk2": "lisa",
	"spk3": "julia"
}


const perm_samples_per_speaker = {
	"spk0": [
		"chatbot_510112",
		"chatbot_510149",
		"chatbot_510178",
		"chatbot_510306",
		"chatbot_510378",
		"chatbot_510395",
		"chatbot_510444",
		"chatbot_510546",
		"chatbot_510735",
		"chatbot_511142",
		"chatbot_511194",
		"chatbot_511546",
		"chatbot_511568",
		"chatbot_511600",
		"chatbot_511645",

	],
	"spk1": [
		"Bixby_NLG_W_3002033",
		"Bixby_NLG_W_3002482",
		"Bixby_NLG_W_3002497",
		"Bixby_NLG_W_3002530",
		"Bixby_NLG_W_3002577",
		"Bixby_NLG_W_3002651",
		"Bixby_NLG_W_3002690",
		"Bixby_NLG_W_3002756",
		"Bixby_NLG_W_3002845",
		"Bixby_NLG_W_3002851",
		"Bixby_NLG_W_3002855",
		"Bixby_NLG_W_3002858",
		"Bixby_NLG_W_3002865",
		"Bixby_NLG_W_3002873",
		"Bixby_NLG_W_3002890",
		"Bixby_NLG_W_3002983",
		"Bixby_NLG_W_3003023",
		"Bixby_NLG_W_3003028",
		"Bixby_NLG_W_3003044",

	],
	"spk2": [
		"Bixby_44840",
		"Bixby_44918",
		"Bixby_45203",
		"Bixby_45221",
		"Bixby_45378",
		"Bixby_45410",
		"Bixby_45424",
		"Bixby_45525",
		"Bixby_45672",
	],
	"spk3": [
		"00363",
		"00399",
		"00448",
		"00627",
		"00947",
		"01412_chunk_640_36832",
		"014410",
		"014430",
		"01594_chunk_36240_69080",
		"01635"
	]
}

const samples_per_speaker = {
	"spk0": [
		"chatbot_510112",
		"chatbot_510149",
		"chatbot_510178",
		"chatbot_510306",
		"chatbot_510378",
		"chatbot_510395",
		"chatbot_510444",
		"chatbot_510546",
		"chatbot_510735",
		"chatbot_511142",
	],
	"spk1": [
		"Bixby_NLG_W_3002033",
		"Bixby_NLG_W_3002482",
		"Bixby_NLG_W_3002497",
		"Bixby_NLG_W_3002530",
		"Bixby_NLG_W_3002577",
		"Bixby_NLG_W_3002651",
		"Bixby_NLG_W_3002690",
		"Bixby_NLG_W_3002756",
		"Bixby_NLG_W_3002845",
		"Bixby_NLG_W_3002851",
		"Bixby_NLG_W_3002855",

	],
	"spk2": [
		"Bixby_19702",
		"Bixby_19703",
		"Bixby_19704",
		"Bixby_19705",
		"Bixby_19706",
		"Bixby_19707",
		"Bixby_19708",
		"Bixby_19709",
		"Bixby_19710",
		"Bixby_19711",
		"Bixby_19712",
	],
	"spk3": [
		"00363",
		"00399",
		"00448",
		"00627",
		"00947",
		"01412_chunk_640_36832",
		"014410",
		"014430",
		"01594_chunk_36240_69080",
		"01635"
	]
}


const copy_synth_samples = [
	"customer_320371",
	"dialog_decl_400305",
	"dialog_prompt_420511",
	"dialog_yes_no_090042",
	"movsum_0333",
	"news_what_082864",
	"news_what_083040",
	"news_yes_no_080816"
]

const copy_synth_prompt = "So you develop a wild enthousiasm about making a small business successful"

const pitch_plots = [
	"Bixby_NLG_W_3002033",
	"Bixby_NLG_W_3002250",
	"Bixby_NLG_W_3002482",
	"Bixby_NLG_W_3002497",
	"Bixby_NLG_W_3002530",
	"chatbot_510112",
	"chatbot_510149",
	"chatbot_510178",
	"chatbot_510306",
	"chatbot_510378",
]

const pitch_plot_pairs = [
	{ id: "Bixby_NLG_W_3002033", from: "spk1", to: "spk0" },
	{ id: "Bixby_NLG_W_3002250", from: "spk1", to: "spk0" },
	{ id: "Bixby_NLG_W_3002482", from: "spk1", to: "spk0" },
	{ id: "Bixby_NLG_W_3002497", from: "spk1", to: "spk0" },
	{ id: "Bixby_NLG_W_3002530", from: "spk1", to: "spk0" },
	{ id: "chatbot_510112", from: "spk0", to: "spk1" },
	{ id: "chatbot_510149", from: "spk0", to: "spk1" },
	{ id: "chatbot_510178", from: "spk0", to: "spk1" },
	{ id: "chatbot_510306", from: "spk0", to: "spk1" },
	{ id: "chatbot_510378", from: "spk0", to: "spk1" },
]