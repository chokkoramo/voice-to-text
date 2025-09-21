import os
import shutil
from config import TEMP_CHUNKS_PATH

def format_timestamp(seconds:float)->str:
    """Convierte segundos en formato (HH:MM:SS,mm)"""
    hours = int(seconds//3600)
    minutes = int((seconds%3600)//60)
    secs = int(seconds%60)
    mills = int((seconds*1000)%1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{mills:03}"

def clear_temp_chunks():
    if os.path.exists(TEMP_CHUNKS_PATH):
        shutil.rmtree(TEMP_CHUNKS_PATH)
        os.makedirs(TEMP_CHUNKS_PATH, exist_ok=True)
