import PyPDF2
import io

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a Streamlit UploadedFile (PDF).
    Returns the full text as a string.
    """
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    
    return text

def chunk_text(text, chunk_size=4000):
    """
    Splits text into chunks to fit within LLM token limits.
    Simple character-based chunking (can be improved with token counters).
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks
