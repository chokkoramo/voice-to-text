from pydub import AudioSegment

def load_audio(file_path:str)->AudioSegment:
    """Carga un archivo de audio y lo devuelve como objeto AudioSegment"""
    return AudioSegment.from_file(file_path)