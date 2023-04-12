import streamlit as st

from generator.generator import gen_columns, gen_number


def create_df(n_rows,n_col):

    data = {}
    columns = gen_columns(n_col)

    for i in columns:

        match columns[i][0]:
            case 'Int':
                data[i] = [gen_number(columns[i][1],columns[i][2]) for _ in range(n_rows)]
            case 'Float':
                data[i] = [gen_number(columns[i][1],columns[i][2],float=True) for _ in range(n_rows)]

    return data
    