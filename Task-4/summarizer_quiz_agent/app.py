import streamlit as st
import os
import time
from dotenv import load_dotenv

# Import our modules
from pdf_utils import extract_text_from_pdf
from summarizer import generate_summary
from quiz_generator import generate_quiz
from notes_generator import generate_study_notes
from keywords import extract_keywords
from concept_map import generate_concept_map
from highlights import add_annotation, get_annotations
from memory import AgentMemory
from utils import get_gemini_client

# --- Configuration & Setup ---
st.set_page_config(
    page_title="Professional AI Study Agent",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom UI Styling ---
st.markdown("""
<style>
    /* Main Title Styling */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        font-family: 'Segoe UI', sans-serif;
        background: linear-gradient(to right, #12c2e9, #c471ed, #f64f59);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 3rem;
    }
    
    /* Footer Styling */
    .footer {
        width: 100%;
        background-color: transparent;
        color: #555; /* Fallback for non-gradient text */
        text-align: center;
        padding: 20px;
        font-size: 14px;
        border-top: none;
        margin-top: 50px;
    }
    .gradient-footer-text {
        background: linear-gradient(45deg, #FF512F, #DD2476, #1A2980); /* Example gradient colors */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 600;
    }
    /* Remove padding bottom from container since footer is no longer fixed */
    .block-container {
        padding-bottom: 1rem;
    }
    
    /* Modern Tab Navigation */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        justify-content: center;
        padding-bottom: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: auto;
        padding: 12px 30px;
        background-color: #ffffff;
        border-radius: 30px;
        border: 1px solid #e0e0e0;
        color: #555;
        font-weight: 600;
        font-size: 15px;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    /* Hover Effect */
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #f8f9fa;
        border-color: #b0b8c1;
        transform: translateY(-2px);
        color: #333;
    }

    /* Active Tab Styling */
    .stTabs [aria-selected="true"] {
        background-color: #2c3e50;
        color: #ffffff;
        border-color: #2c3e50;
        box-shadow: 0 4px 10px rgba(44, 62, 80, 0.3);
    }
    
    /* Hide default decoration line */
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: transparent !important;
    }

    /* Button Styling */
    .stButton button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        padding: 0.5rem 1rem;
    }
    
    /* Success/Info Box Styling */
    .stAlert {
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Initialize Memory
if "memory" not in st.session_state:
    st.session_state.memory = AgentMemory()

# --- Sidebar ---
with st.sidebar:
    st.title("🎓 Study Agent")
    st.markdown("---" )
    
    # Load API Key Internally
    client = get_gemini_client()
    if not client:
        st.error("Configuration Error: API Key not found.")
        st.info("Please ensure GEMINI_API_KEY is set in the .env file.")
        st.stop()
    
    st.success("✅ System Connected")
    st.markdown("---" )

    # File Upload
    uploaded_file = st.file_uploader("Upload Study Material (PDF)", type=["pdf"])
    
    if st.button("Clear Session Memory"):
        st.session_state.memory.clear()
        st.rerun()

# --- Main Logic ---

if uploaded_file:
    # Check if we already processed this file
    last_file = st.session_state.memory.get("last_filename")
    
    if last_file != uploaded_file.name:
        with st.spinner("Processing PDF... (This may take a moment)"):
            # 1. Extract Text
            text = extract_text_from_pdf(uploaded_file)
            
            if text:
                # 2. Auto-Generate All Content
                # Summary
                summary = generate_summary(client, text)
                
                # Keywords
                kws = extract_keywords(text)
                
                # Concept Map
                cmap = generate_concept_map(client, text)
                
                # Quiz
                q_data = generate_quiz(client, text)
                
                # Study Notes
                notes = generate_study_notes(client, text)
                
                # Update Memory
                st.session_state.memory.update({
                    "last_filename": uploaded_file.name,
                    "full_text": text,
                    "summary": summary,
                    "quiz_data": q_data,
                    "keywords": kws,
                    "concept_map": cmap,
                    "ai_notes": notes
                })
                st.rerun()
            else:
                st.error("Failed to extract text from the PDF.")
                st.stop()

    # Load data from memory
    full_text = st.session_state.memory.get("full_text", "")

    # Tabs for features
    tab1, tab2, tab3, tab4 = st.tabs(["📄 Summary & Highlights", "🧠 Concept Map", "📝 Quiz", "📓 Notes"])

    # --- Tab 1: Summary ---
    with tab1:
        st.header("Executive Summary")
        
        summary = st.session_state.memory.get("summary")
        if summary:
            st.markdown(summary)
            
            st.markdown("### 🔑 Key Concepts")
            keywords = st.session_state.memory.get("keywords", [])
            if keywords:
                st.write(" ".join([f"`{k}`" for k in keywords]))
        else:
            st.info("Processing summary...")

    # --- Tab 2: Concept Map ---
    with tab2:
        st.header("Knowledge Graph")
        cmap_code = st.session_state.memory.get("concept_map")
        if cmap_code:
            st.markdown(f"```mermaid\n{cmap_code}\n```")
        else:
             st.info("Processing concept map...")

    # --- Tab 3: Quiz ---
    with tab3:
        st.header("Self-Assessment")
        quiz_data = st.session_state.memory.get("quiz_data")
        
        if quiz_data and "questions" in quiz_data:
            for i, q in enumerate(quiz_data["questions"]):
                st.subheader(f"Q{i+1}: {q['question']}")
                
                # Use a unique key for each radio to maintain state
                user_choice = st.radio(
                    "Choose an answer:", 
                    q['options'], 
                    key=f"q_{i}",
                    index=None
                )
                
                if user_choice:
                    if user_choice == q['correct_answer']:
                        st.success(f"Correct! {q.get('explanation', '')}")
                    else:
                        st.error(f"Incorrect. The correct answer was: {q['correct_answer']}")
            
            st.markdown("---")
            if st.button("🔄 Generate More Questions"):
                with st.spinner("Generating more questions..."):
                    # Generate 5 new questions
                    new_quiz_data = generate_quiz(client, full_text, num_questions=5)
                    
                    if new_quiz_data and "questions" in new_quiz_data:
                        # Append new questions to existing list with updated IDs
                        current_count = len(quiz_data["questions"])
                        for q in new_quiz_data["questions"]:
                            q["id"] = current_count + 1
                            quiz_data["questions"].append(q)
                            current_count += 1
                        
                        # Update session state
                        st.session_state.memory.update({"quiz_data": quiz_data})
                        st.rerun()
                    else:
                        st.error("Failed to generate more questions. Please try again.")

        elif quiz_data:
            st.warning("Could not generate a valid quiz.")
        else:
            st.info("Processing quiz...")

    # --- Tab 4: Notes ---
    with tab4:
        st.header("AI Study Notes")
        ai_notes = st.session_state.memory.get("ai_notes")
        if ai_notes:
            st.markdown(ai_notes)
        else:
            st.info("Processing notes...")
            
        st.markdown("---")
        st.header("My Personal Notes")
        
        new_note = st.text_area("Add a personal note:")
        if st.button("Save Note"):
            if new_note:
                updated_mem = add_annotation(st.session_state.memory.data, "General", new_note)
                st.session_state.memory.update(updated_mem)
                st.success("Note saved!")
                time.sleep(1)
                st.rerun()
        
        annotations = get_annotations(st.session_state.memory.data)
        if annotations:
            for note in annotations:
                with st.expander(f"Note - {note['timestamp']}"):
                    st.write(note['note'])

else:
    st.markdown('<div class="main-title">📚 Professional Study Agent 🤖</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your Personal AI-Powered Research Assistant</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("👆 Please upload a PDF document from the sidebar to begin your study session.")
        
        st.markdown("### 🚀 Capabilities")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            **📄 Smart Summaries**
            Get instant executive summaries of long documents.
            
            **🧠 Concept Maps**
            Visualize complex relationships between topics.
            """)
        with c2:
            st.markdown("""
            **📝 Auto-Generated Quizzes**
            Test your knowledge with dynamic questions.
            
            **📓 Structured Notes**
            Receive exam-ready study notes automatically.
            """)

# --- Footer ---
st.markdown("""
<div class="footer">
    <span class="gradient-footer-text">Created with ❤️ by <b>Muhammad Sufiyan</b></span>
</div>
""", unsafe_allow_html=True)