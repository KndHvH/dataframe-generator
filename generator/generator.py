import random
import streamlit as st
from streamlit_tags import st_tags
import string
import re
import radar
import datetime

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
        casetype = 'Lower' if lower else 'Upper'

    match casetype:

        case 'Lower':
            return gen_letter().lower()

        case 'Upper':
            return gen_letter().upper()

        case 'Random':
            return gen_letter()


def gen_columns(columns,config):

    content = get_content(columns, config)

    with st.expander('Configuracao Colunas', expanded=True):
        data = {}
        data_types = ['Int', 'Float', 'Name', 'Lastname','Date','Time','Custom','Category']
        
        for i,v in enumerate(content):
            col_e1 = None 
            col_e2 = None
            _cat = False
            c1, c2, c3, c4 = st.columns(4)
            with c1: col_name = st.text_input('Column Name', key=i+1000,value=v if config != None else get_letters_list()[i])
            with c2: col_data_type = st.selectbox('Column Type', data_types, key=i+10000,index=get_preselected_option(config[v][0] if config != None else 'Int'))

            match col_data_type:
                case'Int':
                    with c3: col_e1 = st.number_input('Start', step=1, key=i+100000,value=get_config_value(config,v,1,'int'))
                    with c4: col_e2 = st.number_input('Stop', step=1, key=i+1000000,value=get_config_value(config,v,2,'int'))
                case'Float':
                    with c3: col_e1 = st.number_input('Start', step=0.01, key=i+100000,value=get_config_value(config,v,1,'float'))
                    with c4: col_e2 = st.number_input('Stop', step=0.01, key=i+1000000,value=get_config_value(config,v,2,'float'))
                case'Date':
                    with c3: col_e1 = st.date_input('Start',key=i+100000,value=get_config_value(config,v,1,'date'))
                    with c4: col_e2 = st.date_input('Stop',min_value=col_e1,key=i+1000000,value=get_config_value(config,v,2,'date'))
                case'Custom':
                    with c3: col_e1 = st.text_input('Example', key=i+100000,value=get_config_value(config,v,1,'str'))
                    with c4: col_e2 = st.selectbox('MatchCase', ['Match', 'Lower', 'Upper', 'Random'], key=i+1000000)
                case'Category':
                    _cat = True
            if _cat: col_e1 = st_tags(label='Category Values',text='',key=i+100000,value=get_config_value(config,v,1,'list'))

            data[col_name] = [col_data_type, col_e1, col_e2]
        return data


def get_preselected_option(option):

    match option:
        case 'Int':
            return 0
        case 'Float':
            return 1
        case 'Name':
            return 2
        case 'Lastname':
            return 3
        case 'Date':
            return 4
        case 'Time':
            return 5
        case 'Custom':
            return 6
        case 'Category':
            return 7  
        
def get_config_value(config,column_name,index=1,type='int'):
    
    match type:
        case 'int':
            if config != None: return int(config[column_name][index])
            return 0 if index == 1 else 10
        case 'float':
            if config != None: return float(config[column_name][index])
            return 0.0 if index == 1 else 10.0
        case 'str':
            return '' if config == None else config[column_name][index]
        case 'date':
            return None if config == None else datetime.datetime.strptime(config[column_name][index], '%Y-%m-%d')
        
        case 'list':
            return None if config == None else list(eval(config[column_name][index]))



def get_content(columns, config):
    if config == None: return [0 for _ in range(columns)]
    
    content = list(config.keys())
    diff = columns - len(content)

    if diff > 0: content.append(0)
    if diff < 0: content.pop()
    return content