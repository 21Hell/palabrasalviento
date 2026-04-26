---
layout: default
title: Acerca de
body_class: acerca-page
---

# Acerca de

<section class="section">
	<p>
		Escribiendo poemas, viendo peliculas, tomando fotos, programando y como habras notado, haciendo listas.
	</p>
	<p>
		<a href="https://www.instagram.com/cwolf_imc/" target="_blank" rel="noopener">Instagram</a>
		|
		<a href="https://boxd.it/2WdEN" target="_blank" rel="noopener">Letterboxd</a>
	</p>
</section>

<script>
document.addEventListener('DOMContentLoaded', function () {
	var root = document.body;
	if (!root || !root.classList.contains('acerca-page')) return;

	function updatePointerVars(clientX, clientY) {
		var xPercent = (clientX / window.innerWidth) * 100;
		var yPercent = (clientY / window.innerHeight) * 100;
		var shiftX = (xPercent - 50) * 0.18;
		var shiftY = (yPercent - 50) * 0.18;

		root.style.setProperty('--mouse-x', xPercent.toFixed(2) + '%');
		root.style.setProperty('--mouse-y', yPercent.toFixed(2) + '%');
		root.style.setProperty('--bubble-shift-x', shiftX.toFixed(2) + 'px');
		root.style.setProperty('--bubble-shift-y', shiftY.toFixed(2) + 'px');
	}

	window.addEventListener('pointermove', function (ev) {
		updatePointerVars(ev.clientX, ev.clientY);
	});

	window.addEventListener('pointerleave', function () {
		root.style.setProperty('--mouse-x', '50%');
		root.style.setProperty('--mouse-y', '50%');
		root.style.setProperty('--bubble-shift-x', '0px');
		root.style.setProperty('--bubble-shift-y', '0px');
	});
});
</script>
