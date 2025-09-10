---
layout: default
---

<div class="container">
  <h1>Poemas</h1>
  <ul>
    {% for poema in site.poemas %}
      <li>
        <a href="{{ poema.url }}">{{ poema.title }}</a>
        <small>{{ poema.date | date: "%d-%m-%Y" }}</small>
      </li>
    {% endfor %}
  </ul>
</div>
