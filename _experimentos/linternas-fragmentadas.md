---
title: "Linternas Fragmentadas"
layout: experimento
date: 2026-08-20
show_full_date: false
permalink: /experimentos/linternas-fragmentadas/
categoria: procesamiento de imagen
autor: Carlos Wolf
---

Mini herramienta para recortar fragmentos desde una imagen y tejerlos dentro de una frase.


<div id="fragment-lab" style="text-align:left; max-width:1100px; margin:0 auto;">
  <div class="lab-panel">
    <div class="lab-controls">
      <label class="lab-label">Imagen
        <input id="imgInput" type="file" accept="image/*">
      </label>

      <label class="lab-label">Texto base
        <textarea id="baseText" rows="3">A kaleidoscope of painted wings dances across the vast and tranquil cerulean sky.</textarea>
      </label>

      <div class="lab-grid">
        <label class="lab-label">Cantidad
          <input id="countInput" type="range" min="3" max="24" value="10">
          <span id="countValue">10</span>
        </label>

        <label class="lab-label">Tamano de recorte
          <input id="sizeInput" type="range" min="20" max="120" value="52">
          <span id="sizeValue">52 px</span>
        </label>

        <label class="lab-label">Ancho del recorte
          <input id="widthInput" type="range" min="40" max="180" value="100">
          <span id="widthValue">100%</span>
        </label>

        <label class="lab-label">Alto del recorte
          <input id="heightInput" type="range" min="40" max="180" value="100">
          <span id="heightValue">100%</span>
        </label>

        <label class="lab-label">Rotacion
          <input id="rotationInput" type="range" min="-45" max="45" value="0">
          <span id="rotationValue">0°</span>
        </label>

        <label class="lab-label">Escala tipografica
          <input id="fontScaleInput" type="range" min="70" max="180" value="110">
          <span id="fontScaleValue">1.10x</span>
        </label>
      </div>

      <div class="lab-position">
        <div class="lab-position-header">Recorte x Posicion</div>
        <div id="positionGrid" class="position-grid" aria-label="Seleccion de posicion"></div>
      </div>

      <div class="lab-row lab-align-row">
        <span class="lab-align-label">Alineacion del poema</span>
        <label><input type="radio" name="textAlign" value="left" checked> Izquierda</label>
        <label><input type="radio" name="textAlign" value="center"> Centrado</label>
        <label><input type="radio" name="textAlign" value="right"> Derecha</label>
      </div>

      <div class="lab-row">
        <label><input type="radio" name="mode" value="random" checked> Random</label>
        <label><input type="radio" name="mode" value="manual"> Manual</label>
      </div>

      <div class="lab-row">
        <button id="generateBtn" type="button">Generar</button>
        <button id="clearBtn" type="button">Limpiar</button>
        <button id="selectBtn" type="button" class="secondary">Seleccionar corte</button>
        <button id="exportBtn" type="button" class="secondary">Exportar imagen</button>
      </div>

      <p id="hint" class="lab-hint">Tip: en modo manual, haz click para crear recortes y arrastralos para moverlos.</p>
    </div>
  </div>

  <div class="canvas-wrap">
    <div class="canvas-top">
      <div id="sentenceOut" class="sentence-out"></div>
    </div>
    <canvas id="imageCanvas" width="1000" height="600"></canvas>
  </div>
</div>

<style>
#fragment-lab {
  --ink: #16161a;
  --muted: #50505a;
  --paper: #f8f8fb;
  --line: #d8d8e2;
  --accent: #c75a2b;
  margin-top: 0.5rem;
}

#fragment-lab .lab-panel {
  background: linear-gradient(120deg, #ffffff 0%, #f6f8ff 100%);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 1rem;
  box-shadow: 0 8px 24px rgba(19, 19, 28, 0.08);
  margin-bottom: 1.4rem;
}

#fragment-lab .lab-controls {
  display: grid;
  gap: 0.9rem;
}

#fragment-lab .lab-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
  gap: 0.8rem;
}

#fragment-lab .lab-label {
  color: var(--ink);
  display: grid;
  gap: 0.35rem;
  font-size: 0.95rem;
}

#fragment-lab input[type="file"],
#fragment-lab textarea,
#fragment-lab input[type="range"] {
  width: 100%;
}

#fragment-lab textarea {
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 0.6rem;
  background: #fff;
  color: var(--ink);
  resize: vertical;
}

#fragment-lab .lab-row {
  display: flex;
  gap: 0.9rem;
  align-items: center;
  flex-wrap: wrap;
}

#fragment-lab .lab-align-row {
  margin-top: 0.1rem;
}

#fragment-lab .lab-align-label {
  font-weight: 600;
  color: var(--ink);
}

