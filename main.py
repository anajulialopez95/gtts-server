from flask import Flask, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/gtts', methods=['POST'])
def generate_audio():
    data = request.get_json()
    text = data.get('text', '')
    lang = data.get('lang', 'es')  # Español por defecto

    if not text:
        return "Missing text", 400

    tts = gTTS(text=text, lang=lang)
    filename = "output.mp3"
    tts.save(filename)

    return send_file(filename, mimetype="audio/mpeg")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
