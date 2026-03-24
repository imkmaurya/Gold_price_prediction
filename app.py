import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("trained_model.sav", "rb"))

st.title("Gold Price Prediction")

SPX = st.number_input("SPX")
GLD = st.number_input("GLD")
USO = st.number_input("USO")
SLV = st.number_input("SLV")

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "SPX": SPX,
        "GLD": GLD,
        "USO": USO,
        "SLV": SLV
    }])

    prediction = model.predict(input_data)
    st.success(f"Predicted Gold Price: {prediction[0]:.2f}")