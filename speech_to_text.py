import openai
from api_keys import API_KEY

openai.api_key = API_KEY

def transcribe_audio(audio_file):
    # Opening the file in binary
    with open(audio_file, 'rb') as f:
        audio_data = f.read()

    # Calling the OpenAI Speech to Text API
    response = openai.Transcription.create(audio=audio_data)

    # Getting the text
    transcription = response['transcription']

    return transcription