import pandas as pd
import streamlit as st
from cache.session_state import init_session_state
from service.df import create_df
from streamlit import caching

init_session_state()    

c1,c2,c3 = st.columns(3)
with c1:
    table_name = st.text_input('Table Name')
with c2:
    rows = st.number_input('Number Rows', step=1)
with c3:
    columns = st.number_input('Number Columns', step=1)

if st.session_state.imported and st.session_state.imported_columns:
    dataframe = pd.read_csv(st.session_state.imported_columns)
    st.write(dataframe)

data, gen_columns = create_df(rows,columns)


df = pd.DataFrame(data)
st.dataframe(df,use_container_width=True)
df_csv = df.to_csv(index=False)

save_df = pd.DataFrame(gen_columns)
save_file = save_df.to_csv(index=False)



c1,c2,c3,c4 = st.columns(4)

with c1:
    st.download_button("Download",df_csv,file_name=f'{table_name}.csv',use_container_width=True) 
with c2:
    st.download_button("Save config",save_file,file_name=f'save_file_{table_name}.csv',use_container_width=True)
with c3:
    if st.button('Import config',use_container_width=True):
        st.session_state.imported = True
        st.experimental_rerun()
with c4:
    if st.button('Clear page',use_container_width=True):
        st.session_state.imported_columns = None
        st.session_state.imported = False
        caching.clear_cache()
        st.experimental_rerun()


if st.session_state.imported:
    file = st.file_uploader('Upload Config',type='csv')
    st.session_state.imported_columns = file