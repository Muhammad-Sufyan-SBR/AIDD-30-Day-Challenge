import json
from utils import safe_llm_call

SYSTEM_PROMPT_QUIZ = """You are an expert educator. Generate a quiz based on the provided text.
The output MUST be a valid JSON object with the following structure:
{{
    "questions": [
        {{
            "id": 1,
            "question": "Question text here?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct_answer": "Option A",
            "explanation": "Why option A is correct."
        }}
    ]
}}
Create {num_questions} multiple-choice questions that test understanding of key concepts.
Do not include markdown formatting (like ```json), just the raw JSON string.
"""

def generate_quiz(client, text, model="gemini-2.0-flash", num_questions=5):
    """
    Generates a JSON-formatted quiz from the text.
    """
    # Limit text context for the quiz to avoid overload
    truncated_text = text[:10000]

    # Format the system prompt with the requested number of questions
    formatted_system_prompt = SYSTEM_PROMPT_QUIZ.format(num_questions=num_questions)

    messages = [
        {"role": "system", "content": formatted_system_prompt},
        {"role": "user", "content": f"Generate a quiz with {num_questions} questions based on this text:\n\n{truncated_text}"}
    ]

    response_text = safe_llm_call(client, model, messages)

    # Clean up if the LLM adds markdown blocks
    clean_text = response_text.strip()
    if clean_text.startswith("```json"):
        clean_text = clean_text[7:]
    if clean_text.startswith("```"):
        clean_text = clean_text[3:]
    if clean_text.endswith("```"):
        clean_text = clean_text[:-3]

    try:
        quiz_data = json.loads(clean_text)
        return quiz_data
    except json.JSONDecodeError:
        print("Failed to decode JSON from LLM response.")
        return {"questions": []}

