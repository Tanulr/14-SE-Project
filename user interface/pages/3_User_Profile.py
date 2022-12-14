import streamlit as st
import settings
from nav import *

no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

if not settings.status[-1]:
    st.warning("You must log-in to see the content of this sensitive page! Head over to the log-in page.")
    if st.button("Home page"):
        nav_page("")
    if st.button("Log in page"):
        nav_page("Log_in")
    if st.button("Sign up page"):
        nav_page("Sign_up")

if st.button("Create survey"):
    nav_page("Create_survey")

if st.button("View current survey responses"):
    nav_page("View_Responses")

if st.button("Answer current surveys"):
    nav_page("Answer_surveys")

elif st.button("Log out"):
    nav_page("")
    settings.status.append(False)
