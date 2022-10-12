#Youtube
#https://www.youtube.com/watch?v=vIQQR_yq-8I
import pandas as pd
import streamlit as st


file_data = st.file_uploader("st.file_uploader()  ---> ", type=["csv"])

if file_data is not None:
    df = pd.read_csv(file_data)
    st.dataframe(df)
    st.download_button(
        label="st.download_button()  ---> Download data as CSV",
        data=file_data,
        file_name='large_df.csv',
        mime='text/csv', )

