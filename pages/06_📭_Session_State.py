import streamlit as st

st.button("st.button()  --> Click me!", key="click")
clicked = st.session_state.click
st.write(clicked)