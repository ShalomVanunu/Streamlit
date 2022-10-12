import streamlit as st



def load_file(name):
    with open(name,'rb') as f:
        data = f.read()
        return data

st.title("Welcome :tada:") #https://www.webfx.com/tools/emoji-cheat-sheet/

col1, col2= st.columns(2)
with col1:
    st.header("Learn Streamlit ")
with col2:
    data_file = load_file("streamlit.png")
    st.image(data_file, width=150)

st.write("------")

st.code(""" ## create python file . ex: app.py
import streamlit as st

st.write(" text ")

## to Run the code
## in Terminal CLI : > streamlit run app.py


""")

st.write("------")

with st.container():
    col1,col2,col3= st.columns(3)
    with col1:
        st.video("https://youtu.be/vIQQR_yq-8I")
    with col2:
        st.video("https://youtu.be/VqgUkExPvLY")
    with col3:
        st.video("https://youtu.be/_Um12_OlGgw")
st.write("------")
with st.container():
    col1,col2,col3= st.columns(3)
    with col1:
        st.video("https://youtu.be/YClmpnpszq8")
    with col2:
        st.video("https://youtu.be/VqgUkExPvLY")
    with col3:
        st.video("https://youtu.be/_Um12_OlGgw")

st.write("------")
st.subheader(" Created by :copyright:Shalom Vanunu :computer:")

