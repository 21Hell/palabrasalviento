---
layout: default
title: Plausible
body_class: plausible-page
---

<style>
.plausible-wrap {
	max-width: 1200px;
	margin: 1rem auto;
	padding: 0 1rem 2rem;
}

.plausible-panel {
	background: #c0c0c0;
	border: 2px solid;
	border-color: #dfdfdf #808080 #808080 #dfdfdf;
	box-shadow: inset 1px 1px 0 #ffffff, inset -1px -1px 0 #1d1a16;
	padding: 0.8rem;
}

.plausible-panel h1 {
	margin: 0 0 0.75rem;
	background: #2f2a24;
	color: #f3d36b;
	padding: 0.35rem 0.5rem;
	font-size: 1rem;
	font-weight: bold;
	font-family: 'MS Sans Serif', 'Microsoft Sans Serif', Arial, sans-serif;
	border-bottom: 2px solid #dfdfdf;
}

.plausible-panel p {
	margin: 0 0 0.75rem;
	font-family: 'MS Sans Serif', 'Microsoft Sans Serif', Arial, sans-serif;
	font-size: 0.95rem;
	line-height: 1.5;
	color: #000;
}

.plausible-embed {
	width: 100%;
	height: 120px;
	border: 1px solid #444;
	background: #111;
	box-sizing: border-box;
}

.plausible-note a {
	color: #7a3e00;
	font-weight: bold;
	text-decoration: underline;
}

.plausible-warning {
	background: #fff3cd;
	border: 1px solid #d6b656;
	padding: 0.75rem 0.85rem;
	margin: 0 0 0.75rem;
	font-family: 'MS Sans Serif', 'Microsoft Sans Serif', Arial, sans-serif;
	font-size: 0.92rem;
	line-height: 1.45;
	color: #4b3f00;
}

.plausible-warning strong {
	display: block;
	margin-bottom: 0.25rem;
}

@media (max-width: 720px) {
	.plausible-wrap {
		padding: 0 0.5rem 1rem;
	}

	.plausible-embed {
		height: 140px;
	}
}
</style>

<div class="plausible-wrap">
	<section class="plausible-panel">
		<h1>Plausible</h1>
		<p>La analítica del blog ahora usa Plausible. Carga un script ligero, sin cookies, y no requiere un panel embebido dentro del sitio.</p>
		<div class="plausible-warning">
			<strong>Configuración</strong>
			Asegúrate de que <code>plausible_domain</code> en <code>_config.yml</code> coincida con el dominio público del blog y que <code>plausible_src</code> apunte al script correcto.
		</div>
		<p class="plausible-note">Si usas el servicio alojado, el script suele ser <a href="https://plausible.io/js/script.js" target="_blank" rel="noopener">plausible.io/js/script.js</a>.</p>
	</section>
</div>