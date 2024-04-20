import os 
import openai
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()


def transcriber(file_path):
    openai.api_key = os.getenv("OPEN_AI_API")
    text = []
    list_paths = split_mp3(file_path)
    
    for path in list_paths:
        with open(path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            text.append(transcript.text)
    combined_text = ' '.join(text)
    return combined_text


def is_mp3(file_path):
    return file_path.lower().endswith('.mp3')

def split_mp3(file_path):
    output_files = []
    
    
    if not is_mp3(file_path):
        print("Not an MP3 file!")
        return output_files

   
    file_size = os.path.getsize(file_path) / (1024 * 1024) 

   
    if file_size > 25:
        audio = AudioSegment.from_mp3(file_path)

        
        chunk_length = int((25 * 60 * 1000) * (len(audio) / (file_size * 1000)))

        chunks = [audio[i:i + chunk_length] for i in range(0, len(audio), chunk_length)]

        base_name = os.path.basename(file_path).replace('.mp3', '')
        directory = os.path.dirname(file_path)
        for index, chunk in enumerate(chunks):
            chunk_path = os.path.join(directory, f"{base_name}_part{index + 1}.mp3")
            chunk.export(chunk_path, format="mp3")
            output_files.append(chunk_path)

    else:
       output_files.append(file_path)
       return output_files

    return output_files
