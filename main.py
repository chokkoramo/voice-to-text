from config import AUDIO_PATH, MODEL_SIZE, LANGUAGE, CHUNK_LENGTH_MS, EXPORT_SRT
from processor.audio_loader import load_audio
from processor.chunker import split_audio
from processor.transcriber import transcribe_chunks
from processor.utils import clear_temp_chunks
from output.save_text import save_text, save_srt

def main():
    print("Cargando audio desde 'audios/'...")
    audio = load_audio(AUDIO_PATH)

    print("Dividiendo en fragmentos...")
    chunks = split_audio(audio, CHUNK_LENGTH_MS)

    print("Iniciando transcripción...")
    text, srt = transcribe_chunks(
        chunks, model_name=MODEL_SIZE, language=LANGUAGE, export_srt=EXPORT_SRT
    )

    print("Guardando resultados en carpeta 'texto/'...")
    txt_file = save_text(text, AUDIO_PATH)
    srt_file = None
    if EXPORT_SRT:
        srt_file = save_srt(srt, AUDIO_PATH)

    print("Proceso finalizado.")
    print(f"   - Transcripción: {txt_file}")
    if EXPORT_SRT:
        print(f"   - Subtítulos: {srt_file}")

if __name__ == "__main__":
    main()
    clear_temp_chunks()
