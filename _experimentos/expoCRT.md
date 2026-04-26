
# Expo CRT

Para planear la ejecución de la expo hubo tres aspectos principales:

- Bocina
- Tele CRT, que solo tenía el puerto de video color amarillo
- DVD, que no incluía bocinas y por eso se agregó una pasiva

Para quemar el disco en formato MPG-2 se hicieron dos conversiones: primero para estandarizar el tamaño a 4:3 en MP4 y luego para convertirlo a MPG-2.

No todos los archivos eran videos. Se incluyeron dos imagenes que fueron convertidas a MP4 usando el mismo proceso de normalización para que se vieran bien en la Tele CRT:

```bash
ffmpeg -loop 1 -i imagen.jpg -vf "scale=720:540,pad=720:540:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -t 10 -pix_fmt yuv420p imagen.mp4
```

Este comando hace varias cosas a la vez:

- `-loop 1` deja la imagen fija para que se comporte como video.
- `-i imagen.jpg` toma la imagen original.
- `-vf` aplica el filtro de video.
- `scale=720:540` la ajusta a tamaño 4:3.
- `pad=720:540:(ow-iw)/2:(oh-ih)/2` la centra y rellena el espacio que haga falta.
- `-c:v libx264` la convierte a video MP4 con H.264.
- `-t 10` hace que el clip dure 10 segundos.
- `-pix_fmt yuv420p` deja el archivo en un formato más compatible con reproductores viejos.

En pocas palabras, ese comando agarra una foto y la vuelve un video corto que no se deforma en la Tele CRT.

Para quemar el DVD, la verdad sí me desesperé un poco. Si había una alternativa más interesante y que no fuera un dolor de huevos, no la encontré a tiempo; al final usé una máquina virtual de Windows, abrí el Media Player y fue bien simple.

## 3. Quemar el DVD en Windows

Lo que hice fue básicamente esto:

- abrir la máquina virtual de Windows;
- correr el archivo ya convertido en MPG-2;
- usar el Media Player para hacer la grabación.

Al final fue la salida más directa porque no tuve que pelearme con otra herramienta rara. Solo abrí el archivo, lo mandé al disco y ya.

## Comandos de ejemplo

### 1. Convertir todos los videos del folder a MP4 en formato 4:3

```bash
for input in *.mov *.mp4 *.mkv; do
  [ -e "$input" ] || continue
  ffmpeg -i "$input" -vf "scale='if(gt(a,4/3),720,-1)':'if(gt(a,4/3),-1,540)',pad=720:540:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -c:a aac "${input%.*}_4_3.mp4"
done
```

Este comando agarra todos los videos del folder y los deja en 4:3 uno por uno.

- `for input in *.mov *.mp4 *.mkv` recorre los videos del folder.
- `[ -e "$input" ] || continue` evita que falle si no hay archivos que coincidan.
- `-i "$input"` es el archivo de entrada en cada vuelta.
- `scale='if(gt(a,4/3),720,-1)':'if(gt(a,4/3),-1,540)'` usa `if` para decidir qué lado fijar según la proporción del video.
- `pad=720:540:(ow-iw)/2:(oh-ih)/2` evita que el video quede estirado y lo centra dentro del cuadro.
- `-c:v libx264` comprime el video en MP4.
- `-c:a aac` convierte el audio a AAC.

La idea era dejar todo en un formato estable para la Tele CRT antes de hacer la segunda conversión, sin andar peleándose con videos que no venían exactamente en 4:3.

### 2. Convertir de MP4 a MPG-2

```bash
ffmpeg -i salida_4_3.mp4 -target dvd -c:v mpeg2video -c:a ac3 salida.mpg
```

Este comando convierte el archivo ya normalizado a MPG-2, que fue el formato usado para quemar el disco.

- `-i salida_4_3.mp4` usa el archivo ya corregido.
- `-target dvd` aplica una configuración pensada para DVD.
- `-c:v mpeg2video` cambia el video a MPEG-2.
- `-c:a ac3` cambia el audio a AC3.

Así se obtiene un video compatible con reproducción en DVD y pantallas CRT.

La Tele CRT solo tenía entrada de video compuesto en color amarillo, así que la señal se conectó por ese puerto.

### Resumen

- Primero se ajusta el video al formato 4:3.
- Después se convierte a MPG-2 para grabarlo en disco.
- El objetivo final es asegurar que la reproducción funcione bien en la bocina, la Tele CRT y el DVD.
- Como el DVD no traía bocinas incluidas, se requirió agregar una bocina pasiva.
