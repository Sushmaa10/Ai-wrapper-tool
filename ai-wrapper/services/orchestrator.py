from services.cohere_service import query_cohere

def get_ai_response(prompt):
    if not prompt:
        return {"response": "No prompt provided!"}

    generated_text = query_cohere(prompt)

    response = {
        "response": generated_text
    }

    print(f"Generated response: {response}")
    return response