#fragment-lab button {
  border: 1px solid #1d1d25;
  background: #1d1d25;
  color: #fff;
  border-radius: 8px;
  padding: 0.5rem 0.9rem;
  cursor: pointer;
}

#fragment-lab button.secondary {
  background: #f5f6fb;
  color: #1d1d25;
  border-color: var(--line);
}

#fragment-lab button:hover {
  background: #2e2e38;
}

#fragment-lab button.secondary:hover {
  background: #ebedf6;
}

#fragment-lab .lab-hint {
  color: var(--muted);
  margin: 0;
}

#fragment-lab .lab-position {
  display: grid;
  gap: 0.5rem;
  margin-top: 0.2rem;
}

#fragment-lab .lab-position-header {
  font-weight: 600;
  color: var(--ink);
}

#fragment-lab .position-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(42px, 1fr));
  gap: 0.4rem;
  max-height: 180px;
  overflow: auto;
  padding: 0.4rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.5);
}

#fragment-lab .position-cell {
  min-height: 36px;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #f5f6fb;
  color: var(--ink);
  font-size: 0.72rem;
  cursor: pointer;
  transition: all 0.12s ease;
}

#fragment-lab .position-cell:hover {
  border-color: #8aa5c9;
  background: #edf3ff;
}

#fragment-lab .position-cell.is-active {
  background: #dfe9ff;
  border-color: #5183d8;
  box-shadow: inset 0 0 0 1px rgba(81, 131, 216, 0.5);
}

#fragment-lab .canvas-top {
  background: rgba(255, 255, 255, 0.78);
  border-bottom: 1px solid rgba(17, 17, 17, 0.06);
  padding: 1rem 1rem 0.4rem;
  width: 100%;
  max-width: 1000px;
  margin: 0 auto;
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

#fragment-lab .sentence-out {
  margin: 0;
  color: var(--ink);
  line-height: 1.15;
  min-height: 2.5em;
  font-size: clamp(1.5rem, 2.1vw, 3rem);
  letter-spacing: -0.055em;
  font-weight: 500;
  word-wrap: break-word;
  text-align: center;
  width: 100%;
  max-width: 100%;
  margin-inline: auto;
  padding-bottom: 0.5rem;
  display: block;
  box-sizing: border-box;
  overflow-wrap: anywhere;
}

#fragment-lab .sentence-frag {
  display: inline-block;
  margin: 0 0.08em 0.12em 0;
  vertical-align: middle;
  border-radius: 4px;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08), 0 5px 14px rgba(0, 0, 0, 0.08);
  background: rgba(255, 255, 255, 0.28);
  border: 1px solid rgba(17, 17, 17, 0.08);
  cursor: grab;
  user-select: none;
}

#fragment-lab .sentence-frag:active,
#fragment-lab .sentence-frag.is-dragging {
  cursor: grabbing;
  opacity: 0.18;
}

#fragment-lab .sentence-drag-ghost {
  position: fixed;
  z-index: 1000;
  pointer-events: none;
  margin: 0;
  opacity: 0.9;
  box-shadow: 0 8px 22px rgba(0, 0, 0, 0.24);
}

#fragment-lab .sentence-word.is-drop-target {
  background: rgba(81, 131, 216, 0.16);
  box-shadow: inset 0 0 0 2px rgba(81, 131, 216, 0.65);
}

#fragment-lab .sentence-line {
  display: block;
  margin: 0 0 0.2em;
}

#fragment-lab .sentence-word {
  display: inline-block;
  margin-right: 0.18em;
  white-space: nowrap;
  cursor: pointer;
  border-radius: 0.2em;
  padding: 0 0.08em;
}

#fragment-lab .sentence-word.is-active {
  background: rgba(199, 90, 43, 0.12);
  box-shadow: inset 0 0 0 1px rgba(199, 90, 43, 0.45);
}

#fragment-lab .canvas-wrap {
  border: 1px solid var(--line);
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(180deg, #dbeaf8 0%, #b9d6fb 100%);
  box-shadow: 0 10px 28px rgba(16, 36, 63, 0.10);
  display: grid;
  grid-template-rows: auto auto;
  width: min(100%, 1000px);
  margin: 0 auto;
}

#fragment-lab #imageCanvas {
  width: 100%;
  max-width: 1000px;
  height: auto;
  display: block;
  cursor: crosshair;
  touch-action: none;
  background: linear-gradient(180deg, #dfeafc 0%, #b9d6fb 100%);
  margin: 0 auto;
}

@media (max-width: 760px) {
  #fragment-lab .sentence-out {
    font-size: 1.4rem;
  }
}
</style>

