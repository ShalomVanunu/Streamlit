#Youtube
#https://www.youtube.com/watch?v=vIQQR_yq-8I
import streamlit as st


clicked = st.button("st.button()  --> Click me!")
if clicked:
    st.success("Clicked!")

checked = st.checkbox("st.checkbox()   --> Check me!")
st.write(f"Check status :{checked}")

select_item = st.radio("st.radio()    --> Choose !", ['one','two','three'])
st.write(f"choosen :{select_item}")

select_box = st.selectbox(" st.selectbox()   --> ChooseChoose !",['one','two','three'] )
st.write(select_box)

select_items = st.multiselect(
    "st.multiselect()     --> Columns to use",
    ["Col1","Col2","Col3"]
)
st.write(select_items)

value = st.slider("st.slider()     --> Label", value=10 )
st.write(f"Value: {value}")
range_value = st.slider("Label", value=(100,200 ))

select_slider = st.select_slider(
    "st.select_slider()      --> Select a step",options = ["step1","step2","step3" ]
)


