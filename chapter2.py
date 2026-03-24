import streamlit as st

st.title("Chai maker app")

if st.button("make chai"):
    st.success("your chai has been brewed")

masala=st.checkbox("add masala")

if masala:
    st.write("masala is avaiable")

tea_base=st.radio("pick your base:",["milk","water","almond milk"])
st.write(f"selected base {tea_base}")

flavour=st.selectbox("Choose flavour",["adrak","kesar","tulsi"])
st.write(f"Selected flavor {flavour}")

sugar=st.slider("Sugar level by teaspoon ",0,10,2)
st.write(f"selected level{sugar}")

st.number_input("how many cups",min_value=1,max_value=10)

name=st.text_input("enter name:")
if name:
    st.write(f"welcome {name} your chai is on the way")

dob = st.date_input("select your dob")
st.write(f"selected dob{dob}")