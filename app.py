from flask import Flask, render_template, request
import pickle
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

app = Flask(__name__, template_folder='/Users/ravipandey/Projects/Plagiarism Detector/templates')

# Path to your service account file
SERVICE_ACCOUNT_FILE = 'striped-bonfire-445913-p1-636c2f70ee72.json'

# Load your model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Function to detect plagiarism
def detect(input_text):
    vectorized_text = tfidf_vectorizer.transform([input_text])
    result = model.predict(vectorized_text)
    return "Plagiarism Detected" if result[0] == 1 else "No Plagiarism Detected"

# Authenticate using service account credentials
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/drive'])

# Create a service client
drive_service = build('drive', 'v3', credentials=credentials)

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle plagiarism detection
@app.route('/detect', methods=['POST'])
def detect_plagiarism():
    input_text = request.form['text']
    detection_result = detect(input_text)
    return render_template('index.html', result=detection_result)

if __name__ == "__main__":
    app.run(debug=True)
