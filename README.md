# 🚀 LearnPilot AI — Personalized Course Recommendation Agent

An AI-powered learning mentor that creates personalized learning roadmaps based on a student's background, skills, and career goals using **Google Gemini 2.5 Flash**.

The agent analyzes user profiles, understands career objectives, and generates an ordered learning path with recommended courses, prerequisites, and explanations.

---

## 🌟 Features

✅ **Personalized Learning Roadmaps**
- Generates customized learning paths based on:
  - Educational background
  - Current skills
  - Career goals
  - Learning preferences

✅ **AI-Powered Recommendations**
- Uses Google Gemini 2.5 Flash LLM to generate intelligent course suggestions.
- Provides reasoning behind every recommendation.

✅ **Difficulty-Based Course Ordering**
- Automatically organizes courses from:
  - Beginner → Intermediate → Advanced

✅ **Career-Oriented Guidance**
- Helps students prepare for roles such as:
  - Generative AI Engineer
  - Data Scientist
  - Software Engineer
  - Cloud Engineer

✅ **Roadmap Export**
- Download generated learning roadmap as a text file.

---

# 🏗️ System Architecture

```
Student Profile Input
        |
        ↓
Course Knowledge Base
        |
        ↓
Prompt Engineering Layer
        |
        ↓
Google Gemini 2.5 Flash
        |
        ↓
Personalized Learning Roadmap
        |
        ↓
Download Roadmap
```

---

# 🛠 Tech Stack

### Programming Language
- Python

### AI / LLM
- Google Gemini 2.5 Flash
- Google Generative AI SDK

### Framework
- Streamlit

### Environment Management
- python-dotenv

---

# 📂 Project Structure

```
learnpilot-ai/
│
├── app.py                 # Streamlit application
├── courses.json           # Course knowledge base
├── requirements.txt       # Dependencies
├── .env                   # API credentials
├── README.md
└── roadmap.txt            # Generated roadmap output
```

---

# ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/vishnupriya54/learnpilot-ai.git

cd learnpilot-ai
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Configure Gemini API Key

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

### 4. Run Application

```bash
streamlit run app.py
```

---

# 🎯 Example Workflow

### User Input

```
Background:
Computer Science Student

Current Skills:
Python, Java, Basic ML

Goal:
Become a Generative AI Engineer
```

### AI Output

```
1. Python for AI Development
   Reason:
   Strengthen programming foundation.

2. Machine Learning Fundamentals
   Reason:
   Required before deep learning.

3. Deep Learning with Neural Networks
   Reason:
   Build foundation for LLMs.

4. Transformers & Large Language Models
   Reason:
   Understand modern GenAI systems.

5. RAG and AI Agents
   Reason:
   Build production-level GenAI applications.
```

---

# 🚀 Future Enhancements

## ⭐ RAG-Based Recommendation System

Current:

```
courses.json
      |
      |
Gemini AI
      |
      |
Learning Roadmap
```

Future:

```
Course Database
      |
      |
Embedding Model
      |
      |
Vector Database
(FAISS / ChromaDB)
      |
      |
Similarity Search
      |
      |
Gemini LLM
      |
      |
Personalized Roadmap
```

Benefits:
- More accurate recommendations
- Domain-specific knowledge retrieval
- Reduced hallucination
- Scalable course database

---

## 🔮 Planned Features

- [ ] RAG-based course retrieval
- [ ] User authentication
- [ ] Learning progress tracking
- [ ] Skill gap analysis
- [ ] Resume-based recommendations
- [ ] AI career coach chatbot
- [ ] YouTube/course resource integration

---

# 📸 Demo

Coming soon...

---

# 👩‍💻 Author

**Vishnupriya**

GitHub:
https://github.com/vishnupriya54

---

⭐ If you find this project useful, consider giving it a star!
