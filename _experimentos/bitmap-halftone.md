---
title: "Bitmap - Efecto Halftone"
layout: bitmap-halftone
date: 2025-10-07
show_full_date: false
permalink: /experimentos/bitmap-halftone/
categoria: procesamiento de imagen
autor: Carlos Wolf
---

### Proceso de Conversión a Escala de Grises

```javascript
const gray = 0.299 * R + 0.587 * G + 0.114 * B;
```

Esta fórmula refleja la sensibilidad del ojo humano a diferentes colores usando la formula de ITU-R BT.709 

### Detección Automática de Fondos

El algoritmo utiliza un análisis de colores para detectar el fondo de la imagen si es que asi se prefiere usando un promedio del color de los pixeles en la foto

```python
from collections import Counter
color_counts = Counter(pixels)
bg_color = color_counts.most_common(1)[0][0]
```

### Pixelación en el Proceso Halftone

El proceso de pixelación se basa en el algoritmo usado en la libreria de **PIL**, donde la imagen se reduce gradualmente antes de ser convertida a un formato de **1-bit** (blanco y negro):

```python
small = image.resize((w // scale, h // scale), BILINEAR)
binary = small.convert("1")  # Conversión a 1-bit
result = binary.resize(original_size, NEAREST)
```

<div id="pixelate-app">
    <!-- Upload Area -->
    <div class="upload-section">
        <div class="upload-area" id="uploadArea">
            <div class="upload-content">
                <div class="upload-icon">IMAGE</div>
                <h3>Arrastra tu imagen aquí</h3>
                <p>o <span class="browse-link">navega por archivos</span></p>
                <input type="file" id="fileInput" accept="image/*" style="display: none;">
            </div>
        </div>
        
        <!-- Camera Controls -->
        <div class="camera-section">
            <div class="camera-controls">
                <button id="startCameraBtn" class="camera-btn">Iniciar Cámara</button>
                <button id="stopCameraBtn" class="camera-btn" style="display: none;">Detener Cámara</button>
                <button id="captureBtn" class="camera-btn" style="display: none;">Capturar Foto</button>
            </div>
            <video id="cameraVideo" autoplay muted style="display: none; max-width: 100%; border-radius: 8px; margin-top: 1em;"></video>
        </div>
    </div>

    <!-- Controls -->
    <div class="controls-section" id="controlsSection" style="display: none;">
        <h4>Configuración del Efecto</h4>
        <div class="controls-grid">
            <div class="control-group">
                <label for="pixelScale">Tamaño de Píxel: <span id="pixelScaleValue">3</span></label>
                <input type="range" id="pixelScale" min="1.0" max="15.0" value="3.0" step="0.1">
                <small>Tamaño del efecto pixelado</small>
            </div>
            <div class="control-group">
                <label for="pixelStyle">Estilo de Píxel: <span id="pixelStyleValue">Cuadrado</span></label>
                <input type="range" id="pixelStyle" min="0" max="2" value="0" step="1">
                <small>Forma del patrón halftone</small>
            </div>
            <div class="control-group">
                <label for="contrast">Contraste: <span id="contrastValue">3</span></label>
                <input type="range" id="contrast" min="1" max="5" value="3" step="0.1">
                <small>Intensidad del contraste</small>
            </div>
            <div class="control-group">
                <label for="colorDepth">Profundidad de Color: <span id="colorDepthValue">2</span></label>
                <input type="range" id="colorDepth" min="2" max="64" value="2" step="1">
                <small>Niveles de gris disponibles</small>
            </div>
            <div class="control-group">
                <label for="tolerance">Tolerancia Fondo: <span id="toleranceValue">30</span></label>
                <input type="range" id="tolerance" min="0" max="100" value="30" step="5">
                <small>Sensibilidad de detección de fondo</small>
            </div>
            <div class="control-group">
                <label>
                    <input type="checkbox" id="removeBackground" checked>
                    Remover Fondo
                </label>
            </div>
        </div>
    </div>

    <!-- Preview -->
    <div class="preview-section" id="previewSection" style="display: none;">
        <div class="preview-grid">
            <div class="preview-item">
                <h4>Original</h4>
                <canvas id="originalCanvas"></canvas>
            </div>
            <div class="preview-item">
                <h4>Bitmap Effect</h4>
                <canvas id="processedCanvas"></canvas>
                <div class="download-section">
                    <button id="downloadBtn" disabled>Descargar</button>
                </div>
            </div>
        </div>
    </div>

    <div id="statusMessage" style="display: none;"></div>
</div>
