# app.py
from flask import Flask, request, jsonify
import logging

# Configure basic logging for better visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Define a list of "important" keywords. This is our simple "AI" rule set.
IMPORTANT_KEYWORDS = ["urgent", "action", "review", "critical", "deadline", "important"]

@app.route('/')
def health_check():
    """
    Simple health check endpoint to confirm the application is running.
    """
    logging.info("Health check requested.")
    return "Keyword Detector App is running!"

@app.route('/detect-keywords', methods=['POST'])
def detect_keywords():
    """
    API endpoint to detect predefined keywords in input text.
    Expects a JSON payload with a 'text' key: {"text": "Your input sentence."}

    Example Request:
    {
        "text": "Please take urgent action on this critical report before the deadline."
    }

    Example Response:
    {
        "input_text": "Please take urgent action on this critical report before the deadline.",
        "found_keywords": ["urgent", "action", "critical", "deadline"]
    }
    """
   
    
   
    # Ensure the request content type is JSON
    if not request.is_json:
        logging.warning("Received non-JSON request to /detect-keywords.")
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    text = data.get('text')

    if not text:
        logging.warning("No 'text' provided in the request payload.")
        return jsonify({"error": "Please provide 'text' in the request body."}), 400

    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    found_keywords = []

    logging.info(f"Detecting keywords in text: '{text[:100]}...'") # Log first 100 chars

    # Iterate through our defined keywords and check if they are in the input text
    for keyword in IMPORTANT_KEYWORDS:
        if keyword in text_lower:
            found_keywords.append(keyword)

    logging.info(f"Keywords detected: {found_keywords}")

    # Return the original text and the list of found keywords
    return jsonify({
        "input_text": text,
        "found_keywords": found_keywords
    })

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis():
    """
    Placeholder for future sentiment analysis functionality.
    Currently returns a fixed response.
    """
    # logging.info("Sentiment analysis endpoint called, but not implemented yet.")
    # return jsonify({"message": "Sentiment analysis is not implemented yet."}), 501

        # Ensure the request content type is JSON
    if not request.is_json:
        logging.warning("Received non-JSON request to /detect-keywords.")
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    text = data.get('text')

    if not text:
        logging.warning("No 'text' provided in the request payload.")
        return jsonify({"error": "Please provide 'text' in the request body."}), 400

    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    found_keywords = []

    logging.info(f"Detecting keywords in text: '{text[:100]}...'") # Log first 100 chars

    # Iterate through our defined keywords and check if they are in the input text
    for keyword in IMPORTANT_KEYWORDS:
        if keyword in text_lower:
            found_keywords.append(keyword)

    logging.info(f"Keywords detected: {found_keywords}")

    # Return the original text and the list of found keywords
    return jsonify({
        "input_text": text,
        "found_keywords": found_keywords
    })

if __name__ == '__main__':
    # When running locally (outside Docker for testing), use debug mode.
    logging.info("Starting Flask application in development mode...")
    app.run(host='0.0.0.0', port=5000, debug=True)

