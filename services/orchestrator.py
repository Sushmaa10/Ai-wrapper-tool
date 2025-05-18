from services.cohere_service import query_cohere
# You can add other models here in the future, e.g.:
# from services.local_service import query_local_model

def get_ai_response(prompt, model='cohere'):
    """
    Routes the prompt to the appropriate AI service based on the selected model.
    
    Args:
        prompt (str): The user input prompt.
        model (str): The model to use for response generation. Default is 'cohere'.
    
    Returns:
        str: The generated response.
    """
    if not prompt.strip():
        raise ValueError("Prompt is empty or missing.")

    try:
        if model == 'cohere':
            generated_text = query_cohere(prompt)
        # elif model == 'local':
        #     generated_text = query_local_model(prompt)
        else:
            raise ValueError(f"Unsupported model: {model}")

        return generated_text

    except Exception as e:
        raise RuntimeError(f"Error generating AI response: {str(e)}")
