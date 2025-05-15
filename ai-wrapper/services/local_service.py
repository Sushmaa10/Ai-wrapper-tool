import os
import sys
from transformers import pipeline

def check_dependencies():
    try:
        import numpy
        import torch
        import regex
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        return False

def get_local_response(prompt):
    if not check_dependencies():
        return {
            "error": "Missing dependencies",
            "solution": "Run: pip install transformers[torch] numpy regex"
        }
    
    try:
        model = pipeline(
            "text-generation",
            model="distilgpt2",
            device=-1,  # CPU
            torch_dtype="auto",
            tokenizer="distilgpt2"
        )
        
        response = model(
            prompt,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            pad_token_id=50256
        )[0]['generated_text']
        
        return {
            "response": response.strip(),
            "model": "distilgpt2"
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "solution": "Check model files in ~/.cache/huggingface"
        }

if __name__ == "__main__":
    print(get_local_response("Explain AI:"))