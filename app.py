import streamlit as st
from PIL import Image
import os

from weather import get_weather

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Smart Crop Loss Prediction",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
logo_path = "assets/logo.png"

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=160)

st.sidebar.title("🌾 SmartCropLoss")

st.sidebar.markdown("---")

st.sidebar.success("Farmer Decision Support System")

st.sidebar.markdown("""
This application helps farmers to:

🌾 Crop Recommendation

📉 Crop Loss Prediction

🧠 Explainable AI (XAI)

💰 Profit Estimation

🌿 Fertilizer Recommendation

💧 Irrigation Recommendation

🌦 Real-Time Weather

🏛 Government Schemes
""")

st.sidebar.markdown("---")

st.sidebar.info("👈 Select a page from the left sidebar.")

# --------------------------------------------------
# Main Title
# --------------------------------------------------
st.title("🌾 Smart Crop Loss Prediction and Explainable Risk Analysis")

st.markdown("---")

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
left, right = st.columns([2,1])

with left:

    st.header("Welcome")

    st.write("""
Welcome to the **Smart Crop Loss Prediction and Explainable Risk Analysis System**.

This AI-powered decision support system is designed to help farmers make
better agricultural decisions using Machine Learning, Explainable AI,
Weather Forecasting and Smart Farming Analytics.

The application analyses various agricultural parameters and provides
intelligent recommendations to reduce farming risks and improve productivity.
""")

with right:

    farmer_path = "assets/farmer.png"

    if os.path.exists(farmer_path):
        st.image(farmer_path, use_container_width=True)

st.markdown("---")

# --------------------------------------------------
# Features
# --------------------------------------------------
st.header("🌱 Project Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
✅ Crop Recommendation

✅ Crop Loss Prediction

✅ Profit Estimation

✅ Fertilizer Recommendation

✅ Irrigation Recommendation
""")

with col2:

    st.markdown("""
✅ Soil Analysis

✅ Rainfall Analysis

✅ Weather Information

✅ Government Schemes

✅ Explainable AI (XAI)
""")

st.markdown("---")

# --------------------------------------------------
# AI Section
# --------------------------------------------------
# --------------------------------------------------
# Real-Time Weather Information
# --------------------------------------------------

st.markdown("---")

st.header("🌦 Real-Time Weather Information")

city = st.text_input(
    "Enter District/City Name",
    value="Hyderabad"
)

if st.button("Get Weather Data", key="weather_data_button"):

    weather = get_weather(city)

    if "error" in weather:

        st.error(weather["error"])

    else:

        st.success(
            f"Weather data fetched successfully for "
            f"{weather['city']}, {weather['country']}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🌡 Temperature",
                f"{weather['temperature']:.2f} °C"
            )

        with col2:
            st.metric(
                "💧 Humidity",
                f"{weather['humidity']} %"
            )

        with col3:
            st.metric(
                "🌧 Rainfall (1 Hour)",
                f"{weather['rainfall_1h']:.2f} mm"
            )

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric(
                "🌡 Feels Like",
                f"{weather['feels_like']:.2f} °C"
            )

        with col5:
            st.metric(
                "💨 Wind Speed",
                f"{weather['wind_speed']} m/s"
            )

        with col6:
            st.metric(
                "☁ Cloud Coverage",
                f"{weather['clouds']} %"
            )

        st.write(
            f"**Weather Condition:** "
            f"{weather['description'].title()}"
        )

        st.write(
            f"**Atmospheric Pressure:** "
            f"{weather['pressure']} hPa"
        )

# --------------------------------------------------
# Workflow
# --------------------------------------------------
st.header("📌 How It Works")

st.markdown("""
### Step 1
Enter Farm Details

### Step 2
Analyze Farm

### Step 3
AI predicts:

- 🌾 Best Crop
- 📉 Crop Loss Risk
- 💰 Expected Profit
- 🌿 Fertilizer
- 💧 Irrigation
- 🌦 Weather
- 🏛 Government Schemes

### Step 4
View Explainable AI (XAI)

Understand **why** the model recommended that crop and predicted that level of risk.
""")

st.markdown("---")

# --------------------------------------------------
# Objectives
# --------------------------------------------------
st.header("🎯 Project Objectives")

st.markdown("""
✔ Reduce crop losses.

✔ Improve farmer decision making.

✔ Recommend the most suitable crop.

✔ Increase agricultural productivity.

✔ Improve profitability.

✔ Explain AI predictions using Explainable AI (XAI).

✔ Support sustainable farming practices.
""")

st.markdown("---")
# --------------------------------------------------
# Real-Time Weather Information
# --------------------------------------------------

st.markdown("---")

st.header("🌦 Real-Time Weather Information")

city = st.text_input(
    "Enter District/City Name",
    value="Hyderabad",
    key="weather_city"
)

if st.button("Get Weather Data"):

    weather = get_weather(city)

    if "error" in weather:

        st.error(weather["error"])

    else:

        st.success(
            f"Weather data fetched successfully for "
            f"{weather['city']}, {weather['country']}"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "🌡 Temperature",
                f"{weather['temperature']:.2f} °C"
            )

        with col2:
            st.metric(
                "💧 Humidity",
                f"{weather['humidity']} %"
            )

        with col3:
            st.metric(
                "🌧 Rainfall (1 Hour)",
                f"{weather['rainfall_1h']:.2f} mm"
            )

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric(
                "🌡 Feels Like",
                f"{weather['feels_like']:.2f} °C"
            )

        with col5:
            st.metric(
                "💨 Wind Speed",
                f"{weather['wind_speed']} m/s"
            )

        with col6:
            st.metric(
                "☁ Cloud Coverage",
                f"{weather['clouds']} %"
            )

        st.write(
            f"**Weather Condition:** "
            f"{weather['description'].title()}"
        )

        st.write(
            f"**Atmospheric Pressure:** "
            f"{weather['pressure']} hPa"
        )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.success(
"""
🌱 Empowering Farmers with AI-Based Crop Recommendation,
Crop Loss Prediction, Explainable Risk Analysis,
Profit Estimation and Smart Farming Decisions.
"""
)
