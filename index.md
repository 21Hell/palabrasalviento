---
layout: default
---

<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/landing.css">

<div class="hero">
 <h1>Palabras al Viento</h1>
 <p>Blog de expresión libre creado por <strong>Carlos Wolf</strong>, donde los poemas, la reflexión y la experimentación artística se cruzan para compartir ideas, procesos y hallazgos.</p>
 <p>Al final solo son palabras tiradas al viento.</p>
</div>

<div class="container-main">
 <div class="section">
   <h2 class="latest-entry-title">Última entrada</h2>
   {% assign ultimo_poema = site.poemas | sort: 'date' | reverse | first %}
   <a class="latest-entry-link" href="{{ site.baseurl }}{{ ultimo_poema.url }}" aria-label="Abrir última entrada: {{ ultimo_poema.title }}">
    <article class="latest-entry-card">
      <h3 class="latest-entry-name">{{ ultimo_poema.title }}</h3>
      <span class="poema-year">{{ ultimo_poema.date | date: "%Y" }}</span>
    </article>
   </a>
 </div>

 <div class="section">
  <div class="hackerspace-section"> 
   <h2>Manifiesto de un Kernelita</h2>
   <p>Los Kernelitas somos un grupo de personas que nos reunimos para compartir conocimientos, aprender y crear en el ámbito de la tecnología, la informática y la cultura hacker. Nos apasiona el software libre, el hardware abierto y la colaboración comunitaria. En nuestro hackerspace, el Kernel Panic Room, fomentamos un ambiente de apoyo donde esa crisis posterior al Kernel Panic no tiene que ser una experiencia solitaria.</p>
   <p>Que la gloria de San iGNUcio nos guíe al año del Linux Desktop.</p>
   <p>Interesado en el hackerspace?</p>
  <a href="https://eventos.kernelpanic.lol/" class="button" style="display: inline-block; background: #2f2a24; color: #f3d36b; padding: 0.5em 1em; border: 2px solid #dfdfdf #1d1a16 #1d1a16 #dfdfdf; margin-top: 0.8em; text-decoration: none; font-weight: bold;">Únete al próximo Viernes de Linux</a>
  </div>
 </div>

 <div class="section">
  <div class="card">
   <h2>Sitio raíz de la comunidad</h2>
   <p>Para ver el sitio principal de Kernel Panic Room, visita el root oficial:</p>
  <a href="https://kernelpanic.lol" target="_blank" rel="noopener" class="button" style="display: inline-block; background: #2f2a24; color: #f3d36b; padding: 0.5em 1em; border: 2px solid #dfdfdf #1d1a16 #1d1a16 #dfdfdf; margin-top: 0.5em; text-decoration: none; font-weight: bold;">Ir a kernelpanic.lol</a>
  </div>
 </div>
</div>
