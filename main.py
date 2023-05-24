import streamlit as st

from cache.session_state import init_session_state
from content.main_page import main_page
from content.privacy_page import privacy_page

init_session_state()

if st.session_state.lgpd: main_page()

else: privacy_page()
