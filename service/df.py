import streamlit as st

from generator.generator import *


def create_df(n_rows,n_col):

    data = {}
    columns = gen_columns(n_col)

    for i in columns:

        match columns[i][0]:
            case 'Int':
                data[i] = [gen_number(columns[i][1],columns[i][2]) for _ in range(n_rows)]
            case 'Float':
                data[i] = [gen_number(columns[i][1],columns[i][2],float=True) for _ in range(n_rows)]
            case 'Name':
                data[i] = [gen_names() for _ in range(n_rows)]
            case 'Lastname':
                data[i] = [gen_lastnames() for _ in range(n_rows)]
            case 'Custom':
                data[i] = [gen_custom(columns[i][1],columns[i][2]) for _ in range(n_rows)]
    return data
    