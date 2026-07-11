from streamlit_option_menu import option_menu
import streamlit as st

def sidebar():

    with st.sidebar:

        selected = option_menu(

            "ResumeAI Pro",

            [

                "Dashboard",

                "Resume Analysis",

                "ATS Score",

                "Skills",

                "Suggestions"

            ],

            icons=[

                "speedometer2",

                "file-earmark",

                "graph-up",

                "award",

                "lightbulb"

            ],

            default_index=0

        )

    return selected