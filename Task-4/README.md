# 📚 Professional AI Study Agent

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B.svg)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-8E75B2.svg)

An advanced, AI-powered research assistant designed to transform static PDF documents into interactive learning experiences. Built with **Google Gemini 2.0 Flash**, this agent automatically generates summaries, quizzes, concept maps, and structured study notes to help you master any material faster.

## 🚀 Features

- **📄 Smart Executive Summaries**: Instantly get the gist of long research papers or textbooks.
- **🧠 Interactive Knowledge Graphs**: Visualize complex relationships between topics using AI-generated Mermaid.js diagrams.
- **📝 Infinite Auto-Quizzing**: 
    - Test your knowledge with AI-generated multiple-choice questions.
    - **Dynamic Generation**: Click "Generate More Questions" to create endless practice sets.
    - Immediate feedback with detailed explanations.
- **📓 AI Structured Study Notes**: Automatically extracts:
    - Key Definitions
    - Core Concepts
    - Important Facts/Dates
    - Formulas & Rules
- **✍️ Personal Note-Taking**: Add your own insights alongside the AI-generated content.
- **🎨 Professional UI**: A modern, clean interface with pill-shaped navigation, gradient aesthetics, and a user-friendly experience.
- **💾 Session Memory**: Keeps track of your current study session context.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python)
- **AI Engine**: Google Gemini 2.0 Flash (via `google-generativeai`)
- **PDF Processing**: PyPDF2
- **Visualization**: Mermaid.js (rendered via Streamlit)
- **Environment**: Python Dotenv

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Task-4
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. **Run the Application**
   ```bash
   streamlit run summarizer_quiz_agent/app.py
   ```

## 📂 Project Structure

```
Task-4/
├── .env                     # API Keys (Ignored by Git)
├── requirements.txt         # Python Dependencies
├── summarizer_quiz_agent/   # Main Application Source
│   ├── app.py               # Main Streamlit Entry Point
│   ├── summarizer.py        # AI Summary Logic
│   ├── quiz_generator.py    # AI Quiz Logic
│   ├── notes_generator.py   # AI Study Notes Logic
│   ├── concept_map.py       # AI Graph Logic
│   ├── pdf_utils.py         # PDF Parsing
│   ├── memory.py            # Session State Management
│   └── utils.py             # API & Helper Functions
└── README.md                # Documentation
```

## 👤 Creator

**Muhammad Sufiyan**  
*Created with ❤️ using Python & Generative AI.*