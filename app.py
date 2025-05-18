from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from services.orchestrator import get_ai_response
from monitoring.usage_tracker import track_usage  # <-- Logging added

import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# -----------------------------
# Route: Home (for UI rendering)
# -----------------------------
@app.route('/')
def home():
    return render_template("index.html")

# -----------------------------
# Route: API - AI Chat Endpoint
# -----------------------------
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '').strip()

        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400

        # Get AI response via orchestrator
        ai_response = get_ai_response(prompt)

        # Log input/output
        track_usage("anonymous", "cohere", len(prompt.split()))

        return jsonify({'response': ai_response}), 200

    except Exception as e:
        # Log the error (optional: also to a log file)
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# -----------------------------
# Entry Point for App Execution
# -----------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
