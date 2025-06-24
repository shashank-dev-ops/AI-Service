from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Please provide 'text' in the request body"}), 400
    text = data['text']
    result = sentiment_pipeline(text)
    return jsonify(result)

@app.route('/')
def health_check():
    return "AI App is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)