---
layout: default
title: "Libros"
---


<div class="container" style="max-width:750px; margin:auto; padding:2.5em 1em 2em 1em;">
  <h1 style="color:#222; font-size:2em; text-align:center; margin-bottom:1.5em; font-weight:normal; letter-spacing:0.01em;">Libros</h1>
  <div class="libros-list">
    {% if site.libros and site.libros.size > 0 %}
      {% assign libros_con_date = site.libros | where_exp: "l", "l.date" %}
      {% assign libros_ordenados = libros_con_date | sort: "date" | reverse %}
      {% for libro in libros_ordenados %}
        <div class="libro-card">
          <a href="{{ site.baseurl }}{{ libro.url }}" class="libro-title">{{ libro.title }}</a>
          {% if libro.autor_libro %}
            <span class="libro-autor-libro">de {{ libro.autor_libro }}</span>
          {% endif %}
          <span class="libro-date">{{ libro.date | date: "%Y" }}</span>
          {% if libro.autor %}
            <span class="libro-autor">reseña: {{ libro.autor }}</span>
          {% endif %}
        </div>
      {% endfor %}
    {% else %}
      <p style="text-align:center; color:#888;">No hay libros disponibles aún.</p>
    {% endif %}
  </div>
</div>

<style>
/* Libros index sober style */
.libros-list {
  display: flex;
  flex-direction: column;
  gap: 1.5em;
  margin-bottom: 2em;
}
.libro-card {
  background: #f5f5f5;
  border-radius: 8px;
  box-shadow: 0 1px 6px rgba(0,0,0,0.03);
  padding: 1.2em 1.5em;
  margin-bottom: 0.5em;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.libro-title {
  font-size: 1.13em;
  font-weight: 500;
  color: #222;
  text-decoration: none;
  margin-bottom: 0.2em;
  letter-spacing: 0.01em;
}
.libro-title:hover {
  text-decoration: underline;
}
.libro-autor-libro {
  font-size: 1em;
  color: #666;
  margin-bottom: 0.2em;
  font-style: italic;
}
.libro-date {
  font-size: 0.97em;
  color: #aaa;
  margin-bottom: 0.2em;
}
.libro-autor {
  font-size: 0.97em;
  color: #888;
  margin-top: 0.1em;
}
</style>
