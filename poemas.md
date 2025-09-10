---
layout: default
---

<div class="container">
  <h1>Poemas</h1>
  {% assign categorias = site.poemas | map: 'categoria' | uniq %}
  {% for cat in categorias %}
    <h2 style="margin-top:2em; color:#0056b3; border-bottom:1px solid #eee;">{{ cat | capitalize }}</h2>
    {% if cat == "panoramas" %}
      <div style="background:#f7f7f7; padding:1em 1.5em; margin-bottom:1em; font-style:italic; color:#444; border-radius:8px;">
        Enero primero 2021<br>
        Dia primero vaya año acabamos de pasar y el futuro que nos depara no parece ganar sencillo recuerdo de los años pasados, viendo como mis tragedias soo fueron plantadas por mi mismo, trabajar en mi mismo es el plan del mañana de hoy y de todo lo que siga
      </div>
    {% endif %}
    <ul>
      {% for poema in site.poemas %}
        {% if poema.categoria == cat %}
          <li style="margin-bottom:2em;">
            <a href="{{ poema.url }}"><strong>{{ poema.title }}</strong></a><br>
            <span style="display:block; color:#555; font-style:italic; white-space:pre-line;">
              {{ poema.content | strip_html | truncatewords: 12, '...' }}
            </span>
          </li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endfor %}
</div>
