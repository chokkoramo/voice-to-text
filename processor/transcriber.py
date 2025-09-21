import os
import whisper
from tqdm import tqdm
from processor.utils import format_timestamp

def transcribe_chunks(chunks, model_name="medium", language="es", export_srt=False):
    """Transcribe una lista de fracmentos de audio con Whisper"""
    model = whisper.load_model(model_name)
    
    full_text=""
    srt_output=""
    counter=1
    
    for i, chunk in enumerate(tqdm(chunks, desc="Procesando fragmentos")):
        temp_file= f"temp_chunk_{i}.wav"
        chunk.export(temp_file, format="wav")
        
        result= model.transcribe(temp_file, language=language, task="transcribe")
        full_text += result["text"].strip()+" "
        
        if export_srt:
            for seg in result["segments"]:
                start= format_timestamp(seg["start"])
                end= format_timestamp(seg["end"])
                srt_output += f"{counter}\n{start} --> {end}\n{seg['text'].strip()}\n\n"
                counter += 1
                
        os.remove(temp_file)
        
    return full_text.strip(), srt_output