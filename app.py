from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
from gradio_client import Client

app = Flask(__name__)

# Hugging Face Gradio API URL
API_URL = "https://enlightenment-compai.hf.space/run/predict"

client = Client('enlightenment/CompAI')

# Load CSV only to get feature columns
data = pd.read_csv('PHQ9_Student_Depression_Ready_for_Training.csv')
feature_columns = data.columns[1:-2]

# PHQ-9 questions (for form display, optional)
phq9_questions = [
    "Do you have little interest or pleasure in doing things?",
    "Do you feel down, depressed, or hopeless?",
    "Do you have trouble falling or staying asleep, or do you sleep too much?",
    "Do you feel tired or have little energy?",
    "Do you have poor appetite or tend to overeat?",
    "Do you feel bad about yourself or that you are a failure or have let yourself or your family down?",
    "Do you have trouble concentrating on things, such as reading, work, or watching television?",
    "Have you been moving or speaking so slowly that other people have noticed, or the opposite—being fidgety or restless?",
    "Have you had thoughts of self-harm or felt that you would be better off dead?"
]

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/journal', methods=['GET', 'POST'])
def journal():
    return render_template('journal.html')

@app.route('/community', methods=['GET', 'POST'])
def community():
    return render_template('community.html')

@app.route('/predict', methods=['GET','POST'])
def predict_():
    if request.method == 'POST':
        # Collect responses from form
        responses = [request.form.get(f"q{i}", "") for i in range(1, 10)]

        try:
            # Call Hugging Face Space via Gradio Client
            severity_score = client.predict(
                param_0=responses[0],
                param_1=responses[1],
                param_2=responses[2],
                param_3=responses[3],
                param_4=responses[4],
                param_5=responses[5],
                param_6=responses[6],
                param_7=responses[7],
                param_8=responses[8],
                api_name="/predict"
            )

            severity_score = float(severity_score)
            return jsonify({'severity_score': severity_score})
        
        except Exception as e:
            print("Gradio API Error:", e)
            return jsonify({'error': 'Failed to get prediction from API'}), 500


    return render_template('form.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
