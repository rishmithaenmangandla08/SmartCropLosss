import streamlit as st
import pandas as pd
import joblib
import shap

from weather_api import get_weather


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Smart Farm Analysis",
    page_icon="🌾",
    layout="wide"
)


# ==========================================================
# LOAD MODEL
# ==========================================================

crop_model = joblib.load("models/crop_model.pkl")


# ==========================================================
# INITIAL VALUES
# ==========================================================

risk_score = 0
risk = "Not Calculated"


# ==========================================================
# MAIN TITLE
# ==========================================================

st.title(
    "🌾 Smart Crop Loss Prediction and Explainable Risk Analysis"
)

st.markdown("""
### 🌱 Empowering Farmers with AI

This platform provides:

- 🌾 Crop Recommendation
- 📉 Crop Risk Prediction
- 🧠 Explainable AI
- 💰 Profit / Loss Estimation
- 🌦 Real-Time Weather Analysis
- 💧 Smart Farming Recommendations
- 🏛 Government Decision Support

Enter farm details and click **Analyze Farm**.
""")


# ==========================================================
# FARMER INFORMATION
# ==========================================================

st.header("👨‍🌾 Farmer Information")

col1, col2 = st.columns(2)

with col1:

    farmer_name = st.text_input(
        "Farmer Name"
    )

    state = st.text_input(
        "State"
    )


with col2:

    district = st.text_input(
        "District"
    )

    season = st.selectbox(
        "Season",
        [
            "Kharif",
            "Rabi",
            "Zaid"
        ]
    )


st.divider()


# ==========================================================
# FARM INFORMATION
# ==========================================================

st.header("🌱 Farm Information")

col1, col2 = st.columns(2)

with col1:

    cultivation_area = st.number_input(
        "Cultivation Area (Acres)",
        min_value=0.5,
        value=1.0,
        step=0.5
    )

    soil_type = st.selectbox(
        "Soil Type",
        [
            "Black",
            "Red",
            "Alluvial",
            "Laterite",
            "Clay",
            "Sandy"
        ]
    )


with col2:

    irrigation = st.selectbox(
        "Irrigation Available",
        [
            "Yes",
            "No"
        ]
    )

    groundwater = st.slider(
        "Groundwater Level (%)",
        0,
        100,
        60
    )


st.divider()


# ==========================================================
# PROFIT / LOSS INPUTS
# ==========================================================

st.header("💰 Profit / Loss Inputs")

st.info(
    "Enter expected yield, selling price and cultivation cost "
    "to estimate the possible profit or loss."
)

col1, col2, col3 = st.columns(3)

with col1:

    expected_yield = st.number_input(
        "Expected Yield (kg/acre)",
        min_value=0.0,
        value=2000.0,
        step=100.0
    )


with col2:

    market_price = st.number_input(
        "Expected Selling Price (₹/kg)",
        min_value=0.0,
        value=25.0,
        step=1.0
    )


with col3:

    cultivation_cost = st.number_input(
        "Cultivation Cost (₹/acre)",
        min_value=0.0,
        value=30000.0,
        step=1000.0
    )


st.divider()


# ==========================================================
# SOIL PARAMETERS
# ==========================================================

st.header("🧪 Soil Parameters")

col1, col2 = st.columns(2)

with col1:

    nitrogen = st.number_input(
        "Nitrogen (N)",
        0,
        150,
        90
    )

    phosphorus = st.number_input(
        "Phosphorus (P)",
        0,
        150,
        42
    )


with col2:

    potassium = st.number_input(
        "Potassium (K)",
        0,
        250,
        43
    )

    ph = st.number_input(
        "Soil pH",
        0.0,
        14.0,
        6.5,
        step=0.1
    )


st.divider()


# ==========================================================
# WEATHER PARAMETERS
# ==========================================================

st.header("🌦 Weather Parameters")

col1, col2 = st.columns(2)

with col1:

    temperature = st.number_input(
        "Temperature (°C)",
        0.0,
        60.0,
        20.8,
        step=0.1
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        0.0,
        500.0,
        202.0,
        step=0.1
    )


with col2:

    humidity = st.number_input(
        "Humidity (%)",
        0.0,
        100.0,
        82.0,
        step=0.1
    )


# ==========================================================
# ANALYZE FARM BUTTON
# ==========================================================

