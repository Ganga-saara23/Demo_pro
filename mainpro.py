import streamlit as st
from streamlit_option_menu import option_menu

st.title('Project title')
with st.sidebar:
    selected = option_menu(
        menu_title='Project Title',
        options=['Abstract','Company Profile','System Analysis','System Requirements','Tasks','Modules']
    )
