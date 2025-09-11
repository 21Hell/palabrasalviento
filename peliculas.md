---
layout: default
title: "Películas"
---

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
  <h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Películas</h1>
  <div class="peliculas-list">
    {% for pelicula in site.peliculas %}
      <div class="pelicula-card">
        {% if pelicula.poster %}
          <a href="{{ site.baseurl }}{{ pelicula.url }}" style="display:block; margin-bottom:1em;">
            <img src="{{ pelicula.poster }}" alt="Poster {{ pelicula.title }}">
          </a>
        {% endif %}
        <a href="{{ site.baseurl }}{{ pelicula.url }}" class="pelicula-title">{{ pelicula.title }}</a>
        <span class="pelicula-year">{{ pelicula.year }}</span>
        {% if pelicula.rating %}
          <span class="pelicula-rating">{{ pelicula.rating }}<span class="pelicula-max">/5</span></span>
        {% endif %}
      </div>
    {% endfor %}
  </div>
</div>

<style>
.peliculas-list {
  display:flex;
  flex-wrap:wrap;
  gap:2em;
  justify-content:center;
  margin-bottom:2em;
}
.pelicula-card {
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
.pelicula-card img {
  max-width:120px;
  border-radius:10px;
  box-shadow:0 2px 8px rgba(0,0,0,0.10);
  margin-bottom:1em;
}
.pelicula-title {
  font-size:1.15em;
  font-weight:bold;
  color:#0056b3;
  text-decoration:none;
  margin-bottom:0.5em;
  text-align:center;
}
.pelicula-year {
  color:#888;
  font-size:0.95em;
  margin-bottom:0.7em;
}
.pelicula-rating {
  color:#ffb400;
  font-size:1.2em;
  font-weight:bold;
  text-align:center;
}
.pelicula-max {
  font-size:0.7em;
  color:#888;
  margin-left:0.3em;
}
@media (max-width: 700px) {
  .peliculas-list { flex-direction:column; gap:1em; align-items:center; }
  .pelicula-card { max-width:98vw; min-width:0; width:100%; }
}
</style>
