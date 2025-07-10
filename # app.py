# app.py

import streamlit as st
import joblib

# Load model
model = joblib.load("liquidity_model.pkl")

# Title
st.title("Cryptocurrency Liquidity Predictor")

# Input fields
volume = st.number_input("24h Volume", min_value=0.0, format="%.4f")
ma_7 = st.number_input("7-Day Moving Average", min_value=0.0, format="%.4f")
volatility = st.number_input("Volatility", min_value=0.0, format="%.4f")
liquidity_ratio = st.number_input("Liquidity Ratio", min_value=0.0, format="%.4f")

# Prediction
if st.button("Predict Liquidity"):
    features = [[volume, ma_7, volatility, liquidity_ratio]]
    prediction = model.predict(features)
    st.success(f"Predicted Liquidity: {prediction[0]:.4f}")
import joblib
import streamlit as st

st.success(" joblib loaded successfully!")
