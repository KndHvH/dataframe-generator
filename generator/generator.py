import random
import streamlit as st
from streamlit_tags import st_tags
import string
import re
import radar

from service.pool import *


def gen_number(start=0, stop=10, float=False):
    if float:
        return random.uniform(start, stop)
    return random.randrange(start, stop)


def gen_names():
    return random.choice(get_namelist())


def gen_lastnames():
    return random.choice(get_lastnamelist())


def gen_letter():
    return random.choice(string.ascii_letters)

def gen_category(list):
    return random.choice(list)

def gen_date(start,stop):
    date = radar.random_datetime(start,stop)
    return date.strftime("%d.%m.%Y")

def gen_time():
    hour = f'{gen_number(0,3)}{gen_number()}'
    minute = f'{gen_number(0,6)}{gen_number()}'
    second = f'{gen_number(0,6)}{gen_number()}'
    return f"{hour}:{minute}:{second}"

def gen_custom(example, casetype):
    output = []
    skip = False
    for i in example:
        if i == '~':
            skip = False if skip else True
            continue

        if skip: 
            output.append(i)
            continue

        if re.search('\d', i):
            output.append(str(gen_number()))
            continue

        if re.search('[a-z]', i):
            output.append(match_letter(casetype))
            continue

        if re.search('[A-Z]', i):
            output.append(match_letter(casetype, lower=False))
            continue

        output.append(i)

    return ''.join(output)


def match_letter(casetype, lower=True):
    if casetype == 'Match':
        casetype = 'Lower' if lower else 'High'

    match casetype:

        case 'Lower':
            return gen_letter().lower()

        case 'High':
            return gen_letter().upper()

        case 'Random':
            return gen_letter()


def gen_columns(columns):
    with st.expander('Configuracao Colunas', expanded=True):
        data = {}
        data_types = ['Int', 'Float', 'Name', 'Lastname','Date','Time','Custom','Category']
        col_e1 = None
        col_e2 = None
        for i in range(columns):
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                col_name = st.text_input('Column Name', key=i)
            with c2:
                col_data_type = st.selectbox(
                    'Column Type', data_types, key=i+10)

            match col_data_type:
                case'Int':
                    with c3:
                        col_e1 = st.number_input('Start', step=1, key=i+100)
                    with c4:
                        col_e2 = st.number_input(
                            'Stop', value=10, step=1, key=i+1000)
                case'Float':
                    with c3:
                        col_e1 = st.number_input('Start', step=0.01, key=i+100)
                    with c4:
                        col_e2 = st.number_input(
                            'Stop', value=10, step=1, key=i+1000)
                case'Date':
                    with c3:
                        col_e1 = st.date_input('Start',key=i+100)
                    with c4:
                        col_e2 = st.date_input('Stop',min_value=col_e1,key=i+1000)

                case'Custom':
                    with c3:
                        col_e1 = st.text_input('Example', key=i+100)
                    with c4:
                        col_e2 = st.selectbox(
                            'MatchCase', ['Match', 'Lower', 'Upper', 'Random'], key=i+1000)
                case'Category':
                    with c3:
                        col_e1 = st_tags(label='Category Values',text='',key=i+100)
                        # TODO remove text

            data[col_name] = [col_data_type, col_e1, col_e2]
        return data
