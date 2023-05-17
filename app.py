from flask import Flask, request, jsonify
from flask_cors import CORS
from speech_to_text import transcribe_audio
from get_bot_answer import get_answer

app = Flask(__name__)
# CORS(app)   # Enables CORS for all routes
CORS(app, resources={"/api2/*": {"origins": "http://localhost:4200"}})  # Enables CORS only for this route


@app.route('/')
def hello():
    return "hello"


@app.route('/api2/transcribe', methods=['POST'])
def transcribe_endpoint():
    # Check if a file was received in the request
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file found'})

    file = request.files['audioFile']

    transcription = transcribe_audio(file)

    return jsonify(transcription)


@app.route('/api2/get-answer', methods=['POST'])
def answer_endpoint():
    message_history = request.get_json()
    messages = get_answer(message_history)

    return jsonify(messages)


if __name__ == '__main__':
    app.run(debug=True)
