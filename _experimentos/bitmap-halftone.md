---
title: "Bitmap - Efecto Halftone"
layout: experimento
date: 2025-10-07
show_full_date: false
permalink: /experimentos/bitmap-halftone/
categoria: procesamiento de imagen
autor: Carlos Wolf
---

Un experimento interactivo para convertir imágenes en efectos bitmap/halftone en tiempo real. Sube una imagen y observa cómo se transforma en puntos y patrones que recrean el efecto clásico de impresión periodística.

### Cómo usar:
1. **Arrastra una imagen** o haz clic para seleccionar
2. **Ajusta los controles** para experimentar con diferentes efectos
3. **Descarga el resultado** cuando estés satisfecho

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
                <small>1.0-2.0: Ultra fino | 2.0-4.0: Fino | 4.0-8.0: Medio | 8.0-15.0: Grueso</small>
            </div>
            <div class="control-group">
                <label for="pixelStyle">Estilo de Píxel: <span id="pixelStyleValue">Cuadrado</span></label>
                <input type="range" id="pixelStyle" min="0" max="2" value="0" step="1">
                <small>Cuadrado → Círculo → Diamante</small>
            </div>
            <div class="control-group">
                <label for="contrast">Contraste: <span id="contrastValue">3</span></label>
                <input type="range" id="contrast" min="1" max="5" value="3" step="0.1">
                <small>Separación de tonos claros y oscuros</small>
            </div>
            <div class="control-group">
                <label for="colorDepth">Profundidad de Color: <span id="colorDepthValue">2</span></label>
                <input type="range" id="colorDepth" min="2" max="64" value="2" step="1">
                <small>2: Blanco/Negro | 8: 8 grises | 16: 16 grises | 32: 32 grises | 64: Ultra suave</small>
            </div>
            <div class="control-group">
                <label for="tolerance">Tolerancia Fondo: <span id="toleranceValue">30</span></label>
                <input type="range" id="tolerance" min="0" max="100" value="30" step="5">
                <small>Sensibilidad para remover fondo</small>
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

<style>
#pixelate-app {
    max-width: 100%;
    margin: 2em 0;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.upload-area {
    border: 3px dashed #0056b3;
    border-radius: 12px;
    padding: 3em 2em;
    text-align: center;
    background: #f8f9ff;
    transition: all 0.3s ease;
    cursor: pointer;
    margin: 1em 0;
}

.upload-area:hover, .upload-area.dragover {
    border-color: #ff6b6b;
    background: #fff5f5;
}

.upload-icon {
    font-size: 3em;
    margin-bottom: 0.5em;
}

.browse-link {
    color: #0056b3;
    cursor: pointer;
    text-decoration: underline;
}

.camera-section {
    margin-top: 1em;
    text-align: center;
}

.camera-controls {
    display: flex;
    gap: 1em;
    justify-content: center;
    flex-wrap: wrap;
}

.camera-btn {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background 0.3s ease;
}

.camera-btn:hover {
    background: #218838;
}

.camera-btn:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

#cameraVideo {
    border: 2px solid #0056b3;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.controls-section {
    background: #f8f9ff;
    padding: 1.5em;
    border-radius: 12px;
    margin: 1em 0;
}

.controls-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1em;
    margin: 1em 0;
}

.control-group label {
    display: block;
    margin-bottom: 0.5em;
    font-weight: 600;
}

.control-group input[type="range"] {
    width: 100%;
    margin-bottom: 0.5em;
}

.preview-section {
    margin: 2em 0;
}

.preview-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2em;
    margin: 1em 0;
}

@media (max-width: 768px) {
    .preview-grid {
        grid-template-columns: 1fr;
    }
}

.preview-item {
    text-align: center;
}

.preview-item h4 {
    margin-bottom: 1em;
    color: #0056b3;
}

.preview-item canvas {
    max-width: 100%;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.download-section {
    margin-top: 1em;
}

#downloadBtn {
    background: #0056b3;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
}

#downloadBtn:hover:not(:disabled) {
    background: #004494;
}

#downloadBtn:disabled {
    background: #ccc;
    cursor: not-allowed;
}

#statusMessage {
    padding: 1em;
    border-radius: 6px;
    margin: 1em 0;
    text-align: center;
}

#statusMessage.success {
    background: #d4edda;
    color: #155724;
    border: 1px solid #c3e6cb;
}

#statusMessage.error {
    background: #f8d7da;
    color: #721c24;
    border: 1px solid #f5c6cb;
}
</style>

