import streamlit as st


def score_card(score):

    st.markdown(
        f"""
        <div class="dashboard-card">
            <div style="text-align:center">
                <div class="score-circle">
                    <div class="score-inner">
                        <div class="score-number">{score}</div>
                        <div class="score-text">/100</div>
                    </div>
                </div>
                <h3 style="margin-top:20px;">
                    ATS Score
                </h3>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
def progress_bar(title, percent):
    st.markdown(
        f"""
    <div style="margin-bottom:18px;">
        <div style="
        display:flex;
        justify-content:space-between;
        color:white;
        margin-bottom:6px;">
            <span>{title}</span>
            <span>{percent}%</span>
        </div>
        <div style="
        width:100%;
        background:#374151;
        height:10px;
        border-radius:20px;">
            <div style="
            width:{percent}%;
            background:#22C55E;
            height:10px;
            border-radius:20px;">
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

def skill_badge(skill):
    st.markdown(
        f"""
    <span class="skill-badge">
        {skill}
    </span>
    """,
    unsafe_allow_html=True
)

def missing_badge(skill):
    st.markdown(
        f"""
    <span class="missing-badge">
        {skill}
    </span>
    """,
    unsafe_allow_html=True
)

def suggestion_card(text):
    st.markdown(
        f"""
    <div class="tip">
        ✔ {text}
    </div>
    """,
    unsafe_allow_html=True
)

import streamlit as st


def metric_card(title, value, icon, color="#22C55E"):
    st.markdown(
        f"""
        <div style="background:#1E293B; padding:25px; border-radius:22px; box-shadow: 0 10px 25px rgba(0,0,0,.25); height:170px;">
            <div style="font-size:18px; color:#CBD5E1;">
                {icon} {title}
            </div>
            <div style="font-size:42px; font-weight:bold; color:{color}; margin-top:18px;">
                {value}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

