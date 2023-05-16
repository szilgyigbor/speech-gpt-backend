import openai
from api_keys import API_KEY
import os

openai.api_key = API_KEY


def transcribe_audio(incoming_audio):
    # Save the file first
    file_path = "temp_audio.m4a"
    incoming_audio.save(file_path)

    # Opening the file in binary
    with open(file_path, 'rb') as audio_file:
        # Calling the OpenAI Speech to Text API
        response = openai.Audio.transcribe("whisper-1", audio_file)

    # Getting the text
    transcription = response['text']

    # Delete the temporary file
    os.remove(file_path)

    return transcription
