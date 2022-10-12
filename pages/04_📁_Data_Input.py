#Youtube
#https://www.youtube.com/watch?v=vIQQR_yq-8I
import streamlit as st
import datetime as date

name = st.text_input(" st.text_input()  --> input name")
if name !="":
    st.markdown(name)

password = st.text_input(" st.text_input() ,type='password' --> input password", type="password")

text_area = st.text_area(" st.text_area() --> Type text")

number_inpuut = st.number_input("st.number_input()  --> ",
                                min_value=0,
                                max_value=100,
                                step=10)

date_input = st.date_input("st.date_input()    --> ")
if date_input:
    st.write(date_input)

range_input = st.date_input("st.date_input( " ",value=)    --> ",
                            value=(date.datetime.now(),date.datetime.now()))

time_input = st.time_input("st.time_inpdut()     -->  ")

camera_photo = st.camera_input("st.camera_input  ---> Take Photo")