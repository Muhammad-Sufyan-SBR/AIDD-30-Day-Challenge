from utils import safe_llm_call

SYSTEM_PROMPT_NOTES = """You are an expert academic tutor. 
Your goal is to create comprehensive, structured STUDY NOTES from the provided text.
These notes should be perfect for exam revision.

Structure the notes as follows:
1. **Key Definitions**: Define important terms found in the text.
2. **Core Concepts**: Explain the main ideas in bullet points.
3. **Important Facts/Data**: List any specific dates, numbers, names, or crucial facts.
4. **Formulas/Rules** (if applicable): Extract any mathematical formulas or scientific rules.
5. **Summary Points**: Brief takeaways for quick revision.

Format using Markdown (bolding, lists, headers). Keep it concise but informative.
"""

def generate_study_notes(client, text, model="gemini-2.0-flash"):
    """
    Generates structured study notes from the provided text.
    """
    # Limit text to avoid token issues, though for notes we want good coverage.
    # 15k chars is a reasonable balance for this prototype.
    truncated_text = text[:15000]
    if len(text) > 15000:
        truncated_text += "\n\n[Text truncated for notes generation...]"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_NOTES},
        {"role": "user", "content": f"Create study notes for the following text:\n\n{truncated_text}"}
    ]

    return safe_llm_call(client, model, messages)

