import streamlit as st

def upload():
    # Render white input card container
    st.markdown('<div class="input-card"><h3 class="card-title">Resume analysis</h3>', unsafe_allow_html=True)
    
    # Streamlit tabs for Text Paste vs PDF upload
    tab_pasted, tab_uploaded = st.tabs(["📝 Paste Text", "📤 Upload PDF"])
    
    resume_content = None
    
    with tab_pasted:
        pasted_text = st.text_area(
            "Paste resume text",
            placeholder="Paste your resume text here — name, work history, skills, and education...",
            height=180,
            label_visibility="collapsed",
            key="pasted_resume_text"
        )
        if pasted_text:
            resume_content = pasted_text
            
    with tab_uploaded:
        uploaded_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
            label_visibility="collapsed",
            key="uploaded_resume_file"
        )
        if uploaded_file:
            resume_content = uploaded_file

    st.write("")
    
    # Option to match against Job Description
    match_jd = st.checkbox("🔍 Match against a target job description")
    job_description = None
    if match_jd:
        job_description = st.text_area(
            "Target Job Description",
            placeholder="Paste the job description here (e.g. required skills, role duties)...",
            height=120,
            key="target_job_description"
        )
        
    st.write("")
    
    # Large primary action button
    analyze_clicked = st.button("🔍 Analyze my resume", use_container_width=True, type="primary")
    
    st.markdown("""
        <div class="card-footer-text">
            Your resume is analyzed in real time and is not stored.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    return resume_content, job_description, analyze_clicked