---
layout: default
---

<div class="container" style="max-width:900px; margin:auto; padding:2em 1em;">
  <h1 style="color:#0056b3; font-size:2em; text-align:center; margin-bottom:1em;">Poemas</h1>
  <div id="poemas-disclaimer-bar" style="background:#fffbe6; border:1px solid #ffe58f; color:#8c6d1f; padding:1.2em 2em; border-radius:18px; max-width:600px; margin:0 auto 2em auto; font-size:1.15em; text-align:justify; box-shadow:0 4px 24px rgba(0,0,0,0.12); position:relative; display:none;">
    <button id="poemas-disclaimer-close" style="position:absolute; top:10px; right:16px; background:none; border:none; font-size:1.3em; color:#8c6d1f; cursor:pointer;">&times;</button>
    <strong>Disclaimer</strong><br><br>
  Los poemas aquí presentados son obras originales de Carlos Wolf y forman parte de un archivo histórico personal. Este espacio tiene como objetivo la expresión libre y no está destinado a la venta de ningún producto. Se trata de un blog de poemas, es decir, un sitio a razon de diario o libreta informal. Si deseas contactar al autor para cualquier consulta o propuesta, puedes hacerlo a través de su cuenta de Instagram:<br>
      <a href="https://www.instagram.com/cwolf_imc/" target="_blank" rel="noopener" style="color:#0056b3; text-decoration:none;">@cwolf_imc</a>.<br><br>
       <span style="font-size:0.95em; color:#6c5d2f;">Nota: Este disclaimer fue hecho a petición de Gabriel Kryger. para no herir suceptibilidades de poetas y poetisas</span><br>

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
    <div class="poemas-list" style="display:flex; flex-wrap:wrap; gap:2em; justify-content:center; margin-bottom:2em;">
  {% assign poemas_categoria = site.poemas | where: "categoria", cat | sort: "date" | reverse %}
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
