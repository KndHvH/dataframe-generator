import random
import streamlit as st

def gen_number(start=0, stop=10,float=False):
    if float: return random.uniform(start,stop)
    return random.randrange(start,stop)

def gen_phonenumber():
    return f'{gen_number(90000,99999)}-{gen_number(1000,9999)}'

def gen_rg():
    return f'{gen_number(10,99)}.{gen_number(100,999)}.{gen_number(100,999)}-{gen_number(0,10)}'

def gen_cpf():
    return f'{gen_number(100,999)}-{gen_number(100,999)}-{gen_number(100,999)}/{gen_number(10,99)}'


def gen_columns(columns):
    data = {}
    data_types = ['Int', 'Float','Phone-Number','RG','CPF']
    col_e1 = None
    col_e2 = None
    for i in range(columns):
        c1, c2, c3, c4 = st.columns(4)
        with c1: col_name = st.text_input('Column Name', key=i)
        with c2: col_data_type = st.selectbox('Column Type', data_types, key=i+10)

        match col_data_type:
            case'Int' :
                with c3: col_e1 = st.number_input('Start', step=1, key=i+100)
                with c4: col_e2 = st.number_input('Stop',value=10, step=1, key=i+1000)
            case'Float':
                with c3: col_e1 = st.number_input('Start', step=0.01, key=i+100)
                with c4: col_e2 = st.number_input('Stop',value=10, step=1, key=i+1000)
            
        data[col_name] = [col_data_type,col_e1,col_e2]

    return data



