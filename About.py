import streamlit as st


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="About SmartCropLoss",
    page_icon="🌾",
    layout="wide"
)


# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🌾 About SmartCropLoss")

st.markdown("""
## Smart Crop Loss Prediction and Explainable Risk Analysis

**SmartCropLoss** is an AI-powered agricultural decision-support
system designed to help farmers make better farming decisions.

The system combines **Machine Learning, Explainable AI (XAI),
Real-Time Weather Information and Smart Farming Analytics**
to provide useful agricultural insights.
""")


st.divider()


# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.header("📌 Project Overview")

st.write("""
Agriculture is strongly affected by weather conditions, soil
characteristics, water availability and other environmental
factors.

SmartCropLoss analyzes these factors and provides:

- 🌾 Crop Recommendation
- 📉 Crop Loss Risk Analysis
- 🧠 Explainable AI using SHAP
- 💰 Profit / Loss Estimation
- 🌿 Fertilizer Recommendation
- 💧 Irrigation Recommendation
- 🌦 Real-Time Weather Information
- 🏛 Government Scheme Information
""")


st.divider()


# ==========================================================
# PROJECT OBJECTIVES
# ==========================================================

st.header("🎯 Project Objectives")

objectives = [
    "Recommend suitable crops using Machine Learning.",
    "Identify agricultural conditions associated with crop-loss risk.",
    "Explain model predictions using Explainable AI.",
    "Estimate possible farming profit or loss.",
    "Provide fertilizer recommendations based on soil nutrient values.",
    "Provide irrigation guidance using water and weather conditions.",
    "Display real-time weather information for a selected location.",
    "Help farmers discover relevant government agricultural schemes."
]

for objective in objectives:
    st.write(f"✅ {objective}")


st.divider()


# ==========================================================
# TECHNOLOGY STACK
# ==========================================================

st.header("💻 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Programming & Data")

    st.write("🐍 Python")

    st.write("🐼 Pandas")

    st.write("🔢 NumPy")

    st.write("📊 Matplotlib")

    st.write("📈 Plotly")


with col2:

    st.subheader("Machine Learning & Application")

    st.write("🌲 Scikit-learn")

    st.write("🌳 Random Forest")

    st.write("🧠 SHAP")

    st.write("🌐 Streamlit")

    st.write("🌦 OpenWeather API")

    st.write("💾 Joblib")


st.divider()


# ==========================================================
# MACHINE LEARNING
# ==========================================================

st.header("🤖 Machine Learning")

st.subheader("🌳 Random Forest Classifier")

st.write("""
The crop recommendation module uses a Random Forest Classifier.
Random Forest combines multiple decision trees and uses their
combined predictions to produce the final classification.

The model uses agricultural parameters such as:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

The predicted output is the recommended crop.
""")


st.divider()


# ==========================================================
# EXPLAINABLE AI
# ==========================================================

st.header("🧠 Explainable AI (XAI)")

st.subheader("SHAP")

st.write("""
SHAP (SHapley Additive exPlanations) is used to explain the
Machine Learning prediction.

Instead of showing only the predicted crop, the system can
show which input features contributed most strongly to the
prediction.

This helps make the model easier to understand and provides
greater transparency.
""")


st.divider()


# ==========================================================
# WEATHER INTEGRATION
# ==========================================================

st.header("🌦 Real-Time Weather Integration")

st.write("""
The application integrates the OpenWeather API to retrieve
current weather information for a selected district or city.

The weather module can provide:

- Temperature
- Feels-like temperature
- Humidity
- Rainfall
- Wind speed
- Cloud coverage
- Atmospheric pressure
- Weather condition
""")


st.info("""
The live weather data can support weather-risk analysis,
irrigation decisions and agricultural monitoring.
""")


st.divider()


# ==========================================================
# PROJECT MODULES
# ==========================================================

st.header("🧩 Project Modules")

modules = {
    "🌾 Smart Farm Analysis":
        "Combines farm, soil and weather information with crop recommendation and SHAP explanation.",

    "📉 Crop Loss":
        "Evaluates agricultural and environmental risk factors and estimates a potential crop-loss risk range.",

    "💰 Profit / Loss Estimation":
        "Calculates expected production, revenue, cultivation cost, estimated profit/loss, ROI and break-even values.",

    "🌿 Fertilizer Recommendation":
        "Analyzes nitrogen, phosphorus, potassium and soil pH values to identify possible nutrient deficiencies.",

    "💧 Irrigation Recommendation":
        "Uses soil moisture, groundwater, rainfall and weather conditions to provide irrigation guidance.",

    "🌦 Weather":
        "Displays current weather information retrieved through the OpenWeather API.",

    "🏛 Government Schemes":
        "Provides information and links to relevant agricultural government schemes and official portals."
}

for module_name, description in modules.items():

    with st.expander(module_name):

        st.write(description)


st.divider()


# ==========================================================
# SYSTEM WORKFLOW
# ==========================================================

st.header("🔄 System Workflow")

st.markdown("""
```text
Farmer / Farm Information
          ↓
Soil Parameters
          ↓
Weather Information
          ↓
Machine Learning Model
          ↓
Crop Recommendation
          ↓
Crop Risk Analysis
          ↓
SHAP Explanation
          ↓
Profit / Loss Estimation
          ↓
Fertilizer Recommendation
          ↓
Irrigation Recommendation
          ↓
Government Scheme Information""")