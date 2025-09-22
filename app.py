import subprocess
import os
from tkinter import Tk, filedialog

def convertir_mp4_a_mp3():
    # Ocultar la ventana principal de Tkinter
    Tk().withdraw()

    # Abrir explorador de archivos para elegir el MP4
    mp4_file = filedialog.askopenfilename(
        title="Selecciona un archivo MP4",
        filetypes=[("Archivos MP4", "*.mp4")]
    )

    if not mp4_file:
        print("❌ No seleccionaste ningún archivo.")
        return

    # Generar la ruta de salida en la misma carpeta con extensión .mp3
    mp3_file = os.path.splitext(mp4_file)[0] + ".mp3"

    print(f"🎬 Convirtiendo:\n{mp4_file}\n➡️ {mp3_file}")

    # Ejecutar ffmpeg para extraer el audio en MP3 (rápido, sin re-encode innecesario)
    subprocess.run([
        "ffmpeg", "-y", "-i", mp4_file,
        "-vn", "-acodec", "libmp3lame", "-q:a", "2", mp3_file
    ], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    print("✅ Conversión completada.")

if __name__ == "__main__":
    convertir_mp4_a_mp3()
