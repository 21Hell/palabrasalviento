---
layout: default
title: Nostalgia
---

<div class="container">
  <h1>Poemas: Nostalgia</h1>
  <ul>
    {% assign nostalgia_poems = site.poemas | where: "categoria", "nostalgia" %}
    {% for poema in nostalgia_poems %}
      <li style="margin-bottom:2em;">
  <a href="{{ site.baseurl }}{{ poema.url }}"><strong>{{ poema.title }}</strong></a><br>
        <span style="display:block; color:#555; font-style:italic; white-space:pre-line;">
          {{ poema.content | strip_html | truncatewords: 12, '...' }}
        </span>
      </li>
    {% endfor %}
  </ul>
</div>
