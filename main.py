import streamlit as st
from PIL import Image
import tempfile

# Import your modules
from app.agents.math_solver import solve_math_problem
from app.multimodal.ocr import extract_text_from_image
from app.multimodal.speech_to_text import transcribe_audio


st.set_page_config(
    page_title="AI Math Mentor",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Math Mentor")
st.caption("Solve math problems using text, image, or audio input")

st.divider()

# Tabs for input modes
tab1, tab2, tab3 = st.tabs(["✍ Text", "🖼 Image", "🎤 Audio"])


# ==========================
# TEXT SOLVER
# ==========================

with tab1:

    st.subheader("Enter a Math Problem")

    question = st.text_input(
        "Enter text",
        placeholder="Example: Find derivative of x^2 + 3x"
    )

    if st.button("Solve Text Problem", key="text_solve"):

        if question.strip() == "":
            st.warning("Please enter a math question.")
        else:

            with st.spinner("Solving..."):
                result = solve_math_problem(question)

            st.success("Solution Generated")

            st.markdown("### 📌 Symbolic Solution")
            st.code(result["solution"])

            st.markdown("### 🧠 Explanation")
            st.markdown(result["explanation"])


# ==========================
# IMAGE SOLVER
# ==========================

with tab2:

    st.subheader("Upload Image with Math Problem")

    uploaded_image = st.file_uploader(
        "Upload image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image is not None:

        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Solve Image Problem", key="image_solve"):

            with st.spinner("Extracting text from image..."):

                question = extract_text_from_image(uploaded_image)

            st.write("### Extracted Question")
            st.code(question)

            with st.spinner("Solving..."):
                result = solve_math_problem(question)

            st.success("Solution Generated")

            st.markdown("### 📌 Symbolic Solution")
            st.code(result["solution"])

            st.markdown("### 🧠 Explanation")
            st.markdown(result["explanation"])


# ==========================
# AUDIO SOLVER
# ==========================

with tab3:

    st.subheader("Upload Audio with Math Question")

    uploaded_audio = st.file_uploader(
        "Upload audio",
        type=["wav", "mp3", "m4a"]
    )

    if uploaded_audio is not None:

        st.audio(uploaded_audio)

        if st.button("Solve Audio Problem", key="audio_solve"):

            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded_audio.read())
                temp_path = tmp.name

            with st.spinner("Transcribing audio..."):
                question = transcribe_audio(temp_path)

            st.write("### Transcribed Question")
            st.code(question)

            with st.spinner("Solving..."):
                result = solve_math_problem(question)

            st.success("Solution Generated")

            st.markdown("### 📌 Symbolic Solution")
            st.code(result["solution"])

            st.markdown("### 🧠 Explanation")
            st.markdown(result["explanation"])


# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("About AI Math Mentor")

st.sidebar.markdown(
"""
🚀 **AI Math Mentor**

A multimodal AI system that solves math problems using:

• Text input  
• Image OCR  
• Audio speech recognition  

### Features

✔ Retrieval‑Augmented Generation  
✔ Multi‑Agent Reasoning  
✔ Symbolic Math Solver (SymPy)  
✔ Step‑by‑Step Explanations  
✔ Verification Layer  
✔ Human‑in‑the‑Loop Ready

Built for demonstrating modern **AI system design**.
"""
)

st.sidebar.markdown("---")
st.sidebar.caption("Built with ❤️ using AI, RAG, and Multi-Agent Systems")