# AI Wrapper Tool

A Flask-based web application that provides a clean interface to interact with various AI models, currently supporting Cohere's language models.

## Features

- RESTful API endpoint for AI interactions
- Web interface for easy interaction
- Support for Cohere's language models
- Usage tracking and monitoring
- CORS enabled for cross-origin requests

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and add your Cohere API key:
   ```bash
   cp .env.example .env
   ```
5. Edit `.env` and add your Cohere API key

## Running the Application

Start the server:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## API Usage

Send a POST request to `/api/chat` with a JSON body:
```json
{
    "prompt": "Your question or prompt here"
}
```

## Development

- The project uses Flask for the web framework
- Cohere's API for AI model interactions
- Python-dotenv for environment variable management
- Flask-CORS for handling cross-origin requests

## Security Notes

- Never commit the `.env` file containing your API keys
- Always use environment variables for sensitive data
- The `.env.example` file shows what environment variables are needed
