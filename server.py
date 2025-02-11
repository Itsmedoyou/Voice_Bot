from flask import Flask, request, jsonify
import speech_recognition as sr
import pyttsx3
import sqlite3

app = Flask(__name__)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS queries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        text TEXT)''')
    conn.commit()
    conn.close()

@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            
            conn = sqlite3.connect('data.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO queries (text) VALUES (?)", (text,))
            conn.commit()
            conn.close()
            
            return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    data = request.json
    text = data.get("text", "")
    
    engine.say(text)
    engine.runAndWait()
    
    return jsonify({"message": "Text converted to speech"})

@app.route("/get-queries", methods=["GET"])
def get_queries():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM queries")
    rows = cursor.fetchall()
    conn.close()
    return jsonify({"queries": rows})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
