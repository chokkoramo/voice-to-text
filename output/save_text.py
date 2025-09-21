import os

OUTPUT_DIR = "text_outputs"

def ensure_output_dir():
    """Crea la carpeta de salida si no existe."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def save_text(text: str, audio_filename: str):
    """Guarda transcripción en 'text_outputs/' con el mismo nombre del audio."""
    ensure_output_dir()
    base_name = os.path.splitext(os.path.basename(audio_filename))[0]
    file_path = os.path.join(OUTPUT_DIR, f"{base_name}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    return file_path

def save_srt(srt: str, audio_filename: str):
    """Guarda subtítulos en 'text_outputs/' con el mismo nombre del audio."""
    ensure_output_dir()
    base_name = os.path.splitext(os.path.basename(audio_filename))[0]
    file_path = os.path.join(OUTPUT_DIR, f"{base_name}.srt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(srt)
    return file_path
