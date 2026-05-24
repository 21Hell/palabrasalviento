---
layout: default
title: Umami
body_class: umami-page
---

<style>
.umami-wrap {
	max-width: 1200px;
	margin: 1rem auto;
	padding: 0 1rem 2rem;
}

.umami-panel {
	background: #c0c0c0;
	border: 2px solid;
	border-color: #dfdfdf #808080 #808080 #dfdfdf;
	box-shadow: inset 1px 1px 0 #ffffff, inset -1px -1px 0 #1d1a16;
	padding: 0.8rem;
}

.umami-panel h1 {
	margin: 0 0 0.75rem;
	background: #2f2a24;
	color: #f3d36b;
	padding: 0.35rem 0.5rem;
	font-size: 1rem;
	font-weight: bold;
	font-family: 'MS Sans Serif', 'Microsoft Sans Serif', Arial, sans-serif;
	border-bottom: 2px solid #dfdfdf;
}

.umami-panel p {
	margin: 0 0 0.75rem;
	font-family: 'MS Sans Serif', 'Microsoft Sans Serif', Arial, sans-serif;
	font-size: 0.95rem;
	line-height: 1.5;
	color: #000;
}

.umami-embed {
	width: 100%;
	height: min(82vh, 980px);
	border: 1px solid #444;
	background: #111;
	box-sizing: border-box;
}

.umami-note a {
	color: #7a3e00;
	font-weight: bold;
	text-decoration: underline;
}

.umami-warning {
	background: #fff3cd;
	border: 1px solid #d6b656;
	padding: 0.75rem 0.85rem;
	margin: 0 0 0.75rem;
	font-family: 'MS Sans Serif', 'Microsoft Sans Serif', Arial, sans-serif;
	font-size: 0.92rem;
	line-height: 1.45;
	color: #4b3f00;
}

.umami-warning strong {
	display: block;
	margin-bottom: 0.25rem;
}

@media (max-width: 720px) {
	.umami-wrap {
		padding: 0 0.5rem 1rem;
	}

	.umami-embed {
		height: 74vh;
	}
}
</style>

<div class="umami-wrap">
	<section class="umami-panel">
		<h1>Umami</h1>
		<p>Este panel solo embebe Umami cuando hay una URL segura disponible. Así evitamos el bloqueo de contenido mixto en HTTPS.</p>
		{% if site.umami_embed_url != empty %}
		<iframe
			class="umami-embed"
			src="{{ site.umami_embed_url }}"
			title="Umami dashboard"
			loading="lazy"
			rel="noopener"
		></iframe>
		<p class="umami-note">Si prefieres abrirlo aparte, usa <a href="{{ site.umami_direct_url }}" target="_blank" rel="noopener">esta URL directa</a>.</p>
		{% else %}
		<div class="umami-warning">
			<strong>Embed desactivado</strong>
			El dashboard todavía no tiene una URL HTTPS pública. El navegador bloquea iframes HTTP dentro del blog.
			Usa la <a href="{{ site.umami_direct_url }}" target="_blank" rel="noopener">URL directa de Umami</a> o configura <code>umami_embed_url</code> con una dirección HTTPS.
		</div>
		<p class="umami-note">Cuando tengas una URL segura, el iframe se activará automáticamente.</p>
		{% endif %}
	</section>
</div>