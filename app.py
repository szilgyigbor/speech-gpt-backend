from flask import Flask, request, jsonify
from flask_cors import CORS
from speech_to_text import transcribe_audio
from get_bot_answer import get_answer

app = Flask(__name__)
# CORS(app)   # Enables CORS for all routes
CORS(app, resources={"/pia/*": {"origins": "*"}})


@app.route('/')
def hello():
    return "hello"


@app.route('/pia/transcribe', methods=['POST'])
def transcribe_endpoint():
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file found'})

    file = request.files['audioFile']

    transcription = transcribe_audio(file)

    return jsonify(transcription)


@app.route('/pia/get-answer', methods=['POST'])
def answer_endpoint():
    message_history = request.get_json()
    messages = get_answer(message_history)

    return jsonify(messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1300)
