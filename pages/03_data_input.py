#Youtube
#https://www.youtube.com/watch?v=vIQQR_yq-8I
import streamlit as st

name = st.text_input(" st.text_input()  --> input name")
if name !="":
    st.markdown(name)

password = st.text_input(" st.text_input() ,type='password' --> input password", type="password")

text_area = st.text_area(" st.text_area() --> Type text")