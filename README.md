# 🧠 CompAI – Mental Health Assessment App

CompAI is a **Flask-based web application** powered by a **Hugging Face model** that helps assess mental health conditions through PHQ-9 questionnaire responses.  
It integrates with a deployed model hosted on **Hugging Face Spaces** using the `gradio_client`.

---

## ⚙️ Tech Stack
- **Backend**: Python (Flask)  
- **Model Serving**: Hugging Face Spaces (`gradio_client`)  
- **Production Server**: Gunicorn   

---

## ▶️ Running the App Locally

### Using Flask (Development Mode)
```bash
python app.py
```

App will be available at:  
👉 `http://127.0.0.1:5000`

### Using Gunicorn (Production Mode)
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
- `-w 4`: Number of workers (adjust based on your server).  
- `-b 0.0.0.0:5000`: Binds to all interfaces on port `5000`.  
- `app:app`: Refers to `app.py` and Flask’s `app` object.  

---

## 🤖 Model & API Integration

The app connects to a Hugging Face Space where we have deployed our **Neural Network model**:

```
https://enlightenment-compai.hf.space
```

We built an **API layer** on top of the neural network model to optimize both **response time** ⏱️ and **result accuracy** ✅.  

The Flask app uses the `gradio_client` to send PHQ-9 questionnaire inputs to this API and fetch a **severity score** instantly.

### Example API Call (Python)

```python
from gradio_client import Client

client = Client("enlightenment/CompAI")

severity_score = client.predict(
    param_0="I feel sad",
    param_1="I feel hopeless",
    param_2="I sleep poorly",
    param_3="I am tired",
    param_4="I have no appetite",
    param_5="I feel like a failure",
    param_6="I can't concentrate",
    param_7="I feel restless",
    param_8="I have thoughts of self-harm",
    api_name="/predict"
)

print("Severity Score:", severity_score)
```


The app connects to the Hugging Face Space:
Here we have deployed our Neural Network

```
https://enlightenment-compai.hf.space
```

It uses the `gradio_client` to send PHQ-9 questionnaire inputs and get a **severity score**.


## 📜 License
This project is licensed under the MIT License.  

---

## 🙌 Contribution
Pull requests and issues are welcome! Please open a discussion before major changes.
