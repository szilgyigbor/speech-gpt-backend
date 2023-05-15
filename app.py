from flask import Flask, request, jsonify
from speech_to_text import transcribe_audio

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


@app.route('/transcribe', methods=['POST'])
def transcribe_endpoint():
    # Check if a file was received in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file found'})

    file = request.files['file']

    transcription = transcribe_audio(file)

    return jsonify(transcription)


if __name__ == '__main__':
    app.run(debug=True)
