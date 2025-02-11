Speak-Write: Speech-to-Text & Text-to-Speech with Flask Backend

Overview
Speak-Write is a Python-based application that converts speech to text and vice versa. It features a Tkinter GUI for user interaction and a Flask backend for handling speech processing and database storage.

Features
Speech-to-Text: Convert spoken words into text.
Text-to-Speech: Read out text using a speech synthesizer.
Database Integration: Store and retrieve recognized text using SQLite.
Flask API: Backend server for processing speech and managing data.

Installation
Prerequisites
Ensure you have Python installed (version 3.7 or later).
1. Clone the Repository
git clone https://github.com/yourusername/Speak-Write.git
cd Speak-Write

2. Create and Activate Virtual Environment (Optional but Recommended)
python -m venv venv  # Create virtual environment
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

Usage
1. Start the Flask Backend
python server.py
This will start the Flask API at http://127.0.0.1:5000/.

2. Run the Tkinter GUI
python pyProject.py
API Endpoints
Method
Endpoint

Description
POST
/speech-to-text
Converts speech to text and stores in DB

POST
/text-to-speech
Reads text aloud

GET
/get-queries
Retrieves stored speech-to-text queries
Contributing

Fork the repository.
Create a new branch: git checkout -b feature-branch
Commit changes: git commit -m 'Add new feature'
Push to the branch: git push origin feature-branch
Open a Pull Request.

License
This project is licensed under the MIT License.

Author
saurabh buye
