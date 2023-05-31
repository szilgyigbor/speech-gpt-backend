# OpenAI Flask Backend Server

This is a backend server built with Python and Flask to interface with two OpenAI models: Whisper and GPT-3.5.
(OpenAi API key required)

## Features

- **Whisper Model Endpoint:** The Whisper model is a machine learning model developed by OpenAI, capable of converting audio input into text. This server provides a POST endpoint for the Whisper model to process the audio input and produce textual output.

- **GPT-3.5 Model Endpoint:** The GPT-3.5 is the latest addition to the renowned Generative Pretrained Transformer model series, capable of generating responses based on textual input. This server also provides a POST endpoint for the GPT-3.5 model.

## Technologies Used

The project uses the following technologies:

- Python
- Flask
- OpenAI API

## Installation

1. Clone the repository onto your local machine.
- git clone [<repo-link>](https://github.com/szilgyigbor/speech-gpt-backend)
  
2. Install the necessary dependencies.
- pip install -r requirements.txt

3. Run the server.
- python app.py

## Usage
  
You can make POST requests to the following endpoints:
- '/pia/transcribe': Convert audio input into text using the Whisper model.
- '/pia/get-answer': Generate a response based on textual input using the GPT-3.5 model.
  
