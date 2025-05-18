# AI Wrapper Tool

This is a simple AI chatbot web app built with Flask and Cohere API. Users can enter a prompt, and the app sends it to the Cohere API to generate a response.

## Live Demo

👉 [ai-wrapper-tool.onrender.com](https://ai-wrapper-tool.onrender.com)

## Features

- Simple UI to chat with the AI
- Uses Cohere's large language model to generate responses
- Deployed on Rend
- Supports running with Docker using environment variables

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Sushmaa10/Ai-wrapper-tool.git
   cd Ai-wrapper-tool

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt

3. Create a .env file in the root directory with your Cohere API key and port:

   ```ini
   COHERE_API_KEY=your-api-key-here
   PORT=5000

4. Run without Docker:

   ```bash
   python app.py

5. Run with Docker(recommended):

- Build the Docker image:
     
   ```bash
   docker build -t ai-wrapper .

- Run the Docker container with your .env file:   

   ```bash
   docker run --env-file .env -p 5000:5000 ai-wrapper

6. Open your browser and go to:

   ```arduino
   http://localhost:5000

## Technologies Used

- Python (Flask)
- Cohere API
- HTML/CSS/JavaScript
- Docker
- Deployed on Render


![Ai chat](https://github.com/user-attachments/assets/3cf68db8-5c25-48ff-b8ff-ccc3a3fa660b)

