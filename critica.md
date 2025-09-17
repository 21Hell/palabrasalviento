---
title: "Críticas"
layout: default
---

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
  <h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Críticas</h1>
  <div class="criticas-list" style="display:flex; flex-wrap:wrap; gap:2em; justify-content:center; margin-bottom:2em;">
    {% assign ensayos = site.criticas | default: empty %}
    {% assign ensayos_ordenados = ensayos | sort: "date" | reverse %}
    {% for ensayo in ensayos_ordenados %}
      <div class="critica-card" style="background:#f7f7f7; border-radius:18px; box-shadow:0 2px 12px rgba(0,0,0,0.08); padding:1.5em 2em; max-width:320px; min-width:220px; margin-bottom:1em; display:flex; flex-direction:column; align-items:flex-start;">
        <a href="{{ site.baseurl }}{{ ensayo.url }}" style="font-size:1.2em; font-weight:bold; color:#0056b3; text-decoration:none; margin-bottom:0.5em;">{{ ensayo.title }}</a>
        <span style="color:#888; font-size:0.95em; margin-bottom:0.7em;">{{ ensayo.date | date: "%Y" }}</span>
        <span style="color:#444; font-size:1em; font-style:italic; white-space:pre-line;">
          {% if ensayo.excerpt %}
            {{ ensayo.excerpt }}
          {% else %}
            {{ ensayo.content | strip_html | truncatewords: 18, '...' }}
          {% endif %}
        </span>
      </div>
    {% endfor %}
  </div>
</div>
<style>
.criticas-list { display:flex; flex-wrap:wrap; gap:2em; justify-content:center; }
.critica-card { background:#f7f7f7; border-radius:18px; box-shadow:0 2px 12px rgba(0,0,0,0.08); padding:1.5em 2em; max-width:320px; min-width:220px; margin-bottom:1em; display:flex; flex-direction:column; align-items:flex-start; }
@media (max-width: 700px) {
  .criticas-list { flex-direction:column; gap:1em; align-items:center; }
  .critica-card { max-width:98vw; min-width:0; width:100%; }
}
</style>
