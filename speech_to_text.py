import openai
from api_keys import API_KEY
import os

openai.api_key = API_KEY


def transcribe_audio(incoming_audio):
    # Opening the file in binary
    with open(incoming_audio, 'rb') as audio_file:
        # Calling the OpenAI Speech to Text API
        response = openai.Audio.transcribe("whisper-1", audio_file)

    # Getting the text
    transcription = response['text']

    return transcription