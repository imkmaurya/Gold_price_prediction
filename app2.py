import streamlit as st
import pandas as pd
import pickle


loaded_model=pickle.load(open("trained_model.sav","rb"))


st.title("Car price prediction")

year=st.number_input("Year")
Present_Price=st.number_input("Present_price")
Kms_Driven=st.number_input("Kms_Driven")
Fuel_Type=st.text_input("Fuel_Type")
Seller_Type=st.text_input("Seller_Type")
Transmission=st.text_input("Transmission")

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "year":year,
        "Present_Price": Present_Price,
        "Kms_Driven": Kms_Driven,
        "Fuel_Type": Fuel_Type,
        "Seller_Type": Seller_Type,
        "Transmission": Transmission
        

    }])

    prediction = loaded_model.predict(input_data)
    st.success(f"Predicted car Price: {prediction[0]:.2f}")