<script>
(function() {
  const imgInput = document.getElementById('imgInput');
  const baseText = document.getElementById('baseText');
  const countInput = document.getElementById('countInput');
  const sizeInput = document.getElementById('sizeInput');
  const widthInput = document.getElementById('widthInput');
  const heightInput = document.getElementById('heightInput');
  const rotationInput = document.getElementById('rotationInput');
  const fontScaleInput = document.getElementById('fontScaleInput');
  const countValue = document.getElementById('countValue');
  const sizeValue = document.getElementById('sizeValue');
  const widthValue = document.getElementById('widthValue');
  const heightValue = document.getElementById('heightValue');
  const rotationValue = document.getElementById('rotationValue');
  const fontScaleValue = document.getElementById('fontScaleValue');
  const positionGrid = document.getElementById('positionGrid');
  const generateBtn = document.getElementById('generateBtn');
  const clearBtn = document.getElementById('clearBtn');
  const exportBtn = document.getElementById('exportBtn');
  const hint = document.getElementById('hint');
  const textAlignRadios = document.querySelectorAll('input[name="textAlign"]');
  const sentenceOut = document.getElementById('sentenceOut');
  const canvas = document.getElementById('imageCanvas');
  const ctx = canvas.getContext('2d');

  let image = null;
  let clips = [];
  let drawMeta = { x: 0, y: 0, w: canvas.width, h: canvas.height };
  let selectedClipIndex = -1;
  let dragState = null;
  let sentenceDrag = null;

  function mode() {
    const m = document.querySelector('input[name="mode"]:checked');
    return m ? m.value : 'random';
  }

  function textAlignment() {
    const input = document.querySelector('input[name="textAlign"]:checked');
    return input ? input.value : 'left';
  }

  function updateLabels() {
    countValue.textContent = countInput.value;
    sizeValue.textContent = sizeInput.value + ' px';
    widthValue.textContent = widthInput.value + '%';
    heightValue.textContent = heightInput.value + '%';
    rotationValue.textContent = rotationInput.value + '°';
    fontScaleValue.textContent = (Number(fontScaleInput.value) / 100).toFixed(2) + 'x';
  }

  function getTextBlocks() {
    const raw = (baseText.value || '').replace(/\r/g, '');
    return raw.split(/\n\s*\n+/).map(block => block.split(/\n/)).filter(block => block.some(line => line.trim().length > 0));
  }

  function buildPositionGrid() {
    const blocks = getTextBlocks();
    positionGrid.innerHTML = '';

    let lineIndexGlobal = 0;
    blocks.forEach((block, blockIndex) => {
      block.forEach((line) => {
        const words = line.trim() ? line.split(/\s+/) : [];
        words.forEach((word, wordIndex) => {
          const button = document.createElement('button');
          button.type = 'button';
          button.className = 'position-cell';
          button.textContent = String(lineIndexGlobal + 1) + '.' + String(wordIndex + 1);
          button.title = 'Verso ' + (lineIndexGlobal + 1) + ', palabra ' + (wordIndex + 1) + ' — ' + word;
          button.dataset.blockIndex = String(blockIndex);
          button.dataset.lineIndex = String(lineIndexGlobal);
          button.dataset.wordIndex = String(wordIndex);
          button.addEventListener('click', function() {
            if (selectedClipIndex < 0 || !clips[selectedClipIndex]) {
              return;
            }
            clips[selectedClipIndex].blockIndex = Number(button.dataset.blockIndex);
            clips[selectedClipIndex].lineIndex = Number(button.dataset.lineIndex);
            clips[selectedClipIndex].wordIndex = Number(button.dataset.wordIndex);
            renderSentence();
            updatePositionGrid();
          });
          positionGrid.appendChild(button);
        });
        lineIndexGlobal += 1;
      });
      if (blocks.length > 1) {
        lineIndexGlobal += 1;
      }
    });
    updatePositionGrid();
  }

  function updatePositionGrid() {
    const buttons = positionGrid.querySelectorAll('.position-cell');
    buttons.forEach(button => {
      const lineIndex = Number(button.dataset.lineIndex);
      const wordIndex = Number(button.dataset.wordIndex);
      const blockIndex = Number(button.dataset.blockIndex || 0);
    const isActive = selectedClipIndex >= 0 && clips[selectedClipIndex] &&
        Number(clips[selectedClipIndex].blockIndex || 0) === blockIndex &&
        Number(clips[selectedClipIndex].lineIndex || 0) === lineIndex &&
        Number(clips[selectedClipIndex].wordIndex || 0) === wordIndex;
      button.classList.toggle('is-active', isActive);
    });
  }

  function syncSelectedClipControls() {
    if (selectedClipIndex < 0 || !clips[selectedClipIndex]) {
      return;
    }
    const clip = clips[selectedClipIndex];
    widthInput.value = String(Math.round((clip.widthScale || 1) * 100));
    heightInput.value = String(Math.round((clip.heightScale || 1) * 100));
    rotationInput.value = String(Math.round(clip.rotation || 0));
    updateLabels();
    updatePositionGrid();
  }

  function clearCanvas() {
    ctx.fillStyle = '#f2f4fa';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  }

  function fitDrawRect(img) {
    return {
      x: 0,
      y: 0,
      w: canvas.width,
      h: canvas.height
    };
  }

  function toCanvasRect(c) {
    const w = Math.max(18, c.size * (c.widthScale || 1));
    const h = Math.max(18, c.size * (c.heightScale || 1));
    return {
      x: drawMeta.x + c.rx * drawMeta.w - w / 2,
      y: drawMeta.y + c.ry * drawMeta.h - h / 2,
      w,
      h
    };
  }

  function drawImageAndMasks() {
    clearCanvas();
    if (!image) {
      return;
    }
    drawMeta = fitDrawRect(image);
    ctx.drawImage(image, drawMeta.x, drawMeta.y, drawMeta.w, drawMeta.h);

    ctx.save();
    clips.forEach((c, index) => {
      const r = toCanvasRect(c);
      ctx.save();
      ctx.translate(r.x + r.w / 2, r.y + r.h / 2);
      ctx.rotate((c.rotation || 0) * Math.PI / 180);
      ctx.fillStyle = selectedClipIndex === index ? '#f5f5f5' : '#f7f7f7';
      ctx.strokeStyle = selectedClipIndex === index ? '#111318' : '#d5d5d5';
      ctx.lineWidth = selectedClipIndex === index ? 2 : 1;
      ctx.fillRect(-r.w / 2, -r.h / 2, r.w, r.h);
      ctx.strokeRect(-r.w / 2, -r.h / 2, r.w, r.h);
      ctx.restore();

      if (selectedClipIndex === index) {
        const handleSize = 12;
        ctx.save();
        ctx.translate(r.x + r.w / 2, r.y + r.h / 2);
        ctx.rotate((c.rotation || 0) * Math.PI / 180);
        ctx.fillStyle = '#111318';
        ctx.fillRect(r.w / 2 - handleSize, r.h / 2 - handleSize, handleSize, handleSize);
        ctx.restore();
      }
    });
    ctx.restore();
  }

  function rand(min, max) {
    return Math.random() * (max - min) + min;
  }

  function sampleClipAt(rx, ry, sizePx, widthScale, heightScale) {
    const sx = Math.max(0, Math.min(image.width - 1, Math.floor(rx * image.width)));
    const sy = Math.max(0, Math.min(image.height - 1, Math.floor(ry * image.height)));

    const sourceWidth = Math.min(image.width, Math.max(12, Math.floor(sizePx * (widthScale || 1) * (image.width / drawMeta.w))));
    const sourceHeight = Math.min(image.height, Math.max(12, Math.floor(sizePx * (heightScale || 1) * (image.height / drawMeta.h))));
    const x = Math.max(0, Math.min(image.width - sourceWidth, sx - Math.floor(sourceWidth / 2)));
    const y = Math.max(0, Math.min(image.height - sourceHeight, sy - Math.floor(sourceHeight / 2)));

    const tmp = document.createElement('canvas');
    tmp.width = sourceWidth;
    tmp.height = sourceHeight;
    const tctx = tmp.getContext('2d');
    tctx.drawImage(image, x, y, sourceWidth, sourceHeight, 0, 0, sourceWidth, sourceHeight);

    const dataUrl = tmp.toDataURL('image/png');
    const img = new Image();
    img.src = dataUrl;

    return {
      rx,
      ry,
      size: sizePx,
      widthScale: 1,
      heightScale: 1,
      rotation: 0,
      blockIndex: 0,
      lineIndex: 0,
      wordIndex: 0,
      dataUrl,
      image: img
    };
  }

  function uniqueSlots(totalSlots, n) {
    const set = new Set();
    while (set.size < n && set.size < totalSlots) {
      set.add(Math.floor(Math.random() * totalSlots));
    }
    return Array.from(set).sort((a, b) => a - b);
  }

  function renderSentence() {
    const blocks = getTextBlocks();
    sentenceOut.innerHTML = '';
    sentenceOut.style.fontSize = (Number(fontScaleInput.value) / 100) + 'em';

    sentenceOut.style.transform = 'none';
    sentenceOut.style.width = '100%';
    sentenceOut.style.maxWidth = '100%';
    sentenceOut.style.textAlign = textAlignment();

    if (!blocks.length) {
      sentenceOut.innerHTML = '';
      return;
    }

    blocks.forEach((block, blockIndex) => {
      const blockWrap = document.createElement('div');
      blockWrap.className = 'sentence-line';
      blockWrap.style.textAlign = textAlignment();
      if (blockIndex > 0) {
        blockWrap.style.marginTop = '0.7em';
      }

      block.forEach((line, lineIndex) => {
        if (!line.trim()) {
          return;
        }
        const lineEl = document.createElement('div');
        lineEl.className = 'sentence-line';
        lineEl.style.textAlign = textAlignment();
        const words = line.trim().split(/\s+/);

        words.forEach((wordText, wordIndex) => {
          const assigned = clips.filter(clip => Number(clip.lineIndex || 0) === lineIndex && Number(clip.wordIndex || 0) === wordIndex && Number(clip.blockIndex || 0) === blockIndex);
          assigned.forEach((clip) => {
            const img = document.createElement('img');
            img.className = 'sentence-frag';
            img.src = clip.dataUrl;
            img.alt = 'fragmento';
            img.draggable = false;
            img.dataset.clipIndex = String(clips.indexOf(clip));
            img.title = 'Arrastra este fragmento a otra palabra';
            const w = Math.max(18, Math.floor((clip.size || 52) * (clip.widthScale || 1)));
            const h = Math.max(18, Math.floor((clip.size || 52) * (clip.heightScale || 1)));
            img.style.width = w + 'px';
            img.style.height = h + 'px';
            img.style.transform = 'rotate(' + (clip.rotation || 0) + 'deg)';
            img.style.transformOrigin = 'center center';
            lineEl.appendChild(img);
          });

          const word = document.createElement('span');
          const isActive = selectedClipIndex >= 0 && clips[selectedClipIndex] &&
            Number(clips[selectedClipIndex].blockIndex || 0) === blockIndex &&
            Number(clips[selectedClipIndex].lineIndex || 0) === lineIndex &&
            Number(clips[selectedClipIndex].wordIndex || 0) === wordIndex;
          word.className = 'sentence-word' + (isActive ? ' is-active' : '');
          word.textContent = wordText;
          word.dataset.blockIndex = String(blockIndex);
          word.dataset.lineIndex = String(lineIndex);
          word.dataset.wordIndex = String(wordIndex);
          word.title = 'Haz click para fijar este recorte en esta palabra';
          lineEl.appendChild(word);
        });

        blockWrap.appendChild(lineEl);
      });

      sentenceOut.appendChild(blockWrap);
    });

    sentenceOut.querySelectorAll('.sentence-word').forEach((el) => {
      el.addEventListener('click', function() {
        if (selectedClipIndex < 0 || !clips[selectedClipIndex]) {
          return;
        }
        const blockIndex = Number(el.dataset.blockIndex || 0);
        const lineIndex = Number(el.dataset.lineIndex || 0);
        const wordIndex = Number(el.dataset.wordIndex || 0);
        clips[selectedClipIndex].blockIndex = blockIndex;
        clips[selectedClipIndex].lineIndex = lineIndex;
        clips[selectedClipIndex].wordIndex = wordIndex;
        renderSentence();
        updatePositionGrid();
      });
    });

    sentenceOut.querySelectorAll('.sentence-frag').forEach((el) => {
      el.addEventListener('click', function() {
        selectedClipIndex = Number(el.dataset.clipIndex);
        syncSelectedClipControls();
        renderSentence();
        updatePositionGrid();
      });
      el.addEventListener('pointerdown', function(event) {
        if (event.button !== 0) {
          return;
        }
        event.preventDefault();
        const clipIndex = Number(el.dataset.clipIndex);
        selectedClipIndex = clipIndex;
        const ghost = el.cloneNode(true);
        ghost.classList.add('sentence-drag-ghost');
        ghost.style.width = el.getBoundingClientRect().width + 'px';
        ghost.style.height = el.getBoundingClientRect().height + 'px';
        document.body.appendChild(ghost);
        el.classList.add('is-dragging');
        sentenceDrag = {
          clipIndex,
          element: el,
          ghost,
          target: null,
          offsetX: el.getBoundingClientRect().width / 2,
          offsetY: el.getBoundingClientRect().height / 2
        };
        moveSentenceDrag(event);
      });
    });
  }

  function moveSentenceDrag(event) {
    if (!sentenceDrag) {
      return;
    }
    sentenceDrag.ghost.style.left = (event.clientX - sentenceDrag.offsetX) + 'px';
    sentenceDrag.ghost.style.top = (event.clientY - sentenceDrag.offsetY) + 'px';
    const underPointer = document.elementFromPoint(event.clientX, event.clientY);
    const target = underPointer && underPointer.closest ? underPointer.closest('.sentence-word') : null;
    if (sentenceDrag.target && sentenceDrag.target !== target) {
      sentenceDrag.target.classList.remove('is-drop-target');
    }
    sentenceDrag.target = target && sentenceOut.contains(target) ? target : null;
    if (sentenceDrag.target) {
      sentenceDrag.target.classList.add('is-drop-target');
    }
  }

  function finishSentenceDrag() {
    if (!sentenceDrag) {
      return;
    }
    const currentDrag = sentenceDrag;
    sentenceDrag = null;
    currentDrag.element.classList.remove('is-dragging');
    if (currentDrag.target) {
      currentDrag.target.classList.remove('is-drop-target');
      const clip = clips[currentDrag.clipIndex];
      if (clip) {
        clip.blockIndex = Number(currentDrag.target.dataset.blockIndex || 0);
        clip.lineIndex = Number(currentDrag.target.dataset.lineIndex || 0);
        clip.wordIndex = Number(currentDrag.target.dataset.wordIndex || 0);
        syncSelectedClipControls();
      }
    }
    currentDrag.ghost.remove();
    renderSentence();
    updatePositionGrid();
  }

  function generateRandom() {
    if (!image) {
      return;
    }
    clips = [];
    const count = Number(countInput.value);
    const size = Number(sizeInput.value);
    for (let i = 0; i < count; i++) {
      const rx = rand(0.08, 0.92);
      const ry = rand(0.08, 0.92);
      clips.push(sampleClipAt(rx, ry, size));
    }
    selectedClipIndex = -1;
    drawImageAndMasks();
    renderSentence();
  }

  function clearAll() {
    clips = [];
    selectedClipIndex = -1;
    sentenceOut.textContent = '';
    drawImageAndMasks();
  }

  function getCanvasPoint(ev) {
    const rect = canvas.getBoundingClientRect();
    return {
      x: ((ev.clientX - rect.left) / rect.width) * canvas.width,
      y: ((ev.clientY - rect.top) / rect.height) * canvas.height
    };
  }

  function findClipAt(x, y) {
    for (let i = clips.length - 1; i >= 0; i--) {
      const clip = clips[i];
      const r = toCanvasRect(clip);
      const angle = -(clip.rotation || 0) * Math.PI / 180;
      const dx = x - (r.x + r.w / 2);
      const dy = y - (r.y + r.h / 2);
      const localX = dx * Math.cos(angle) - dy * Math.sin(angle);
      const localY = dx * Math.sin(angle) + dy * Math.cos(angle);
      const handleHit = 18;
      const onHandle = localX >= r.w / 2 - handleHit && localX <= r.w / 2 + 6 &&
        localY >= r.h / 2 - handleHit && localY <= r.h / 2 + 6;
      if (onHandle) {
        return { index: i, action: 'resize' };
      }
      if (Math.abs(localX) <= r.w / 2 && Math.abs(localY) <= r.h / 2) {
        return { index: i, action: 'move' };
      }
    }
    return { index: -1, action: null };
  }

  function addClipAtPoint(x, y) {
    if (!image) {
      return;
    }
    if (x < drawMeta.x || y < drawMeta.y || x > drawMeta.x + drawMeta.w || y > drawMeta.y + drawMeta.h) {
      return;
    }

    const rx = (x - drawMeta.x) / drawMeta.w;
    const ry = (y - drawMeta.y) / drawMeta.h;
    const size = Number(sizeInput.value);

    if (clips.length >= Number(countInput.value)) {
      clips.shift();
      selectedClipIndex = Math.max(-1, selectedClipIndex - 1);
    }

    clips.push(sampleClipAt(rx, ry, size));
    selectedClipIndex = clips.length - 1;
    drawImageAndMasks();
    renderSentence();
  }

  function onCanvasPointerDown(ev) {
    if (!image) {
      return;
    }

    const p = getCanvasPoint(ev);
    const hit = findClipAt(p.x, p.y);

    if (mode() === 'manual') {
      if (hit.index >= 0) {
        selectedClipIndex = hit.index;
        dragState = {
          index: hit.index,
          action: hit.action,
          startX: p.x,
          startY: p.y,
          baseRx: clips[hit.index].rx,
          baseRy: clips[hit.index].ry,
          baseWidthScale: clips[hit.index].widthScale || 1,
          baseHeightScale: clips[hit.index].heightScale || 1
        };
      } else {
        addClipAtPoint(p.x, p.y);
      }
    } else if (hit.index >= 0) {
      selectedClipIndex = hit.index;
      dragState = {
        index: hit.index,
        action: hit.action,
        startX: p.x,
        startY: p.y,
        baseRx: clips[hit.index].rx,
        baseRy: clips[hit.index].ry,
        baseWidthScale: clips[hit.index].widthScale || 1,
        baseHeightScale: clips[hit.index].heightScale || 1
      };
    }

    if (dragState) {
      canvas.setPointerCapture(ev.pointerId);
    }
    syncSelectedClipControls();
    drawImageAndMasks();
  }

  function onCanvasPointerMove(ev) {
    if (!dragState || !image) {
      return;
    }

    const p = getCanvasPoint(ev);
    const clip = clips[dragState.index];

    const dx = p.x - dragState.startX;
    const dy = p.y - dragState.startY;

    if (dragState.action === 'resize') {
      const angle = -(clip.rotation || 0) * Math.PI / 180;
      const localDx = dx * Math.cos(angle) - dy * Math.sin(angle);
      const localDy = dx * Math.sin(angle) + dy * Math.cos(angle);
      clip.widthScale = Math.max(0.4, Math.min(1.8, dragState.baseWidthScale + localDx / clip.size));
      clip.heightScale = Math.max(0.4, Math.min(1.8, dragState.baseHeightScale + localDy / clip.size));
      widthInput.value = String(Math.round(clip.widthScale * 100));
      heightInput.value = String(Math.round(clip.heightScale * 100));
    } else {
      clip.rx = Math.max(0.03, Math.min(0.97, dragState.baseRx + dx / drawMeta.w));
      clip.ry = Math.max(0.03, Math.min(0.97, dragState.baseRy + dy / drawMeta.h));
    }

    updateLabels();
    drawImageAndMasks();
    renderSentence();
  }

  function onCanvasPointerUp(ev) {
    if (ev && canvas.hasPointerCapture(ev.pointerId)) {
      canvas.releasePointerCapture(ev.pointerId);
    }
    dragState = null;
    if (selectedClipIndex >= 0) {
      const clip = clips[selectedClipIndex];
      clip.dataUrl = sampleClipAt(clip.rx, clip.ry, clip.size, clip.widthScale, clip.heightScale).dataUrl;
      renderSentence();
    }
  }

  function exportComposition() {
    const exportCanvas = document.createElement('canvas');
    const topHeight = Math.max(180, sentenceOut.scrollHeight || 220);
    const totalWidth = canvas.width;
    const padding = 30;
    exportCanvas.width = totalWidth + padding * 2;
    exportCanvas.height = canvas.height + topHeight + padding * 2;
    const ectx = exportCanvas.getContext('2d');

    ectx.fillStyle = '#edf1f8';
    ectx.fillRect(0, 0, exportCanvas.width, exportCanvas.height);

    const sentenceRect = sentenceOut.getBoundingClientRect();
    const elements = Array.from(sentenceOut.querySelectorAll('.sentence-word, .sentence-frag'));
    const imageElements = elements.filter(element => element.classList.contains('sentence-frag'));
    const imagePromises = imageElements.map(element => new Promise(resolve => {
      if (element.complete) {
        resolve();
        return;
      }
      element.onload = resolve;
      element.onerror = resolve;
    }));

    function drawTextWithSpacing(text, x, y, style) {
      const letterSpacing = parseFloat(style.letterSpacing) || 0;
      ectx.font = style.font;
      ectx.fillStyle = style.color;
      ectx.textBaseline = 'top';
      if (!letterSpacing) {
        ectx.fillText(text, x, y);
        return;
      }

      let cursorX = x;
      Array.from(text).forEach(character => {
        ectx.fillText(character, cursorX, y);
        cursorX += ectx.measureText(character).width + letterSpacing;
      });
    }

    Promise.all(imagePromises).then(function() {
      elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const x = rect.left - sentenceRect.left;
        const y = rect.top - sentenceRect.top;
        const style = window.getComputedStyle(element);

        if (element.classList.contains('sentence-frag')) {
          ectx.drawImage(element, padding + x, padding + y, rect.width, rect.height);
        } else {
          drawTextWithSpacing(element.textContent, padding + x, padding + y, style);
        }
      });

      const previousSelection = selectedClipIndex;
      selectedClipIndex = -1;
      drawImageAndMasks();
      ectx.drawImage(canvas, padding, padding + topHeight, canvas.width, canvas.height);
      selectedClipIndex = previousSelection;
      drawImageAndMasks();

      const a = document.createElement('a');
      a.href = exportCanvas.toDataURL('image/png');
      a.download = 'fragmentos-export.png';
      a.click();
    });
  }

  function loadImage(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
      const img = new Image();
      img.onload = function() {
        image = img;
        const maxWidth = 1000;
        const ratio = img.width / img.height;
        const targetWidth = Math.min(img.width, maxWidth);
        canvas.width = Math.round(targetWidth);
        canvas.height = Math.round(targetWidth / ratio);
        canvas.style.width = '100%';
        canvas.style.maxWidth = maxWidth + 'px';

        const wrapper = canvas.parentElement;
        const topPanel = wrapper.querySelector('.canvas-top');
        if (topPanel) {
          topPanel.style.width = canvas.width + 'px';
          topPanel.style.maxWidth = '100%';
          topPanel.style.height = Math.max(170, Math.round(canvas.height * 0.78)) + 'px';
        }

        clearAll();
        drawImageAndMasks();
        if (mode() === 'random') {
          generateRandom();
        }
      };
      img.src = String(e.target.result);
    };
    reader.readAsDataURL(file);
  }

  imgInput.addEventListener('change', function(e) {
    const file = e.target.files && e.target.files[0];
    if (file) {
      loadImage(file);
    }
  });

  generateBtn.addEventListener('click', function() {
    if (mode() === 'random') {
      generateRandom();
    } else {
      hint.textContent = 'Modo manual activo: arrastra cualquier corte para moverlo y ajustarlo.';
      renderSentence();
    }
  });

  document.getElementById('selectBtn').addEventListener('click', function() {
    if (clips.length > 0) {
      selectedClipIndex = (selectedClipIndex + 1) % clips.length;
      syncSelectedClipControls();
      drawImageAndMasks();
      renderSentence();
    }
  });

  clearBtn.addEventListener('click', clearAll);
  exportBtn.addEventListener('click', exportComposition);

  baseText.addEventListener('input', function() {
    buildPositionGrid();
    updateLabels();
    renderSentence();
  });
  fontScaleInput.addEventListener('input', function() {
    updateLabels();
    renderSentence();
  });
  countInput.addEventListener('input', updateLabels);
  sizeInput.addEventListener('input', function() {
    updateLabels();
    if (selectedClipIndex >= 0 && clips[selectedClipIndex]) {
      const clip = clips[selectedClipIndex];
      clip.size = Number(sizeInput.value);
      clip.dataUrl = sampleClipAt(clip.rx, clip.ry, clip.size, clip.widthScale, clip.heightScale).dataUrl;
      drawImageAndMasks();
      renderSentence();
    }
    if (mode() === 'random' && image) {
      generateRandom();
    }
  });
  widthInput.addEventListener('input', function() {
    updateLabels();
    if (selectedClipIndex >= 0 && clips[selectedClipIndex]) {
      const clip = clips[selectedClipIndex];
      clip.widthScale = Number(widthInput.value) / 100;
      clip.dataUrl = sampleClipAt(clip.rx, clip.ry, clip.size, clip.widthScale, clip.heightScale).dataUrl;
      drawImageAndMasks();
      renderSentence();
    }
  });
  heightInput.addEventListener('input', function() {
    updateLabels();
    if (selectedClipIndex >= 0 && clips[selectedClipIndex]) {
      const clip = clips[selectedClipIndex];
      clip.heightScale = Number(heightInput.value) / 100;
      clip.dataUrl = sampleClipAt(clip.rx, clip.ry, clip.size, clip.widthScale, clip.heightScale).dataUrl;
      drawImageAndMasks();
      renderSentence();
    }
  });
  rotationInput.addEventListener('input', function() {
    updateLabels();
    if (selectedClipIndex >= 0 && clips[selectedClipIndex]) {
      clips[selectedClipIndex].rotation = Number(rotationInput.value);
      drawImageAndMasks();
      renderSentence();
    }
  });
  document.querySelectorAll('input[name="mode"]').forEach(el => {
    el.addEventListener('change', function() {
      const m = mode();
      if (m === 'manual') {
        hint.textContent = 'Modo manual activo: haz click para crear recortes y arrastralos para moverlos.';
      } else {
        hint.textContent = 'Tip: en modo manual, haz click sobre la imagen para agregar recortes.';
        if (image) {
          generateRandom();
        }
      }
    });
  });

  textAlignRadios.forEach(el => {
    el.addEventListener('change', function() {
      renderSentence();
    });
  });

  canvas.addEventListener('pointerdown', onCanvasPointerDown);
  canvas.addEventListener('pointermove', onCanvasPointerMove);
  canvas.addEventListener('pointerup', onCanvasPointerUp);
  canvas.addEventListener('pointercancel', onCanvasPointerUp);
  document.addEventListener('pointermove', moveSentenceDrag);
  document.addEventListener('pointerup', finishSentenceDrag);
  document.addEventListener('pointercancel', finishSentenceDrag);

  buildPositionGrid();
  updateLabels();
  clearCanvas();
})();
</script>
