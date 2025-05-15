from .caching import get_cached_response  # Import from your caching system

def batch_process(prompts):
    """
    Process multiple prompts efficiently with deduplication
    Args:
        prompts: List of input strings
    Returns:
        List of responses in original order
    """
    # Deduplicate while preserving later order (more cache-friendly)
    unique_prompts = list(dict.fromkeys(prompts))
    
    # Batch get cached or fresh responses
    responses = {p: get_cached_response(p) for p in unique_prompts}
    
    # Return in original order with duplicates
    return [responses[p] for p in prompts]