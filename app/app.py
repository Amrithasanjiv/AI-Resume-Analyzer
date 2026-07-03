import tempfile
import sys
from pathlib import Path

import streamlit as st

# Project Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))
from skill_extractor import extract_skills
from predictor import ResumePredictor
from pdf_reader import extract_text_from_pdf

# -----------------------------------
# Page Settings
# -----------------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")
st.markdown("### Upload your resume and let AI analyze it.")

st.divider()

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    predictor = ResumePredictor()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:

        temp.write(uploaded_file.read())

        pdf_path = temp.name

    resume_text = extract_text_from_pdf(pdf_path)

    category = predictor.predict(resume_text)
    skills = extract_skills(resume_text)
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📄 Resume Preview")

        st.text_area(
            "",
            resume_text[:2500],
            height=500
        )

    with col2:

        st.subheader("🤖 AI Prediction")
        st.subheader("🛠 Skills Found")

        for skill in skills:

            st.write("✅", skill)
        st.success(category)

        st.metric(
            label="Resume Length",
            value=f"{len(resume_text.split())} words"
        )