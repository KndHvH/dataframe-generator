import random
import streamlit as st
import string
import re

from service.pool import *

def gen_number(start=0, stop=10,float=False):
    if float: return random.uniform(start,stop)
    return random.randrange(start,stop)

def gen_names():
    return random.choice(get_namelist())

def gen_lastnames():
    return random.choice(get_lastnamelist())

def gen_letter():
    return random.choice(string.ascii_letters)

def gen_custom(example,casetype):
    output = []
    for i in example:
        if re.search('\d',i): output.append(str(gen_number()))

        elif re.search('[a-z]',i):
            output.append(match_letter(casetype))

        elif re.search('[A-Z]',i):
            output.append(match_letter(casetype,lower=False))

        else: output.append(i)

    return ''.join(output)

 
 
def match_letter(casetype,lower=True):
    if casetype == 'Match': casetype = 'Lower' if lower else 'High'

    match casetype:

        case 'Lower':
            return gen_letter().lower()

        case 'High':
            return gen_letter().upper()
        
        case 'Random':
            return gen_letter()

def gen_columns(columns):
    with st.expander('Configuracao Colunas',expanded=True):
        data = {}
        data_types = ['Int', 'Float','Name','Lastname','Custom']
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
                case'Custom':
                    with c3: col_e1 = st.text_input('Example', key=i+100)
                    with c4: col_e2 = st.selectbox('MatchCase',['Match','Lower','Upper','Random'], key=i+1000)
                
            data[col_name] = [col_data_type,col_e1,col_e2]

        return data



