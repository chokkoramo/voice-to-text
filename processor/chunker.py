import os
from pydub import AudioSegment
from config import TEMP_CHUNKS_PATH

def chunk_audio(audio: AudioSegment, chunk_length_ms: int):
    os.makedirs(TEMP_CHUNKS_PATH, exist_ok=True)
    chunks = []
    for i, start in enumerate(range(0, len(audio), chunk_length_ms)):
        end = min(start + chunk_length_ms, len(audio))
        chunk = audio[start:end]
        filename = os.path.join(TEMP_CHUNKS_PATH, f"chunk_{i}.wav")
        chunk.export(filename, format="wav")
        chunks.append(filename)
    return chunks
