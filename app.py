import streamlit as st

def load_file(name):
    with open(name,'rb') as f:
        data = f.read()
        return data


col1, col2= st.columns(2)

with col1:
    st.write(" add column : st.columns(2)")
    data_file = load_file("streamlit.png")
    st.image(data_file, width=100)
with col2:
    st.write(" add column : st.columns(2)")
    st.write("Referance https://docs.streamlit.io/library/api-reference ")



st.title("import streamlit as st")
st.write("------")
st.title("write title : st.title() :tada:") #https://www.webfx.com/tools/emoji-cheat-sheet/
st.write(" icons from https://www.webfx.com/tools/emoji-cheat-sheet/")

st.header("write header : st.header() ")
st.subheader("write subheader : st.subheader() ")
st.write("write text or variable : st.write() ")
st.caption("write caption : st.caption() ")
st.code("write code : st.code() ")


