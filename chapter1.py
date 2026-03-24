import streamlit as st

st.title("Programming language 🚀")
st.write("Hello Kavya! This is your brother.")
st.subheader("kavya maurya")
st.text("hello how are u")

prog=st.selectbox("your fav programming lanuage:",["python","ruby","c++","java","js"])
st.text(f" you choose {prog} , excellent choice")

st.success("your languuage has been good")