<script>
class BitmapProcessor {
    constructor() {
        this.currentImageData = null;
        this.initializeElements();
        this.bindEvents();
    }

    initializeElements() {
        this.uploadArea = document.getElementById('uploadArea');
        this.fileInput = document.getElementById('fileInput');
        this.controlsSection = document.getElementById('controlsSection');
        this.previewSection = document.getElementById('previewSection');
        this.originalCanvas = document.getElementById('originalCanvas');
        this.processedCanvas = document.getElementById('processedCanvas');
        // Canvas oculto para descarga de alta calidad
        this.downloadCanvas = document.createElement('canvas');
        this.downloadCanvas.style.display = 'none';
        document.body.appendChild(this.downloadCanvas);
        
        this.pixelScale = document.getElementById('pixelScale');
        this.pixelScaleValue = document.getElementById('pixelScaleValue');
        this.pixelStyle = document.getElementById('pixelStyle');
        this.pixelStyleValue = document.getElementById('pixelStyleValue');
        this.contrast = document.getElementById('contrast');
        this.contrastValue = document.getElementById('contrastValue');
        this.colorDepth = document.getElementById('colorDepth');
        this.colorDepthValue = document.getElementById('colorDepthValue');
        this.tolerance = document.getElementById('tolerance');
        this.toleranceValue = document.getElementById('toleranceValue');
        this.removeBackground = document.getElementById('removeBackground');
        this.downloadBtn = document.getElementById('downloadBtn');
        this.statusMessage = document.getElementById('statusMessage');
        
        // Camera elements
        this.cameraVideo = document.getElementById('cameraVideo');
        this.startCameraBtn = document.getElementById('startCameraBtn');
        this.stopCameraBtn = document.getElementById('stopCameraBtn');
        this.captureBtn = document.getElementById('captureBtn');
        this.cameraStream = null;
        this.isLiveMode = false;
    }

    bindEvents() {
        this.uploadArea.addEventListener('click', () => this.fileInput.click());
        this.uploadArea.addEventListener('dragover', (e) => this.handleDragOver(e));
        this.uploadArea.addEventListener('dragleave', (e) => this.handleDragLeave(e));
        this.uploadArea.addEventListener('drop', (e) => this.handleDrop(e));
        this.fileInput.addEventListener('change', (e) => this.handleFileSelect(e));
        
        this.pixelScale.addEventListener('input', () => this.updateControls());
        this.pixelStyle.addEventListener('input', () => this.updateControls());
        this.contrast.addEventListener('input', () => this.updateControls());
        this.colorDepth.addEventListener('input', () => this.updateControls());
        this.tolerance.addEventListener('input', () => this.updateControls());
        this.pixelScale.addEventListener('change', () => this.processImage());
        this.pixelStyle.addEventListener('change', () => this.processImage());
        this.contrast.addEventListener('change', () => this.processImage());
        this.colorDepth.addEventListener('change', () => this.processImage());
        this.tolerance.addEventListener('change', () => this.processImage());
        this.removeBackground.addEventListener('change', () => this.processImage());
        
        this.downloadBtn.addEventListener('click', () => this.downloadImage());
        
        // Camera events
        this.startCameraBtn.addEventListener('click', () => this.startCamera());
        this.stopCameraBtn.addEventListener('click', () => this.stopCamera());
        this.captureBtn.addEventListener('click', () => this.captureFrame());
        
        document.querySelector('.browse-link').addEventListener('click', () => this.fileInput.click());
    }

    updateControls() {
        this.pixelScaleValue.textContent = parseFloat(this.pixelScale.value).toFixed(1);
        const styleLabels = ['Cuadrado', 'Círculo', 'Diamante'];
        this.pixelStyleValue.textContent = styleLabels[this.pixelStyle.value];
        this.contrastValue.textContent = this.contrast.value;
        this.colorDepthValue.textContent = this.colorDepth.value;
        this.toleranceValue.textContent = this.tolerance.value;
    }

    handleDragOver(e) {
        e.preventDefault();
        this.uploadArea.classList.add('dragover');
    }

    handleDragLeave(e) {
        e.preventDefault();
        this.uploadArea.classList.remove('dragover');
    }

