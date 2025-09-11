---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---


<div class="container" style="max-width:700px; margin:auto; padding:2em 1em;">
	<h1 style="color:#0056b3; font-size:2.2em; text-align:center; margin-bottom:0.5em;">Bienvenido a Palabras al Viento</h1>
	<p style="font-size:1.2em; color:#444; text-align:center; margin-bottom:2em;">Un espacio para compartir poemas y reflexiones sobre películas.<br>Al final, solo palabras tiradas al viento.</p>

		<div style="background:#f7f7f7; border-radius:18px; box-shadow:0 2px 12px rgba(0,0,0,0.08); padding:1.5em 2em; margin-bottom:2em;">
			<h2 style="color:#0056b3; font-size:1.3em; margin-bottom:0.3em;">Última entrada</h2>
			{% assign ultimo_poema = site.poemas | sort: 'date' | reverse | first %}
			<a href="{{ site.baseurl }}{{ ultimo_poema.url }}" style="font-size:1.1em; font-weight:bold; color:#0056b3; text-decoration:none;">{{ ultimo_poema.title }}</a>
			<span style="color:#888; font-size:0.95em; margin-left:1em;">{{ ultimo_poema.date | date: "%Y" }}</span>
			<div style="color:#444; font-size:1em; margin-top:0.7em; font-style:italic; white-space:pre-line;">
				{% if ultimo_poema.parrafos %}
					{{ ultimo_poema.parrafos[0].texto | strip_html | truncatewords: 24, '...' }}
				{% else %}
					{{ ultimo_poema.content | strip_html | truncatewords: 24, '...' }}
				{% endif %}
			</div>
		</div>
</div>
