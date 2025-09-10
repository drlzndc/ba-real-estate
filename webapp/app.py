import os
import sys
import joblib
import pandas
import streamlit as st


current_dir = os.path.dirname(os.path.abspath(__file__))
dir_prefix  = "../" if current_dir == "/app/webapp" else ""

# Enable import of custom helpers
sys.path.append(os.path.abspath(dir_prefix + "helpers"))

# Import custom helpers
from modeling            import *
from feature_engineering import *


model = joblib.load(dir_prefix + "models/best_model.joblib")

st.title("Apartment Price Predictor (BiH)")
st.info("The model was trained on around 2,500 listings from OLX.ba.")
st.info(
    "It has r² of **0.77** and MAE of around **26,000** — it explains around "
    "**77%** of the price variation and is on average off by about **26,000 €** "
    "on the training data, where prices ranged from 10,000 € to 900,000 €."
)
st.write("---")
st.info(
    "Select apartment features below and click 'Predict' get the model's "
    "prediction for the price."
)

area      = st.number_input("Area (m²)", min_value=5, max_value=500)
type      = st.selectbox("Apartment type", list(rooms_mapping.keys()))
state     = st.selectbox("State of the apartment", ["not listed", "used", "new"])
posted_by = st.selectbox("Listed by", ["individual", "agency"])
city      = st.selectbox("City", cities_by_popularity)

if st.button("Predict"):
    X = pandas.DataFrame(
        [[state, type, area, posted_by, city]],
        columns=["state", "type", "m²", "posted_by", "city"]
    )
    price = int(round(model.predict(X)[0], -3))
    
    st.write("---")
    st.metric(label="Predicted Price", value=f"{price:,.0f} €")

