---
layout: default
---
<style>
/* Poems index responsive styles */
.poemas-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem; }
.poema-card { background:#fff; border-radius:10px; padding:0.9rem 1rem; box-shadow:0 2px 10px rgba(0,0,0,0.06); display:flex; flex-direction:column; gap:0.5rem; position:relative; }
.poema-link { color:#0b5ed7; font-weight:700; font-size:1rem; text-decoration:none; }
.poema-year { color:#6c757d; font-size:0.85rem; }
.poema-excerpt { color:#333; font-size:0.95rem; line-height:1.35; margin-top:0.4rem; }
/* Off-screen searchable text: present in DOM but visually hidden */
.poema-search { position:absolute; left:-9999px; top:auto; width:1px; height:1px; overflow:hidden; }
@media (max-width:800px) {
  /* Force exactly 2 columns for viewports up to 800px */
  .poemas-list { grid-template-columns: repeat(2,1fr) !important; gap:0.8rem !important; }
  .poema-card { padding:0.9rem !important; }
  .poema-link { font-size:1.04rem !important; }
  .poema-excerpt { font-size:1.00rem !important; line-height:1.45 !important; }
}
@media (max-width:640px) {
  /* Tighter adjustments for small phones */
  .poemas-list { grid-template-columns: repeat(2,1fr); gap:0.6rem; }
  .poema-card { padding:0.8rem; }
  .poema-link { font-size:1.02rem; }
  .poema-excerpt { font-size:0.98rem; line-height:1.45; }
}
@media (min-width:1600px) { .poemas-list { grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); gap:1.5rem; } }
</style>

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
  <h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Poemas</h1>
  <div id="poemas-disclaimer-bar" style="background:#fffbe6; border:1px solid #ffe58f; color:#8c6d1f; padding:1.2em 2em; border-radius:18px; max-width:600px; margin:0 auto 2em auto; font-size:1.15em; text-align:justify; box-shadow:0 4px 24px rgba(0,0,0,0.12); position:relative; display:none;">
    <button id="poemas-disclaimer-close" style="position:absolute; top:10px; right:16px; background:none; border:none; font-size:1.3em; color:#8c6d1f; cursor:pointer;">&times;</button>
    <strong>Disclaimer</strong><br><br>
  Los poemas aquí presentados son obras originales de Carlos Wolf y forman parte de un archivo histórico personal. Este espacio tiene como objetivo la expresión libre y no está destinado a la venta de ningún producto. Se trata de un blog de poemas, es decir, un sitio a razon de diario o libreta informal. Si deseas contactar al autor para cualquier consulta o propuesta, puedes hacerlo a través de su cuenta de Instagram:<br>
      <a href="https://www.instagram.com/cwolf_imc/" target="_blank" rel="noopener" style="color:#0056b3; text-decoration:none;">@cwolf_imc</a>.<br><br>
       <span style="font-size:0.95em; color:#6c5d2f;">Nota: Este disclaimer fue hecho a petición de Mesa para no herir suceptibilidades de poetas y poetisas</span><br>

    <button id="poemas-disclaimer-hide-btn" style="margin-top:1em; padding:0.6em 2em; background:#ffe58f; color:#8c6d1f; border:none; border-radius:8px; font-size:1em; cursor:pointer;">No mostrar de nuevo</button>
  </div>
  <script>
    function showDisclaimerBar() {
      var bar = document.getElementById('poemas-disclaimer-bar');
      if (!localStorage.getItem('poemasDisclaimerHidden')) {
        bar.style.display = 'block';
      }
      document.getElementById('poemas-disclaimer-close').onclick = function() {
        bar.style.display = 'none';
      };
      document.getElementById('poemas-disclaimer-hide-btn').onclick = function() {
        bar.style.display = 'none';
        localStorage.setItem('poemasDisclaimerHidden', 'true');
      };
    }
    document.addEventListener('DOMContentLoaded', showDisclaimerBar);
  </script>
  {% assign categorias = site.poemas | map: 'categoria' | uniq %}
  {%- assign cat_keys = "" | split: "" -%}
  {%- for c in categorias -%}
    {%- assign poemas_cat = site.poemas | where: "categoria", c | sort: "date" -%}
    {%- assign first_poema = poemas_cat | first -%}
    {%- if first_poema -%}
      {%- assign min_date = first_poema.date | date: "%Y-%m-%d" -%}
    {%- else -%}
      {%- assign min_date = "9999-12-31" -%}
    {%- endif -%}
    {%- assign key = min_date | append: "|" | append: c -%}
    {%- assign cat_keys = cat_keys | push: key -%}
  {%- endfor -%}
  {%- assign ordered_keys = cat_keys | sort | reverse -%}
  {% for key in ordered_keys %}
    {% assign parts = key | split: "|" %}
    {% assign cat = parts[1] %}
    <h2 style="margin-top:2em; color:#0056b3; border-bottom:1px solid #eee;">{{ cat | capitalize }}</h2>
    {% if cat == "panoramas" %}
      <div style="background:#f7f7f7; padding:1em 1.5em; margin-bottom:1em; font-style:italic; color:#444; border-radius:8px;">
        Enero primero 2021<br>
        Dia primero vaya año acabamos de pasar y el futuro que nos depara no parece ganar sencillo recuerdo de los años pasados, viendo como mis tragedias soo fueron plantadas por mi mismo, trabajar en mi mismo es el plan del mañana de hoy y de todo lo que siga
      </div>
    {% endif %}
    <div class="poemas-list">
      {% assign poemas_categoria = site.poemas | where: "categoria", cat | sort: "date" | reverse %}
      {% for poema in poemas_categoria %}
        <article class="poema-card">
          <a class="poema-link" href="{{ site.baseurl }}{{ poema.url }}">{{ poema.title }}</a>
          <span class="poema-year">{{ poema.date | date: "%Y" }}</span>
          <p class="poema-excerpt">
            {% if poema.parrafos %}
              {{ poema.parrafos[0].texto | strip_html | truncatewords: 12, '...' }}
            {% else %}
              {{ poema.content | strip_html | truncatewords: 12, '...' }}
            {% endif %}
          </p>
          <!-- Hidden full-text for browser search (Ctrl/Cmd+F) -->
          <div class="poema-search">{{ poema.content | strip_html | replace: '\n', ' ' }}</div>
        </article>
      {% endfor %}
    </div>
  {% endfor %}
</div>

