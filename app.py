from flask import Flask, request, jsonify
from flask_cors import CORS
from speech_to_text import transcribe_audio

app = Flask(__name__)
# CORS(app)   # Enables CORS for all routes
CORS(app, resources={"/transcribe": {"origins": "http://localhost:4200"}})  # Enables CORS only for this route


@app.route('/')
def hello():
    return "hello"


@app.route('/transcribe', methods=['POST'])
def transcribe_endpoint():
    # Check if a file was received in the request
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file found'})

    file = request.files['audioFile']

    transcription = transcribe_audio(file)

    return jsonify(transcription)


if __name__ == '__main__':
    app.run(debug=True)
