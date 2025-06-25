# app.py
from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL.
    It returns a simple greeting message.
    """
    return 'Hello from Docker!'

# This block ensures the application runs only when the script is executed directly
# It starts the Flask development server on all available network interfaces (0.0.0.0)
# and on port 5000.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

