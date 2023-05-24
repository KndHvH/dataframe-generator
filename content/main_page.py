
import streamlit as st
import pandas as pd

from service.df import create_df

LOGO_PATH = './pics/hitss2.png'


def main_page():

    table_name, n_rows, n_columns = main_page_header()

    data, gen_columns = create_df(n_rows, n_columns,st.session_state.upload_columns)

    df = pd.DataFrame(data)
    save_df = pd.DataFrame(gen_columns)

    st.dataframe(df, use_container_width=True)

    df_csv = df.to_csv(index=False)
    save_file = save_df.to_csv(index=False)

    main_page_botton(df_csv,save_file,table_name)

def main_page_cfg():
    st.set_page_config( page_title = 'Dataframe Generator',
                    page_icon = LOGO_PATH,
                    layout='centered')


def main_page_header():

    c1, c2, c3 = st.columns(3)
    with c1: table_name = st.text_input('Table Name',value='TABLE')
    with c2: columns = st.number_input('Number Columns', step=1,max_value=702, value=len(st.session_state.upload_columns) if st.session_state.upload_columns else 0)
    with c3: rows = st.number_input('Number Rows', step=1)

    return table_name, rows, columns


def main_page_botton(df_csv,save_file,table_name):
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
