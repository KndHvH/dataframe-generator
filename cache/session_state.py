import streamlit as st

def init_session_state():
    if 'imported_columns' not in st.session_state:
        st.session_state.imported_columns = None
    if 'imported' not in st.session_state:
        st.session_state.imported = False
