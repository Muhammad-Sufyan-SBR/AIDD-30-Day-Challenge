from utils import safe_llm_call

SYSTEM_PROMPT_CONCEPT_MAP = """You are a knowledge visualization expert.
Generate a Mermaid.js 'graph TD' (Top-Down) diagram source code that represents the key concepts and their relationships in the provided text.

Rules:
1. Start with 'graph TD'.
2. Use short, concise labels for nodes (max 3 words).
3. Create meaningful relationships between nodes using arrow syntax (A -->|relationship| B).
4. Limit to the top 10-15 most important concepts to keep the graph readable.
5. Do NOT include markdown blocks (```mermaid). Just return the code.
"""

def generate_concept_map(client, text, model="gemini-2.0-flash"):
    """
    Generates Mermaid.js graph syntax for a concept map.
    """
    truncated_text = text[:10000]

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT_CONCEPT_MAP},
        {"role": "user", "content": f"Create a concept map for:\n\n{truncated_text}"}
    ]

    response = safe_llm_call(client, model, messages)

    # Clean up
    clean_text = response.strip()
    if clean_text.startswith("```mermaid"):
        clean_text = clean_text[10:]
    elif clean_text.startswith("```"):
        clean_text = clean_text[3:]
    if clean_text.endswith("```"):
        clean_text = clean_text[:-3]
        
    return clean_text.strip()

