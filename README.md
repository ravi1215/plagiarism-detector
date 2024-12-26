# Plagiarism Detector
This project is a web-based application that detects plagiarism in text using a machine learning model. The application is built with Flask for the backend and integrates a trained machine learning model to classify whether a given text is plagiarized.

## Features
1. Simple web interface for submitting text.
2. Uses TF-IDF for text vectorization.
3. Machine learning model to predict plagiarism.
4. Displays detection results on the same page.

## Project Structure
```bash
Copy code
/app.py                  # Main Flask application
/templates/index.html    # HTML template for the web interface
/model.pkl               # Trained machine learning model
/tfidf_vectorizer.pkl    # Trained TF-IDF vectorizer
```

## Prerequisites
Python 3.8 or later
Flask
Scikit-learn
Pickle (to save and load the model and vectorizer)

## Installation
1. Clone the repository:

```bash
Copy code
git clone https://github.com/your-repo/plagiarism-detector.git
cd plagiarism-detector
```

2.Install dependencies:

```bash
Copy code
pip install -r requirements.txt
```

3. Ensure the following files are in place:
model.pkl: The trained plagiarism detection model.
tfidf_vectorizer.pkl: The TF-IDF vectorizer used to transform input text.

4. Run the application:

```bash
Copy code
python app.py
```
5. Access the web interface: Open a web browser and navigate to http://127.0.0.1:5000.

## Usage
Enter text in the input box.
x on the web interface.
Submit the text to check for plagiarism.
View the result indicating whether plagiarism is detected.
<img width="1470" alt="Screenshot 2024-12-26 at 23 23 28" src="https://github.com/user-attachments/assets/3cab08ef-e05a-434d-bf21-60c61e79ab4e" />




