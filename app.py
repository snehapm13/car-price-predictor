import pickle
import pandas as pd
import streamlit as st

from login import login, logout
from chatbot import show_chatbot
from style import apply_custom_css


# Page settings
st.set_page_config(
    page_title="CarPrice AI",
    layout="wide"
)

# Apply UI design
apply_custom_css()

# Check login
if not login():
    st.stop()

# Load dataset
df = pd.read_csv("data/cars.csv")

# Load trained model
with open(
    "car_price_model.pkl",
    "rb"
) as file:
    model = pickle.load(file)

# Application header
st.markdown(
    """
    <div class="main-header">
        <h1>CarPrice AI</h1>
        <p>
            Used Car Price Prediction Application
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Logout button
top_left, top_right = st.columns(
    [5, 1]
)

with top_right:
    logout()

# Prediction section
with st.container(border=True):

    st.subheader("Enter Car Details")

    column1, column2, column3 = st.columns(3)

    with column1:
        year = st.number_input(
            "Manufacturing Year",
            min_value=2000,
            max_value=2026,
            value=2020,
            step=1
        )

    with column2:
        km_driven = st.number_input(
            "Kilometres Driven",
            min_value=0,
            value=50000,
            step=1000
        )

    with column3:
        engine = st.number_input(
            "Engine Capacity in CC",
            min_value=500,
            value=1200,
            step=100
        )

    predict_button = st.button(
        "Predict Price",
        use_container_width=True
    )

# Make prediction
if predict_button:

    input_data = pd.DataFrame(
        {
            "year": [year],
            "km_driven": [km_driven],
            "engine": [engine]
        }
    )

    predicted_price = model.predict(
        input_data
    )[0]

    st.success("Prediction completed.")

    st.metric(
        label="Estimated Car Price",
        value=f"₹{predicted_price:,.0f}"
    )

# Chatbot section
st.divider()

with st.container(border=True):

    show_chatbot(df)

# Footer
st.markdown(
    """
    <div class="footer">
        CarPrice AI | Data Science Project
    </div>
    """,
    unsafe_allow_html=True
)