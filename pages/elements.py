import streamlit as st


clicked = st.button("Click me!")
if clicked:
    st.write("Clicked!")

checked = st.checkbox("Check me!")
st.write(f"Check status :{checked}")

select_item = st.radio("Choose !", ['one','two','three'])
st.write(f"choosen :{select_item}")

select_box = st.selectbox("Choose !",['one','two','three'] )
st.write(select_box)