---
layout: default
---

<div class="container">
  <h1>Películas</h1>
  <ul>
    {% for pelicula in site.peliculas %}
      <li>
        <a href="{{ pelicula.url }}">{{ pelicula.title }}</a>
        <small>{{ pelicula.date | date: "%d-%m-%Y" }}</small>
      </li>
    {% endfor %}
  </ul>
</div>
