from flask import Flask, request, jsonify
import joblib  # for loading ML models
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)
# CORS(app)
CORS(app, resources={r"/predict": {"origins": "http://localhost:5173"}})

# Load your trained model and the TfidfVectorizer
model = joblib.load('model.pkl')  # replace with your actual model file
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # assume the input is JSON format
    text = data.get('text', '')

    # Transform the input text
    text_features = vectorizer.transform([text])

    # Predict using the model
    prediction = model.predict(text_features)

    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
