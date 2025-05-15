from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from services.orchestrator import get_ai_response
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        logger.debug("Received request to /api/chat")
        data = request.get_json()
        
        if not data:
            logger.error("No JSON data received")
            return jsonify({'error': 'No JSON data received'}), 400
            
        prompt = data.get('prompt', '')
        if not prompt:
            logger.error("No prompt provided")
            return jsonify({'error': 'Prompt is required'}), 400

        logger.debug(f"Processing prompt: {prompt}")
        response = get_ai_response(prompt)
        logger.debug(f"Generated response: {response}")
        
        return jsonify(response)
    except Exception as e:
        logger.error(f"Error in /api/chat: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure we're in the correct directory
    app_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(app_dir)
    
    # Make sure the templates directory exists
    if not os.path.exists('templates'):
        os.makedirs('templates')
        
    logger.info(f"Starting Flask application in directory: {app_dir}")
    app.run(debug=True, host='127.0.0.1', port=5000)
