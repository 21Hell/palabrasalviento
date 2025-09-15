---
layout: default
title: "Experimentos"
---

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
	<h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Experimentos</h1>
	<div class="experimentos-list">
		{% for experimento in site.experimentos %}
			<div class="experimento-card">
				<a href="{{ site.baseurl }}{{ experimento.url }}" class="experimento-title">{{ experimento.title }}</a>
				{% if experimento.date %}
					<span class="experimento-date">{{ experimento.date | date: "%Y" }}</span>
				{% endif %}
				{% if experimento.autor %}
					<span class="experimento-autor">{{ experimento.autor }}</span>
				{% endif %}
			</div>
		{% endfor %}
	</div>
</div>

<style>
.experimentos-list {
	display:flex;
	flex-wrap:wrap;
	gap:2em;
	justify-content:center;
	margin-bottom:2em;
}
.experimento-card {
	background:#f7f7f7;
	border-radius:18px;
	box-shadow:0 2px 12px rgba(0,0,0,0.08);
	padding:1.5em 2em;
	max-width:320px;
	min-width:220px;
	margin-bottom:1em;
	display:flex;
	flex-direction:column;
	align-items:center;
}
.experimento-title {
	font-size:1.15em;
	font-weight:bold;
	color:#0056b3;
	text-decoration:none;
	margin-bottom:0.5em;
	text-align:center;
}
.experimento-date {
	color:#888;
	font-size:0.95em;
	margin-bottom:0.7em;
}
.experimento-autor {
	color:#888;
	font-size:1em;
	margin-bottom:0.7em;
}
@media (max-width: 700px) {
	.experimentos-list { flex-direction:column; gap:1em; align-items:center; }
	.experimento-card { max-width:98vw; min-width:0; width:100%; }
}
</style>
