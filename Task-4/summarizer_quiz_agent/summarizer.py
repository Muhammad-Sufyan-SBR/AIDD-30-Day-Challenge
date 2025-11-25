from utils import safe_llm_call

SYSTEM_PROMPT_SUMMARIZER = """You are an expert academic research assistant. 
Your goal is to provide a comprehensive, accurate, and structured summary of the provided text.
Focus on:
1. Main arguments and thesis.
2. Key evidence and methodology.
3. Important conclusions.
Use bullet points and clear headings."""

def generate_summary(client, text, model="gemini-2.0-flash"):
    """
    Generates a summary of the provided text.
    """
    if not text:
        return "No text to summarize."

    # For very large texts, we might need a map-reduce strategy, 
    # but for this implementation, we assume the chunk passed is manageable 
    # or the user accepts a truncation/first-pass approach.
    # A robust production version would iterate over chunks.
    
    # If text is huge, we take the first 15k chars as a proxy for now 
    # to prevent token limit errors in a simple prototype.
    truncated_text = text[:15000] 
    if len(text) > 15000:
        truncated_text += "\n\n[Text truncated for summary generation...]"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_SUMMARIZER},
        {"role": "user", "content": f"Summarize the following text:\n\n{truncated_text}"}
    ]

    return safe_llm_call(client, model, messages)
