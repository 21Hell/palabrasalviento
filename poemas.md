---
layout: default
---

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
  <h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Poemas</h1>
  {% assign categorias = site.poemas | map: 'categoria' | uniq %}
  {% for cat in categorias %}
    <h2 style="margin-top:2em; color:#0056b3; border-bottom:1px solid #eee;">{{ cat | capitalize }}</h2>
    {% if cat == "panoramas" %}
      <div style="background:#f7f7f7; padding:1em 1.5em; margin-bottom:1em; font-style:italic; color:#444; border-radius:8px;">
        Enero primero 2021<br>
        Dia primero vaya año acabamos de pasar y el futuro que nos depara no parece ganar sencillo recuerdo de los años pasados, viendo como mis tragedias soo fueron plantadas por mi mismo, trabajar en mi mismo es el plan del mañana de hoy y de todo lo que siga
      </div>
    {% endif %}
    <div class="poemas-list" style="display:flex; flex-wrap:wrap; gap:2em; justify-content:center; margin-bottom:2em;">
      {% assign poemas_categoria = site.poemas | where: "categoria", cat | sort: "date" %}
      {% for poema in poemas_categoria %}
        <div class="poema-card" style="background:#f7f7f7; border-radius:18px; box-shadow:0 2px 12px rgba(0,0,0,0.08); padding:1.5em 2em; max-width:320px; min-width:220px; margin-bottom:1em; display:flex; flex-direction:column; align-items:flex-start;">
          <a href="{{ site.baseurl }}{{ poema.url }}" style="font-size:1.2em; font-weight:bold; color:#0056b3; text-decoration:none; margin-bottom:0.5em;">{{ poema.title }}</a>
          <span style="color:#888; font-size:0.95em; margin-bottom:0.7em;">{{ poema.date | date: "%Y" }}</span>
          <span style="color:#444; font-size:1em; font-style:italic; white-space:pre-line;">
            {% if poema.parrafos %}
              {{ poema.parrafos[0].texto | strip_html | truncatewords: 10, '...' }}
            {% else %}
              {{ poema.content | strip_html | truncatewords: 10, '...' }}
            {% endif %}
          </span>
        </div>
      {% endfor %}
    </div>
  {% endfor %}
</div>
<style>
.poemas-list { display:flex; flex-wrap:wrap; gap:2em; justify-content:center; }
.poema-card { background:#f7f7f7; border-radius:18px; box-shadow:0 2px 12px rgba(0,0,0,0.08); padding:1.5em 2em; max-width:320px; min-width:220px; margin-bottom:1em; display:flex; flex-direction:column; align-items:flex-start; }
@media (max-width: 700px) {
  .poemas-list { flex-direction:column; gap:1em; align-items:center; }
  .poema-card { max-width:98vw; min-width:0; width:100%; }
}
</style>
