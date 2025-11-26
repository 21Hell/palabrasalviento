---
title: "Ensayos"
layout: default
---

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
  <h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Ensayos</h1>
  <div class="ensayos-lista">
  {% assign ensayos = site.ensayos %}
  {% if ensayos.size == null %}
    {% assign ensayos = '' | split: '' %}
  {% endif %}
  {% assign ensayos_ordenados = ensayos | sort: "date" | reverse %}
  {% for ensayo in ensayos_ordenados %}
    <a href="{{ site.baseurl }}{{ ensayo.url }}" class="ensayo-card" style="display:block; text-decoration:none; color:inherit;">
      <h2 style="margin-top:0;">{{ ensayo.title }}</h2>
      <span class="ensayo-date">{{ ensayo.date | date: "%Y-%m-%d" }}</span>
      <p>
        {% if ensayo.excerpt %}
          {{ ensayo.excerpt }}
        {% else %}
          {{ ensayo.content | strip_html | truncatewords: 18, '...' }}
        {% endif %}
      </p>
    </a>
    {% endfor %}
  </div>
</div>