if st.button(
    "🔍 Analyze Farm",
    key="analyze_farm_button"
):

    # ------------------------------------------------------
    # PREPARE MODEL INPUT
    # ------------------------------------------------------

    input_data = pd.DataFrame({
        "N": [nitrogen],
        "P": [phosphorus],
        "K": [potassium],
        "temperature": [temperature],
        "humidity": [humidity],
        "ph": [ph],
        "rainfall": [rainfall]
    })


    # ------------------------------------------------------
    # CROP PREDICTION
    # ------------------------------------------------------

    prediction = crop_model.predict(
        input_data
    )

    recommended_crop = str(
        prediction[0]
    )


    st.success(
        f"🌾 Recommended Crop: {recommended_crop.title()}"
    )


    # ======================================================
    # PROFIT / LOSS ESTIMATION
    # ======================================================

    st.subheader(
        "💰 Profit / Loss Estimation"
    )

    # Total expected production
    total_yield = (
        cultivation_area *
        expected_yield
    )

    # Total expected revenue
    total_revenue = (
        total_yield *
        market_price
    )

    # Total cultivation cost
    total_cost = (
        cultivation_area *
        cultivation_cost
    )

    # Profit or loss
    estimated_profit = (
        total_revenue -
        total_cost
    )


    # ------------------------------------------------------
    # BREAK-EVEN CALCULATION
    # ------------------------------------------------------

    if market_price > 0:

        break_even_yield = (
            total_cost /
            market_price
        )

    else:

        break_even_yield = 0


    # ------------------------------------------------------
    # DISPLAY PROFIT INFORMATION
    # ------------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🌾 Expected Production",
            f"{total_yield:,.2f} kg"
        )


    with col2:

        st.metric(
            "💵 Expected Revenue",
            f"₹{total_revenue:,.2f}"
        )


    with col3:

        st.metric(
            "💸 Total Cost",
            f"₹{total_cost:,.2f}"
        )


    st.divider()


    # ------------------------------------------------------
    # PROFIT / LOSS RESULT
    # ------------------------------------------------------

    if estimated_profit > 0:

        st.success(
            f"✅ Estimated Profit: "
            f"₹{estimated_profit:,.2f}"
        )

    elif estimated_profit < 0:

        st.error(
            f"⚠️ Estimated Loss: "
            f"₹{abs(estimated_profit):,.2f}"
        )

    else:

        st.warning(
            "⚖️ Estimated Result: Break-even"
        )


    # ------------------------------------------------------
    # BREAK-EVEN INFORMATION
    # ------------------------------------------------------

    st.info(
        f"📊 Break-even Production: "
        f"{break_even_yield:,.2f} kg"
    )


    # ------------------------------------------------------
    # PROFIT CALCULATION DETAILS
    # ------------------------------------------------------

    st.write(
        "### 📊 Profit / Loss Calculation"
    )


    st.write(
        f"**Production:** "
        f"{cultivation_area:.2f} acres × "
        f"{expected_yield:,.2f} kg/acre = "
        f"{total_yield:,.2f} kg"
    )


    st.write(
        f"**Revenue:** "
        f"{total_yield:,.2f} kg × "
        f"₹{market_price:,.2f}/kg = "
        f"₹{total_revenue:,.2f}"
    )


    st.write(
        f"**Cost:** "
        f"{cultivation_area:.2f} acres × "
        f"₹{cultivation_cost:,.2f}/acre = "
        f"₹{total_cost:,.2f}"
    )


    st.write(
        f"**Profit / Loss:** "
        f"₹{total_revenue:,.2f} − "
        f"₹{total_cost:,.2f} = "
        f"₹{estimated_profit:,.2f}"
    )


    st.divider()


    # ======================================================
    # SHAP EXPLAINABLE AI
    # ======================================================

    st.subheader(
        "🧠 Explainable AI (SHAP)"
    )

    try:

        explainer = shap.TreeExplainer(
            crop_model
        )

        shap_explanation = explainer(
            input_data
        )

        shap_values = shap_explanation.values


        # --------------------------------------------------
        # HANDLE MULTI-CLASS SHAP OUTPUT
        # --------------------------------------------------

        if len(shap_values.shape) == 3:

            predicted_class_index = list(
                crop_model.classes_
            ).index(
                prediction[0]
            )

            values = shap_values[
                0,
                :,
                predicted_class_index
            ]

        else:

            values = shap_values[0]


        # --------------------------------------------------
        # CREATE SHAP DATAFRAME
        # --------------------------------------------------

        shap_df = pd.DataFrame({
            "Feature": input_data.columns,
            "SHAP Value": values
        })


        shap_df["Impact"] = (
            shap_df["SHAP Value"]
            .abs()
        )


        shap_df = shap_df.sort_values(
            by="Impact",
            ascending=False
        )


        # --------------------------------------------------
        # SHAP VISUALIZATION
        # --------------------------------------------------

        st.bar_chart(
            shap_df.set_index(
                "Feature"
            )["Impact"]
        )


        st.dataframe(
            shap_df,
            use_container_width=True
        )


        st.success(
            "✅ SHAP Explanation Generated Successfully"
        )


    except Exception as e:

        st.error(
            f"SHAP Error: {e}"
        )


