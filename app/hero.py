import streamlit as st

def hero():
    # Render Headline

    st.markdown("""
    <h1 class="hero-title">
        Know exactly why your resume gets <span class="hero-highlight">filtered out</span> — or gets an interview.
    </h1>
    """, unsafe_allow_html=True)
    
    # Render Subheadline
    st.markdown("""
    <p class="hero-subtitle">
        Get an instant, structured evaluation of your resume: an ATS compatibility score, a hiring-manager readability score, and specific, prioritized fixes.
    </p>
    """, unsafe_allow_html=True)
    
    # Render Stats Row
    st.markdown("""
    <div class="stats-container">
        <div class="stat-item">
            <div class="stat-number">98%</div>
            <div class="stat-label">of Fortune 500 use ATS filtering</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">&lt;30s</div>
            <div class="stat-label">average analysis time</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">6</div>
            <div class="stat-label">evaluation dimensions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)