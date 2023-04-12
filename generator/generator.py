import random
import streamlit as st

def gen_number(start=0, stop=11,float=False):
    if float: return random.uniform(start,stop)
    return random.randrange(start,stop)




def gen_columns(columns):
    data = {}
    for i in range(columns):
        c1, c2, c3, c4 = st.columns(4)
        with c1: col_name = st.text_input('Column Name', key=i+10)
        with c2: col_data_type = st.selectbox('Column Type', ['Int', 'Float'], key=i+100)

        if col_data_type == 'Int' or col_data_type == 'Float':
            with c3: col_e1 = st.number_input('Start', step=1, key=i+1000)
            with c4: col_e2 = st.number_input('Stop',value=10, step=1, key=i+10000)
        
        data[col_name] = [col_data_type,col_e1,col_e2]

    return data



