import cohere
import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found. Please set COHERE_API_KEY in your .env file.")

co = cohere.Client(COHERE_API_KEY)

def query_cohere(prompt):
    response = co.generate(
        model='command',  # or 'command-r'
        prompt=prompt,
        max_tokens=100,
        temperature=0.7
    )
    return response.generations[0].text.strip()
