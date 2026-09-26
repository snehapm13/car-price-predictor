import pickle
from datetime import datetime

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

apply_custom_css()


# Login
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
header_left, header_right = st.columns(
    [5, 1]
)

with header_right:
    logout()


# Car input section
current_year = datetime.now().year

with st.container(border=True):

    st.subheader("Enter Car Details")

    input1, input2, input3 = st.columns(3)

    with input1:

        year = st.number_input(
            "Manufacturing Year",
            min_value=2000,
            max_value=current_year,
            value=2020,
            step=1
        )

    with input2:

        km_driven = st.number_input(
            "Kilometres Driven",
            min_value=0,
            value=50000,
            step=1000
        )

    with input3:

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


# Prediction section
if predict_button:

    # Create input data
    input_data = pd.DataFrame(
        {
            "year": [year],
            "km_driven": [km_driven],
            "engine": [engine]
        }
    )

    # Predict price
    predicted_price = model.predict(
        input_data
    )[0]

    # Calculate price range
    minimum_price = predicted_price * 0.90
    maximum_price = predicted_price * 1.10

    st.success(
        "Car price prediction completed."
    )

    # Display price cards
    result1, result2, result3 = st.columns(3)

    with result1:

        st.metric(
            label="Predicted Market Price",
            value=f"₹{predicted_price:,.0f}"
        )

    with result2:

        st.metric(
            label="Minimum Expected Price",
            value=f"₹{minimum_price:,.0f}"
        )

    with result3:

        st.metric(
            label="Maximum Expected Price",
            value=f"₹{maximum_price:,.0f}"
        )

    # Price range
    st.info(
        "Expected Price Range: "
        f"₹{minimum_price:,.0f} to "
        f"₹{maximum_price:,.0f}"
    )

    # Create price comparison data
    price_chart_data = pd.DataFrame(
        {
            "Price": [
                minimum_price,
                predicted_price,
                maximum_price
            ]
        },
        index=[
            "Minimum Price",
            "Predicted Price",
            "Maximum Price"
        ]
    )

    # Display price comparison chart
    st.subheader("Price Comparison Chart")

    st.bar_chart(price_chart_data)


# Dataset chart section
st.divider()

with st.container(border=True):

    st.subheader("Car Dataset Charts")

    # Calculate average price by brand
    brand_price = (
        df.groupby("brand")["selling_price"]
        .mean()
        .sort_values(ascending=False)
    )

    # Calculate average price by year
    year_price = (
        df.groupby("year")["selling_price"]
        .mean()
        .sort_index()
    )

    # Create chart tabs
    brand_tab, year_tab = st.tabs(
        [
            "Price by Brand",
            "Price by Year"
        ]
    )

    with brand_tab:

        st.write(
            "Average Selling Price by Brand"
        )

        st.bar_chart(brand_price)

    with year_tab:

        st.write(
            "Average Selling Price by Year"
        )

        st.line_chart(year_price)


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