    handleDrop(e) {
        e.preventDefault();
        this.uploadArea.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            this.loadImage(files[0]);
        }
    }

    handleFileSelect(e) {
        const file = e.target.files[0];
        if (file) {
            this.loadImage(file);
        }
    }

    loadImage(file) {
        if (!file.type.startsWith('image/')) {
            this.showStatus('Por favor selecciona un archivo de imagen válido', 'error');
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
                this.displayOriginalImage(img);
                this.controlsSection.style.display = 'block';
                this.previewSection.style.display = 'block';
                setTimeout(() => this.processImage(), 100);
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }

    displayOriginalImage(img) {
        const canvas = this.originalCanvas;
        const ctx = canvas.getContext('2d');
        
        // Use original image dimensions without resizing
        const { width, height } = img;
        
        canvas.width = width;
        canvas.height = height;
        ctx.drawImage(img, 0, 0, width, height);
        
        this.currentImageData = ctx.getImageData(0, 0, width, height);
    }

    processImage() {
        if (!this.currentImageData) return;

        // Procesar preview comprimido para eficiencia
        this.processPreview();
        
        // Procesar versión completa para descarga
        this.processFullQuality();
        
        this.downloadBtn.disabled = false;
        this.showStatus('Imagen procesada exitosamente', 'success');
    }
    
    processPreview() {
        const canvas = this.processedCanvas;
        const ctx = canvas.getContext('2d');
        
        // Comprimir preview para eficiencia (máximo 400px)
        const maxPreviewSize = 400;
        let { width, height } = this.currentImageData;
        
        if (width > height) {
            if (width > maxPreviewSize) {
                height = (height * maxPreviewSize) / width;
                width = maxPreviewSize;
            }
        } else {
            if (height > maxPreviewSize) {
                width = (width * maxPreviewSize) / height;
                height = maxPreviewSize;
            }
        }
        
        canvas.width = width;
        canvas.height = height;
        
        // Crear nueva ImageData redimensionada
        const tempCanvas = document.createElement('canvas');
        const tempCtx = tempCanvas.getContext('2d');
        tempCanvas.width = this.currentImageData.width;
        tempCanvas.height = this.currentImageData.height;
        tempCtx.putImageData(this.currentImageData, 0, 0);
        
        // Redimensionar para preview
        ctx.drawImage(tempCanvas, 0, 0, width, height);
        const previewImageData = ctx.getImageData(0, 0, width, height);
        
        // Aplicar efecto bitmap al preview
        this.applyBitmapEffect(previewImageData);
        ctx.putImageData(previewImageData, 0, 0);
    }
    
    processFullQuality() {
        const canvas = this.downloadCanvas;
        const ctx = canvas.getContext('2d');
        
        // Usar dimensiones originales completas para descarga
        canvas.width = this.currentImageData.width;
        canvas.height = this.currentImageData.height;

        const imageData = new ImageData(
            new Uint8ClampedArray(this.currentImageData.data),
            this.currentImageData.width,
            this.currentImageData.height
        );

        // Aplicar efecto bitmap a resolución completa
        this.applyBitmapEffect(imageData);
        ctx.putImageData(imageData, 0, 0);
    }

    applyBitmapEffect(imageData) {
        const data = imageData.data;
        const width = imageData.width;
        const height = imageData.height;
        const pixelScale = Math.max(1, parseFloat(this.pixelScale.value));
        const pixelStyle = parseInt(this.pixelStyle.value); // 0=cuadrado, 1=círculo, 2=diamante
        const contrastFactor = parseFloat(this.contrast.value);
        const colorDepth = parseInt(this.colorDepth.value);
        const tolerance = parseInt(this.tolerance.value);
        const removeBackground = this.removeBackground.checked;

        // Crear canvas temporal para procesar con mayor calidad
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = width;
        canvas.height = height;
        
        // Configurar para máxima calidad
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';
        
        // Copiar imageData al canvas
        ctx.putImageData(imageData, 0, 0);
        
        if (removeBackground) {
            // Implementar detección de color de fondo como en PIL
            // Contar frecuencia de colores (implementación de Counter de Python)
            const colorMap = new Map();
            
            // Muestrear todos los píxeles para encontrar el color más común
            for (let i = 0; i < data.length; i += 4) {
                const r = data[i];
                const g = data[i + 1];
                const b = data[i + 2];
                const key = `${r},${g},${b}`;
                colorMap.set(key, (colorMap.get(key) || 0) + 1);
            }
            
            // Encontrar el color más común (background)
            let maxCount = 0;
            let bgColor = [255, 255, 255];
            for (const [colorKey, count] of colorMap) {
                if (count > maxCount) {
                    maxCount = count;
                    bgColor = colorKey.split(',').map(Number);
                }
            }
            
            // Remover fondo con tolerancia como en PIL
            for (let i = 0; i < data.length; i += 4) {
                const rDiff = Math.abs(data[i] - bgColor[0]);
                const gDiff = Math.abs(data[i + 1] - bgColor[1]);
                const bDiff = Math.abs(data[i + 2] - bgColor[2]);
                
                if (rDiff < tolerance && gDiff < tolerance && bDiff < tolerance) {
                    data[i + 3] = 0; // Hacer transparente
                }
            }
            
            // Aplicar fondo negro como en PIL: alpha_composite con fondo negro
            ctx.fillStyle = 'rgba(0, 0, 0, 0.98)'; // equivalente a (0, 0, 0, 250)
            ctx.fillRect(0, 0, width, height);
            ctx.globalCompositeOperation = 'source-over';
            ctx.putImageData(imageData, 0, 0);
        }
        
        // Convertir a escala de grises usando conversión de luminancia (como PIL)
        const grayData = ctx.getImageData(0, 0, width, height);
        const grayPixels = grayData.data;
        
        for (let i = 0; i < grayPixels.length; i += 4) {
            // Usar la misma conversión de luminancia que PIL
            const gray = Math.round(0.299 * grayPixels[i] + 0.587 * grayPixels[i + 1] + 0.114 * grayPixels[i + 2]);
            const contrasted = Math.min(255, Math.max(0, (gray - 128) * contrastFactor + 128));
            
            // Aplicar cuantización de color basada en colorDepth
            const quantized = this.quantizeColor(contrasted, colorDepth);
            
            grayPixels[i] = quantized;
            grayPixels[i + 1] = quantized;
            grayPixels[i + 2] = quantized;
        }
        
        ctx.putImageData(grayData, 0, 0);
        
        // Implementar el algoritmo PIL: resize -> convert("1") -> resize
        // Paso 1: Redimensionar hacia abajo (equivalente a PIL resize con BILINEAR)
        const smallWidth = Math.max(1, Math.floor(width / pixelScale));
        const smallHeight = Math.max(1, Math.floor(height / pixelScale));
        
        const smallCanvas = document.createElement('canvas');
        const smallCtx = smallCanvas.getContext('2d');
        smallCanvas.width = smallWidth;
        smallCanvas.height = smallHeight;
        
        // Usar interpolación bilinear (equivalente a PIL BILINEAR)
        smallCtx.imageSmoothingEnabled = true;
        smallCtx.imageSmoothingQuality = 'high';
        smallCtx.drawImage(canvas, 0, 0, smallWidth, smallHeight);
        
        // Paso 2: Para píxeles personalizados, preservar valores de gris
        // Para píxeles cuadrados, usar conversion a 1-bit tradicional
        if (pixelStyle === 0) {
            // Convertir a 1-bit (equivalente a PIL convert("1")) solo para cuadrados
            const smallImageData = smallCtx.getImageData(0, 0, smallWidth, smallHeight);
            const smallPixels = smallImageData.data;
            
            // Aplicar threshold simple como PIL convert("1")
            for (let i = 0; i < smallPixels.length; i += 4) {
                const gray = smallPixels[i]; // Ya está en escala de grises
                const binary = gray > 128 ? 255 : 0;
                smallPixels[i] = binary;
                smallPixels[i + 1] = binary;
                smallPixels[i + 2] = binary;
            }
            
            smallCtx.putImageData(smallImageData, 0, 0);
        }
        // Para círculos y diamantes, mantener los valores de gris originales
        
        // Paso 3: Redimensionar de vuelta (equivalente a PIL resize con NEAREST)
        ctx.imageSmoothingEnabled = false; // NEAREST interpolation
        ctx.clearRect(0, 0, width, height);
        
        // Si no son píxeles cuadrados, usar renderizado personalizado con valores de gris
        if (pixelStyle !== 0) {
            this.renderCustomPixels(ctx, smallCanvas, width, height, pixelScale, pixelStyle);
        } else {
            ctx.drawImage(smallCanvas, 0, 0, width, height);
        }
        
        // Copiar resultado final a imageData
        const finalData = ctx.getImageData(0, 0, width, height);
        for (let i = 0; i < data.length; i += 4) {
            data[i] = finalData.data[i];
            data[i + 1] = finalData.data[i + 1];
            data[i + 2] = finalData.data[i + 2];
            data[i + 3] = 255; // Alpha completo
        }
    }

    quantizeColor(value, levels) {
        // Cuantizar el valor de gris a un número específico de niveles
        // Usar una distribución más suave para niveles altos
        if (levels >= 32) {
            // Para niveles altos, usar cuantización más suave
            const step = 255 / (levels - 1);
            const quantized = Math.round(value / step) * step;
            return Math.min(255, Math.max(0, quantized));
        } else {
            // Para niveles bajos, usar cuantización más agresiva
            const step = 256 / levels;
            const quantized = Math.floor(value / step) * step + (step / 2);
            return Math.min(255, Math.max(0, quantized));
        }
    }

    renderCustomPixels(ctx, sourceCanvas, width, height, pixelScale, pixelStyle) {
        // Configurar fondo blanco
        ctx.fillStyle = 'white';
        ctx.fillRect(0, 0, width, height);
        
        // Mejorar calidad de renderizado para alta profundidad de color
        const colorDepth = parseInt(this.colorDepth.value);
        if (colorDepth >= 16) {
            ctx.imageSmoothingEnabled = true;
            ctx.imageSmoothingQuality = 'high';
        }
        
        // Obtener datos de la imagen procesada
        const sourceCtx = sourceCanvas.getContext('2d');
        const sourceData = sourceCtx.getImageData(0, 0, sourceCanvas.width, sourceCanvas.height);
        const pixels = sourceData.data;
        
        // Calcular la proporción entre la imagen original y la procesada
        const scaleX = width / sourceCanvas.width;
        const scaleY = height / sourceCanvas.height;
        
        // Tamaño máximo del pixel en la imagen final
        const maxPixelSize = Math.max(1, pixelScale * 0.9);
        
        // Recorrer cada pixel de la imagen procesada
        for (let y = 0; y < sourceCanvas.height; y++) {
            for (let x = 0; x < sourceCanvas.width; x++) {
                const index = (y * sourceCanvas.width + x) * 4;
                const brightness = pixels[index]; // Canal rojo (escala de grises)
                
                // Calcular el tamaño del punto basado en la intensidad del gris
                // brightness 0 (negro) = punto máximo
                // brightness 255 (blanco) = sin punto
                const intensity = 1.0 - (brightness / 255.0); // Invertir: más oscuro = más intenso
                const pointSize = intensity * maxPixelSize;
                
                // Solo dibujar si hay suficiente intensidad (evitar puntos microscópicos)
                if (pointSize > 0.1) {
                    const centerX = (x + 0.5) * scaleX;
                    const centerY = (y + 0.5) * scaleY;
                    
                    // Usar diferentes tonos de gris para diferentes niveles con interpolación suave
                    const colorDepth = parseInt(this.colorDepth.value);
                    let grayValue;
                    
                    if (colorDepth >= 32) {
                        // Para alta profundidad, usar valores más suaves
                        grayValue = Math.floor(brightness * 0.95 + 12); // Evitar extremos puros
                    } else {
                        // Para baja profundidad, usar cuantización más marcada
                        grayValue = Math.floor(brightness);
                    }
                    
                    grayValue = Math.min(255, Math.max(0, grayValue));
                    ctx.fillStyle = `rgb(${grayValue}, ${grayValue}, ${grayValue})`;
                    
                    if (pixelStyle === 1) {
                        // Círculo con tamaño variable y color variable
                        ctx.beginPath();
                        ctx.arc(centerX, centerY, pointSize / 2, 0, 2 * Math.PI);
                        ctx.fill();
                    } else if (pixelStyle === 2) {
                        // Diamante con tamaño variable y color variable
                        const halfSize = pointSize / 2;
                        ctx.beginPath();
                        ctx.moveTo(centerX, centerY - halfSize);
                        ctx.lineTo(centerX + halfSize, centerY);
                        ctx.lineTo(centerX, centerY + halfSize);
                        ctx.lineTo(centerX - halfSize, centerY);
                        ctx.closePath();
                        ctx.fill();
                    }
                }
            }
        }
    }

    downloadImage() {
        const link = document.createElement('a');
        link.download = 'bitmap-effect.png';
        // Usar máxima calidad PNG sin compresión desde el canvas completo
        link.href = this.downloadCanvas.toDataURL('image/png', 1.0);
        link.click();
    }

    showStatus(message, type) {
        this.statusMessage.textContent = message;
        this.statusMessage.className = type;
        this.statusMessage.style.display = 'block';
        
        if (type === 'success') {
            setTimeout(() => {
                this.statusMessage.style.display = 'none';
            }, 3000);
        }
    }

    async startCamera() {
        try {
            this.cameraStream = await navigator.mediaDevices.getUserMedia({ 
                video: { width: 640, height: 480 } 
            });
            
            this.cameraVideo.srcObject = this.cameraStream;
            this.cameraVideo.style.display = 'block';
            
            this.startCameraBtn.style.display = 'none';
            this.stopCameraBtn.style.display = 'inline-block';
            this.captureBtn.style.display = 'inline-block';
            
            this.isLiveMode = true;
            
            // Start live processing
            this.cameraVideo.addEventListener('loadedmetadata', () => {
                this.startLiveProcessing();
            });
            
            this.showStatus('Cámara iniciada exitosamente', 'success');
        } catch (error) {
            this.showStatus('Error al acceder a la cámara: ' + error.message, 'error');
            console.error('Camera error:', error);
        }
    }

    stopCamera() {
        if (this.cameraStream) {
            this.cameraStream.getTracks().forEach(track => track.stop());
            this.cameraStream = null;
        }
        
        this.cameraVideo.style.display = 'none';
        this.startCameraBtn.style.display = 'inline-block';
        this.stopCameraBtn.style.display = 'none';
        this.captureBtn.style.display = 'none';
        
        this.isLiveMode = false;
        
        if (this.liveProcessingInterval) {
            clearInterval(this.liveProcessingInterval);
        }
        
        this.showStatus('Cámara detenida', 'success');
    }

    captureFrame() {
        if (!this.cameraVideo.videoWidth) return;
        
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        
        canvas.width = this.cameraVideo.videoWidth;
        canvas.height = this.cameraVideo.videoHeight;
        
        ctx.drawImage(this.cameraVideo, 0, 0);
        
        // Convert to image and process
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        this.currentImageData = imageData;
        
        // Display captured frame in original canvas
        this.originalCanvas.width = canvas.width;
        this.originalCanvas.height = canvas.height;
        const originalCtx = this.originalCanvas.getContext('2d');
        originalCtx.putImageData(imageData, 0, 0);
        
        this.controlsSection.style.display = 'block';
        this.previewSection.style.display = 'block';
        
        this.processImage();
        this.showStatus('Foto capturada y procesada', 'success');
    }

    startLiveProcessing() {
        this.controlsSection.style.display = 'block';
        this.previewSection.style.display = 'block';
        
        // Process every 100ms for smooth live effect
        this.liveProcessingInterval = setInterval(() => {
            if (this.isLiveMode && this.cameraVideo.videoWidth > 0) {
                this.processLiveFrame();
            }
        }, 100);
    }

    processLiveFrame() {
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        
        canvas.width = this.cameraVideo.videoWidth;
        canvas.height = this.cameraVideo.videoHeight;
        
        ctx.drawImage(this.cameraVideo, 0, 0);
        
        // Get current frame
        const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        
        // Display original frame
        this.originalCanvas.width = canvas.width;
        this.originalCanvas.height = canvas.height;
        const originalCtx = this.originalCanvas.getContext('2d');
        originalCtx.putImageData(imageData, 0, 0);
        
        // Process for preview only (live mode)
        this.processLivePreview(imageData);
    }

    processLivePreview(imageData) {
        const canvas = this.processedCanvas;
        const ctx = canvas.getContext('2d');
        
        // Compress for live processing efficiency
        const maxPreviewSize = 320; // Smaller for live mode
        let { width, height } = imageData;
        
        if (width > height) {
            if (width > maxPreviewSize) {
                height = (height * maxPreviewSize) / width;
                width = maxPreviewSize;
            }
        } else {
            if (height > maxPreviewSize) {
                width = (width * maxPreviewSize) / height;
                height = maxPreviewSize;
            }
        }
        
        canvas.width = width;
        canvas.height = height;
        
        // Create resized image data
        const tempCanvas = document.createElement('canvas');
        const tempCtx = tempCanvas.getContext('2d');
        tempCanvas.width = imageData.width;
        tempCanvas.height = imageData.height;
        tempCtx.putImageData(imageData, 0, 0);
        
        // Resize for live preview
        ctx.drawImage(tempCanvas, 0, 0, width, height);
        const previewImageData = ctx.getImageData(0, 0, width, height);
        
        // Apply bitmap effect
        this.applyBitmapEffect(previewImageData);
        ctx.putImageData(previewImageData, 0, 0);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new BitmapProcessor();
});
</script>