import streamlit as st

st.title("Chai taaste poll")
col1,col2=st.columns(2)

with col1:
    st.header("MAsala chai")
    vote1 = st.button("vote masala chai")
    st.image("https://tse1.mm.bing.net/th/id/OIP.9HyJGkUNm5_ZXqTtVwnqbgHaJQ?rs=1&pid=ImgDetMain&o=7&rm=3",width=100)
    st.write(f"Selected vote {vote1}")

with col2:
    st.header("adrak chai")
    vote2=st.button("vote adrak chai")
    st.image("https://tse3.mm.bing.net/th/id/OIP.7lOvc7nTPfoySGdsuzaUuAHaE8?rs=1&pid=ImgDetMain&o=7&rm=3",width=100)
    st.write(f"Selected vote {vote2}")


if vote1:
    st.success("your vote is given to masala chai")

else:
    
    st.success("your vote is given to adrak chai")

st.sidebar.text_input("enter your name")

with st.expander("show chaia maing instructions"):
    st.write("""
             1.boil water
             2. add milk and spices
             """)
    
st.markdown("### welcome to chaiclub")
st.markdown('> Blockquote')