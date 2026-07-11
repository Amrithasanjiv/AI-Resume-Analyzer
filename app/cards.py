import streamlit as st


def section(title):

    st.markdown(f"""
    <h2 style="
    color:white;
    margin-top:25px;
    margin-bottom:20px;
    ">
    {title}
    </h2>
    """,
    unsafe_allow_html=True)