# ==========================================================
# REAL-TIME WEATHER INFORMATION
# ==========================================================

st.divider()

st.subheader(
    "🌦️ Real-Time Weather Information"
)


city = st.text_input(
    "Enter District/City Name",
    "Hyderabad",
    key="smartfarm_weather_city"
)


if st.button(
    "Get Weather Data",
    key="smartfarm_weather_button"
):

    weather_data = get_weather(
        city
    )


    # ------------------------------------------------------
    # WEATHER ERROR
    # ------------------------------------------------------

    if "error" in weather_data:

        st.error(
            weather_data["error"]
        )


    else:

        # --------------------------------------------------
        # SUCCESS MESSAGE
        # --------------------------------------------------

        st.success(
            f"Weather Data Retrieved Successfully for "
            f"{weather_data['city']}, "
            f"{weather_data['country']}"
        )


        # --------------------------------------------------
        # WEATHER METRICS
        # --------------------------------------------------

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "🌡 Temperature",
                f"{weather_data['temperature']:.2f} °C"
            )


        with col2:

            st.metric(
                "💧 Humidity",
                f"{weather_data['humidity']}%"
            )


        with col3:

            st.metric(
                "🌧 Rainfall (1 Hour)",
                f"{weather_data['rainfall_1h']:.2f} mm"
            )


        col4, col5, col6 = st.columns(3)


        with col4:

            st.metric(
                "🌡 Feels Like",
                f"{weather_data['feels_like']:.2f} °C"
            )


        with col5:

            st.metric(
                "💨 Wind Speed",
                f"{weather_data['wind_speed']} m/s"
            )


        with col6:

            st.metric(
                "☁ Cloud Coverage",
                f"{weather_data['clouds']}%"
            )


        st.write(
            f"**Weather Condition:** "
            f"{weather_data['description'].title()}"
        )


        st.write(
            f"**Atmospheric Pressure:** "
            f"{weather_data['pressure']} hPa"
        )


        # ==================================================
        # WEATHER RISK ANALYSIS
        # ==================================================

        st.subheader(
            "⚠️ Weather Risk Analysis"
        )


        weather_risk_score = 0


        # High temperature
        if weather_data["temperature"] > 35:

            weather_risk_score += 30


        # Low humidity
        if weather_data["humidity"] < 30:

            weather_risk_score += 20


        # Low rainfall
        if weather_data["rainfall_1h"] < 5:

            weather_risk_score += 30


        # Very high rainfall
        if weather_data["rainfall_1h"] > 50:

            weather_risk_score += 30


        # Low groundwater
        if groundwater < 30:

            weather_risk_score += 20


        # No irrigation
        if irrigation == "No":

            weather_risk_score += 20


        # Maximum score
        weather_risk_score = min(
            weather_risk_score,
            100
        )


        # --------------------------------------------------
        # RISK LEVEL
        # --------------------------------------------------

        if weather_risk_score < 30:

            weather_risk = "Low Risk"

        elif weather_risk_score < 60:

            weather_risk = "Medium Risk"

        else:

            weather_risk = "High Risk"


        st.info(
            f"Risk Level: {weather_risk}"
        )


        st.write(
            f"Risk Score: "
            f"{weather_risk_score}/100"
        )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.success("""
🌱 Empowering Farmers with AI-Based Crop Recommendation,
Crop Loss Prediction, Explainable Risk Analysis,
Profit / Loss Estimation and Smart Farming Decisions.
""")
