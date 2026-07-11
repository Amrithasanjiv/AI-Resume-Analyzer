import streamlit as st
import re
from ui_components import metric_card, progress_bar, skill_badge, missing_badge, suggestion_card

def dashboard():
    # Access state variables populated by the ML pipeline
    resume_text = st.session_state.get("resume_text", "")
    predicted_category = st.session_state.get("predicted_category", "UNKNOWN")
    skills = st.session_state.get("skills", [])
    ats_score = st.session_state.get("ats_score", 0)
    missing_skills = st.session_state.get("missing_skills", [])
    suggestions = st.session_state.get("suggestions", [])
    
    # Calculate word count
    word_count = len(resume_text.split())
    
    # Section Header
    st.markdown('<hr style="border: 1px solid rgba(255,255,255,0.08); margin: 50px 0;"><h1 class="title" id="results">📋 Resume Analysis Report</h1>', unsafe_allow_html=True)
    
    # 1. Overview Metrics Row
    col1, col2, col3 = st.columns(3)
    with col1:
        metric_card("Predicted Domain", predicted_category, "🎯", color="#6366F1")
    with col2:
        metric_card("Skills Found", str(len(skills)), "🏆", color="#10B981")
    with col3:
        metric_card("Resume Word Count", str(word_count), "📝", color="#F59E0B")
        
    st.write("")
    
    # 2. ATS Score Circle & Breakdown Progress Bars
    left, right = st.columns([1, 2])
    with left:
        gradient_deg = int(3.6 * ats_score)
        st.markdown(f"""
        <div class="dashboard-card" style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:340px;">
            <h3 style="text-align:center; margin-bottom:15px;">ATS Match Score</h3>
            <div class="score-circle" style="background: conic-gradient(#10B981 0deg, #10B981 {gradient_deg}deg, #374151 {gradient_deg}deg);">
                <div class="score-inner">
                    <div class="score-number">{ats_score}</div>
                    <div class="score-text">/100</div>
                </div>
            </div>
            <h4 style="text-align:center; margin-top:20px; color:{"#10B981" if ats_score >= 70 else "#F59E0B" if ats_score >= 50 else "#EF4444"};">
                {"Excellent Resume" if ats_score >= 75 else "Good Progress" if ats_score >= 50 else "Needs Improvement"}
            </h4>
        </div>
        """, unsafe_allow_html=True)
        
    with right:
        st.markdown('<div class="dashboard-card" style="height: 340px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="margin-bottom: 20px;">Score Breakdown</h3>', unsafe_allow_html=True)
        
        # Calculate sub-scores
        keyword_coverage = min(len(skills) * 10, 100)
        section_completeness = 0
        sections = ["education", "experience", "skills", "project", "certification"]
        for section in sections:
            if section in resume_text.lower():
                section_completeness += 20
        formatting_quality = 90 if word_count >= 250 and word_count <= 800 else 60
        parsing_confidence = 95
        
        progress_bar("Keyword Coverage", keyword_coverage)
        progress_bar("Section Completeness", section_completeness)
        progress_bar("Formatting Quality", formatting_quality)
        progress_bar("Parsing Confidence", parsing_confidence)
        st.markdown('</div>', unsafe_allow_html=True)
        
    st.write("")
    
    # 3. Skills Match & Gap Analysis
    st.markdown('<div class="glass"><h2>🏆 Skill Alignment & Gap Analysis</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<h3 style="color: #10B981;">🟢 Skills Found</h3>', unsafe_allow_html=True)
        if skills:
            for skill in skills:
                st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
        else:
            st.write("No matching skills identified.")
    with col2:
        st.markdown('<h3 style="color: #F59E0B;">🟠 Missing Skills</h3>', unsafe_allow_html=True)
        if missing_skills:
            for skill in missing_skills:
                st.markdown(f'<span class="missing-badge">{skill}</span>', unsafe_allow_html=True)
        else:
            st.write("Excellent! You match all the skills for this profile.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 4. Suggestions for Improvement
    st.markdown('<div class="glass"><h2>💡 Suggestions for Improvement</h2>', unsafe_allow_html=True)
    if suggestions:
        for suggestion in suggestions:
            suggestion_card(suggestion)
    else:
        st.success("Your resume looks great! No suggestions found.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 5. Plain Text Preview (Collapsible)
    with st.expander("📄 View Parsed Resume Plain Text"):
        st.text_area("Extracted Resume Text", resume_text, height=250, disabled=True)