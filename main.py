import streamlit as st

from cache.session_state import init_session_state
from content.main_page import main_page, main_page_cfg
from content.privacy_page import privacy_page

init_session_state()
main_page_cfg()

st.image('pics\hitss.png')

if st.session_state.lgpd: main_page()

else: privacy_page()
