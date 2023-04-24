import pandas as pd
import streamlit as st
from cache.session_state import init_session_state
from service.df import create_df

init_session_state()

c1, c2, c3 = st.columns(3)
with c1: table_name = st.text_input('Table Name',value='table')
with c2: rows = st.number_input('Number Rows', step=1)
with c3: columns = st.number_input('Number Columns', step=1,max_value=702, value=len(st.session_state.upload_columns) if st.session_state.upload_columns else 0)

data, gen_columns = create_df(rows, columns,st.session_state.upload_columns)

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
df_csv = df.to_csv(index=False)

save_df = pd.DataFrame(gen_columns)
save_file = save_df.to_csv(index=False)


c1, c2, c3 = st.columns(3)

with c1: st.download_button("Download", df_csv, file_name=f'{table_name}.csv', use_container_width=True)
with c2: st.download_button("Save config", save_file,file_name=f'save_file_{table_name}.csv', use_container_width=True)
with c3:
    if st.button('Import config', use_container_width=True):
        st.session_state.upload_columns = None
        st.session_state.upload = True
        st.experimental_rerun()

if st.session_state.upload:
    file = st.file_uploader('Upload Config', type='csv')
    if file:        
        st.session_state.upload_columns = pd.read_csv(file).to_dict()
        st.session_state.upload = False
        st.experimental_rerun()
