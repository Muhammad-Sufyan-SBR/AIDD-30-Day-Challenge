import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_gemini_client(api_key=None):
    """
    Returns a configured Google Gemini client instance.
    Prioritizes passed api_key, then environment variable.
    """
    key = api_key or os.getenv("GEMINI_API_KEY") # Changed to GEMINI_API_KEY
    if not key:
        return None
    
    genai.configure(api_key=key)
    return genai

def safe_llm_call(client, model, messages, temperature=0.7, max_tokens=1000):
    """
    Wrapper for Google Gemini API calls with basic error handling.
    """
    try:
        # Convert messages from OpenAI format to Gemini format
        # OpenAI: [{"role": "system", "content": "..."}]
        # Gemini: Start with user role if system instruction is provided, 
        #         otherwise just user/model turns.
        gemini_messages = []
        system_instruction = ""

        if messages and messages[0]["role"] == "system":
            system_instruction = messages[0]["content"]
            # All subsequent messages should alternate user/model
            for msg in messages[1:]:
                if msg["role"] == "user":
                    gemini_messages.append({"role": "user", "parts": [msg["content"]]})
                elif msg["role"] == "assistant": # OpenAI's assistant role maps to Gemini's model role
                    gemini_messages.append({"role": "model", "parts": [msg["content"]]})
        else:
            # If no system instruction, just map roles directly
            for msg in messages:
                if msg["role"] == "user":
                    gemini_messages.append({"role": "user", "parts": [msg["content"]]})
                elif msg["role"] == "assistant":
                    gemini_messages.append({"role": "model", "parts": [msg["content"]]})
        
        # Initialize the generative model
        model_instance = client.GenerativeModel(
            model_name=model,
            system_instruction=system_instruction if system_instruction else None
        )

        response = model_instance.generate_content(
            gemini_messages,
            generation_config=genai.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        return response.text
    except Exception as e:
        return f"Error communicating with AI: {str(e)}"