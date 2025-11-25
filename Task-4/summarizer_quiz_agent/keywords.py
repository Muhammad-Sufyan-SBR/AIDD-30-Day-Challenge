from rake_nltk import Rake
import nltk

# Ensure NLTK resources are available
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

def extract_keywords(text, num=10):
    """
    Extracts top keywords/keyphrases from text using RAKE.
    """
    if not text:
        return []

    try:
        r = Rake()
        r.extract_keywords_from_text(text)
        ranked_phrases = r.get_ranked_phrases()
        # Filter for uniqueness and relevance (simple heuristic)
        unique_phrases = []
        seen = set()
        for phrase in ranked_phrases:
            if phrase.lower() not in seen and len(phrase) > 3:
                unique_phrases.append(phrase)
                seen.add(phrase.lower())
        
        return unique_phrases[:num]
    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return []
