import pandas as pd
import streamlit as st


from service.df import create_df

c1,c2,c3 = st.columns(3)

with c1:
    table_name = st.text_input('Table Name')
with c2:
    rows = st.number_input('Number Rows', step=1)
with c3:
    columns = st.number_input('Number Columns', step=1)

data = create_df(rows,columns)

df = pd.DataFrame(data)
st.dataframe(df,use_container_width=True)

df_csv = df.to_csv(index=False)
st.download_button("Download",df_csv,file_name=f'{table_name}.csv')
