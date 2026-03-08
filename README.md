# 🧠 AI Math Mentor

An **AI‑powered multimodal math assistant** that can solve mathematical problems from **text, images, and audio**, while generating **step‑by‑step explanations** and **symbolic solutions**.

The system combines **multimodal AI, retrieval‑augmented reasoning, symbolic mathematics, and human‑in‑the‑loop verification** to demonstrate a modern AI system architecture.

---

# 🚀 Live Demo

(Replace with your deployed Streamlit link)

```
https://your-app-name.streamlit.app
```

---

# ✨ Key Features

### 📝 Text Math Solver
Users can directly type mathematical questions.

Example inputs:

```
derivative of x**2 + 3*x
integrate sin(x)
solve x**2 - 4 = 0
```

The system parses the problem and generates a **symbolic solution with explanation**.

---

### 🖼 Image Math Solver
Users can upload an image containing a math problem.

Pipeline:

```
Image → OCR → Problem Parsing → Solver → Explanation
```

The OCR engine extracts the text and sends it to the reasoning pipeline.

---

### 🎤 Audio Math Solver
Users can upload an audio file containing a spoken math question.

Pipeline:

```
Audio → Whisper Speech‑to‑Text → Problem Parsing → Solver
```

The speech is transcribed and then solved by the math reasoning pipeline.

---

### 🧠 Step‑by‑Step Explanations

Each solution includes:

- symbolic solution
- reasoning explanation
- verification result

Example output:

```
Symbolic Solution:
2*x + 3

Explanation:
The derivative of x² is 2x.
The derivative of 3x is 3.
Adding both results gives 2x + 3.
```

---

# 🏗 System Architecture

```
                   ┌──────────────────────┐
                   │      Streamlit UI     │
                   │  (Multimodal Input)  │
                   └──────────┬───────────┘
                              │
                              ▼
                     Input Processing
             ┌────────────┬────────────┬────────────┐
             │            │            │            │
             ▼            ▼            ▼
           Text          Image        Audio
                           │            │
                           ▼            ▼
                       OCR Engine   Speech‑to‑Text
                           │            │
                           └──────┬─────┘
                                  ▼
                           Problem Parser
                                  │
                                  ▼
                           LangGraph Agents
                                  │
                                  ▼
                           Math Solver Agent
                                  │
                                  ▼
                        Symbolic Verification
                               (SymPy)
                                  │
                                  ▼
                          Step‑by‑Step Output
```

---

# ⚙️ Tech Stack

## Frontend
- **Streamlit**

## AI / NLP
- **Transformers**
- **Sentence Transformers**
- **Whisper (Speech Recognition)**

## Math Engine
- **SymPy**

## Agent Framework
- **LangGraph**

## Multimodal Processing
- **PaddleOCR**
- **Whisper**

## Vector Retrieval
- **ChromaDB**

## Utilities
- **NumPy**
- **Pillow**
- **Scikit‑Learn**

---

# 📂 Project Structure

```
math-mentor
│
├── main.py                     # Streamlit UI
│
├── app
│   ├── agents
|   |   ├── parser_agent.py
|   |   ├── solver_agent.py
|   |   ├── verifier_agent.py
│   │   └── math_solver.py     # Main solver pipeline
│   │
│   ├── multimodal
│   │   ├── ocr.py             # Image text extraction
│   │   └── speech_to_text.py  # Audio transcription
│   │
│   ├── graph
│   │   └── graph_builder.py   # LangGraph pipeline
│   │
│   └── utils
│
├── data 
│   └── knowledge_base           # Math knowledge documents
│
├── requirements.txt
├── packages.txt
└── README.md
```

---

# 🧪 Example Usage

### Text Input

```
Input:
derivative of x**2 + 3*x
```

Output:

```
Solution:
2*x + 3
```

---

### Image Input

Upload image containing:

```
x^2 + 3x
```

Pipeline:

```
Image → OCR → Solver → Explanation
```

---

### Audio Input

Upload audio saying:

```
"What is the derivative of x squared plus three x?"
```

Pipeline:

```
Audio → Whisper → Solver → Explanation
```

---

# 🛠 Installation (Local Setup)

Clone the repository:

```bash
git clone https://github.com/Mr-Suj/math-mentor.git
cd math-mentor
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Application

Start the Streamlit app:

```bash
streamlit run main.py
```

The application will run at:

```
http://localhost:8501
```

---

# ☁ Deployment

The project can be deployed easily using **Streamlit Community Cloud**.

Steps:

1. Push the repository to GitHub  
2. Visit

```
https://share.streamlit.io
```

3. Click **New App**

4. Configure:

```
Repository → your repository
Branch → main
Main file → main.py
```

5. Deploy

---

# 🎯 Why This Project Is Interesting

This project demonstrates **real‑world AI system design**, including:

✔ Multimodal AI systems  
✔ Agent‑based reasoning (LangGraph)  
✔ Retrieval‑Augmented Generation (RAG)  
✔ Symbolic mathematics verification  
✔ End‑to‑end AI product deployment  

It combines **LLM reasoning with symbolic math**, an emerging direction in AI research.

---

# 📈 Future Improvements

Possible enhancements:

- LaTeX rendering for math output
- handwritten math OCR
- better reasoning agents
- diagram understanding
- interactive math tutoring
- user feedback learning loop

---

# 👨‍💻 Author

**Sujal Gowda J M**

AI / ML Enthusiast building practical AI systems combining:

- Multimodal AI
- Agentic workflows
- Symbolic reasoning
- Retrieval‑augmented pipelines

---

# ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub!