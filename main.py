import pandas as pd
import streamlit as st


from service.df import create_df


rows = st.number_input('Number Rows', step=1)
columns = st.number_input('Number Columns', step=1)

data = create_df(rows,columns)

df = pd.DataFrame(data)
st.dataframe(df,use_container_width=True)

df_csv = df.to_csv()
st.download_button("Download",df_csv,file_name='generated_df.csv')
