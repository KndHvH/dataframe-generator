import streamlit as st


def init_session_state():
    if 'upload_columns' not in st.session_state:
        st.session_state.upload_columns = None
    if 'upload' not in st.session_state:
        st.session_state.upload = False
    if 'lgpd' not in st.session_state:
        st.session_state.lgpd = False

