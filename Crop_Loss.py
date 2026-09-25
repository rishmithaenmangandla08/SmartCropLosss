import streamlit as st
from weather import get_weather


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Crop Loss Risk Analysis",
    page_icon="📉",
    layout="wide"
)


# ==========================================================
# TITLE
# ==========================================================

st.title("📉 Crop Loss Prediction and Risk Analysis")

st.markdown("""
### 🌾 Smart Crop Loss Risk Assessment

This module evaluates agricultural conditions and estimates
the potential crop-loss risk using soil, weather, irrigation
and groundwater-related factors.

**Note:** The loss percentage shown here is a risk-based estimate,
not a guaranteed financial or agricultural outcome.
""")


st.divider()


# ==========================================================
# FARM DETAILS
# ==========================================================

st.header("👨‍🌾 Farm Details")

col1, col2 = st.columns(2)

with col1:

    farmer_name = st.text_input(
        "Farmer Name",
        key="loss_farmer_name"
    )

    state = st.text_input(
        "State",
        key="loss_state"
    )

with col2:

    district = st.text_input(
        "District",
        key="loss_district"
    )

    crop_name = st.selectbox(
        "Crop",
        [
            "Rice",
            "Wheat",
            "Maize",
            "Cotton",
            "Sugarcane",
            "Groundnut",
            "Pulses",
            "Tomato",
            "Potato",
            "Other"
        ],
        key="loss_crop"
    )


st.divider()


# ==========================================================
# FARM CONDITIONS
# ==========================================================

st.header("🌱 Farm Conditions")

col1, col2 = st.columns(2)

with col1:

    soil_type = st.selectbox(
        "Soil Type",
        [
            "Black",
            "Red",
            "Alluvial",
            "Laterite",
            "Clay",
            "Sandy"
        ],
        key="loss_soil"
    )

    soil_ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1,
        key="loss_ph"
    )

with col2:

    irrigation = st.selectbox(
        "Irrigation Available",
        [
            "Yes",
            "No"
        ],
        key="loss_irrigation"
    )

    groundwater = st.slider(
        "Groundwater Level (%)",
        min_value=0,
        max_value=100,
        value=60,
        key="loss_groundwater"
    )


st.divider()


# ==========================================================
# WEATHER SECTION
# ==========================================================

st.header("🌦 Weather Conditions")

st.write(
    "You can either enter weather values manually or use "
    "real-time weather data from OpenWeather."
)


use_live_weather = st.checkbox(
    "🌐 Use Real-Time Weather",
    value=True,
    key="loss_use_live_weather"
)


# ==========================================================
# REAL-TIME WEATHER
# ==========================================================

if use_live_weather:

    weather_city = st.text_input(
        "Enter District / City Name",
        value="Hyderabad",
        key="loss_weather_city"
    )

    if st.button(
        "🌦 Get Live Weather",
        key="loss_weather_button"
    ):

        weather_result = get_weather(
            weather_city
        )

        if "error" in weather_result:

            st.error(
                weather_result["error"]
            )

        else:

            st.session_state[
                "crop_loss_weather"
            ] = weather_result

            st.success(
                f"Weather data retrieved successfully for "
                f"{weather_result['city']}, "
                f"{weather_result['country']}"
            )


    # ------------------------------------------------------
    # DISPLAY SAVED WEATHER
    # ------------------------------------------------------

    if "crop_loss_weather" in st.session_state:

        weather_data = st.session_state[
            "crop_loss_weather"
        ]

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🌡 Temperature",
                f"{weather_data['temperature']:.2f} °C"
            )

        with col2:

            st.metric(
                "💧 Humidity",
                f"{weather_data['humidity']} %"
            )

        with col3:

            st.metric(
                "🌧 Rainfall (1 Hour)",
                f"{weather_data['rainfall_1h']:.2f} mm"
            )

        st.write(
            f"**Weather Condition:** "
            f"{weather_data['description'].title()}"
        )


        temperature = weather_data["temperature"]

        humidity = weather_data["humidity"]

        rainfall = weather_data["rainfall_1h"]

    else:

        st.info(
            "Click 'Get Live Weather' to obtain current weather data."
        )

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            max_value=60.0,
            value=30.0,
            step=0.1,
            key="loss_live_temp_fallback"
        )

        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=0.1,
            key="loss_live_humidity_fallback"
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=500.0,
            value=5.0,
            step=0.1,
            key="loss_live_rainfall_fallback"
        )


else:

    col1, col2, col3 = st.columns(3)

    with col1:

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            max_value=60.0,
            value=30.0,
            step=0.1,
            key="loss_manual_temp"
        )

    with col2:

        humidity = st.number_input(
            "Humidity (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=0.1,
            key="loss_manual_humidity"
        )

    with col3:

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=0.0,
            max_value=500.0,
            value=5.0,
            step=0.1,
            key="loss_manual_rainfall"
        )


st.divider()


# ==========================================================
# ANALYZE BUTTON
# ==========================================================

if st.button(
    "🔍 Analyze Crop Loss Risk",
    key="crop_loss_analyze_button"
):

    # ======================================================
    # INITIAL RISK SCORE
    # ======================================================

    risk_score = 0

    risk_reasons = []


    # ======================================================
    # TEMPERATURE ANALYSIS
    # ======================================================

    if temperature > 40:

        risk_score += 25

        risk_reasons.append(
            "Very high temperature can increase crop stress."
        )

    elif temperature > 35:

        risk_score += 15

        risk_reasons.append(
            "High temperature may cause heat stress."
        )

    elif temperature < 10:

        risk_score += 20

        risk_reasons.append(
            "Very low temperature may affect crop growth."
        )


    # ======================================================
    # HUMIDITY ANALYSIS
    # ======================================================

    if humidity > 90:

        risk_score += 20

        risk_reasons.append(
            "Very high humidity can increase disease risk."
        )

    elif humidity < 30:

        risk_score += 20

        risk_reasons.append(
            "Low humidity may increase moisture stress."
        )


    # ======================================================
    # RAINFALL ANALYSIS
    # ======================================================

    if rainfall < 2:

        risk_score += 20

        risk_reasons.append(
            "Very low rainfall may create water stress."
        )

    elif rainfall > 50:

        risk_score += 25

        risk_reasons.append(
            "Very high rainfall may increase waterlogging or flood risk."
        )


    # ======================================================
    # GROUNDWATER ANALYSIS
    # ======================================================

    if groundwater < 25:

        risk_score += 20

        risk_reasons.append(
            "Very low groundwater availability increases irrigation risk."
        )

    elif groundwater < 40:

        risk_score += 10

        risk_reasons.append(
            "Low groundwater availability may cause water stress."
        )


    # ======================================================
    # IRRIGATION ANALYSIS
    # ======================================================

    if irrigation == "No":

        risk_score += 15

        risk_reasons.append(
            "No irrigation availability can increase crop water risk."
        )


    # ======================================================
    # SOIL pH ANALYSIS
    # ======================================================

    if soil_ph < 5.5:

        risk_score += 15

        risk_reasons.append(
            "Highly acidic soil may reduce crop nutrient availability."
        )

    elif soil_ph > 8.5:

        risk_score += 15

        risk_reasons.append(
            "Highly alkaline soil may affect nutrient availability."
        )


    # ======================================================
    # SOIL TYPE FACTOR
    # ======================================================

    if soil_type == "Sandy":

        if rainfall < 5 and irrigation == "No":

            risk_score += 10

            risk_reasons.append(
                "Sandy soil can lose moisture quickly under dry conditions."
            )


    elif soil_type == "Clay":

        if rainfall > 50:

            risk_score += 10

            risk_reasons.append(
                "Clay soil may have drainage problems during heavy rainfall."
            )


    # ======================================================
    # LIMIT SCORE TO 100
    # ======================================================

    risk_score = min(
        risk_score,
        100
    )


    # ======================================================
    # RISK LEVEL
    # ======================================================

    if risk_score < 30:

        risk_level = "Low Risk"

    elif risk_score < 60:

        risk_level = "Medium Risk"

    elif risk_score < 80:

        risk_level = "High Risk"

    else:

        risk_level = "Critical Risk"


    # ======================================================
    # ESTIMATED LOSS RANGE
    # ======================================================

    if risk_score < 30:

        loss_range = "0% - 10%"

    elif risk_score < 60:

        loss_range = "10% - 30%"

    elif risk_score < 80:

        loss_range = "30% - 60%"

    else:

        loss_range = "60% - 100%"


    # ======================================================
    # RESULT
    # ======================================================

    st.divider()

    st.subheader(
        "📊 Crop Loss Risk Result"
    )


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with col2:

        st.metric(
            "Risk Level",
            risk_level
        )

    with col3:

        st.metric(
            "Estimated Loss Range",
            loss_range
        )


    # ======================================================
    # RISK MESSAGE
    # ======================================================

    if risk_level == "Low Risk":

        st.success(
            "✅ Current conditions indicate relatively low crop-loss risk."
        )

    elif risk_level == "Medium Risk":

        st.warning(
            "⚠️ Current conditions indicate moderate crop-loss risk."
        )

    elif risk_level == "High Risk":

        st.error(
            "🚨 Current conditions indicate high crop-loss risk."
        )

    else:

        st.error(
            "🚨 Critical conditions detected. Immediate farm-risk assessment is recommended."
        )


    # ======================================================
    # RISK BREAKDOWN
    # ======================================================

    st.subheader(
        "🧠 Risk Factor Explanation"
    )

    if risk_reasons:

        for reason in risk_reasons:

            st.write(
                f"🔸 {reason}"
            )

    else:

        st.write(
            "✅ No major risk factors were triggered by the entered conditions."
        )


    # ======================================================
    # INPUT SUMMARY
    # ======================================================

    st.subheader(
        "📋 Analysis Summary"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Crop:** {crop_name}"
        )

        st.write(
            f"**Soil Type:** {soil_type}"
        )

        st.write(
            f"**Soil pH:** {soil_ph:.1f}"
        )

        st.write(
            f"**Irrigation:** {irrigation}"
        )


    with col2:

        st.write(
            f"**Temperature:** {temperature:.2f} °C"
        )

        st.write(
            f"**Humidity:** {humidity:.2f} %"
        )

        st.write(
            f"**Rainfall:** {rainfall:.2f} mm"
        )

        st.write(
            f"**Groundwater:** {groundwater}%"
        )


    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    st.subheader(
        "💡 Risk Reduction Recommendations"
    )

    if temperature > 35:

        st.write(
            "🌡 Consider suitable irrigation and heat-management practices."
        )

    if rainfall < 2:

        st.write(
            "💧 Monitor soil moisture and ensure adequate irrigation."
        )

    if rainfall > 50:

        st.write(
            "🌧 Ensure proper drainage and monitor waterlogging."
        )

    if humidity > 90:

        st.write(
            "🍃 Monitor the crop for possible moisture-related diseases."
        )

    if groundwater < 40:

        st.write(
            "💧 Conserve available groundwater and plan irrigation carefully."
        )

    if irrigation == "No":

        st.write(
            "🚿 Consider suitable water-management measures during dry periods."
        )

    if soil_ph < 5.5:

        st.write(
            "🧪 Soil testing and appropriate soil amendments may be required."
        )

    elif soil_ph > 8.5:

        st.write(
            "🧪 Soil testing and appropriate soil-management practices may be required."
        )

    if risk_score < 30:

        st.write(
            "✅ Continue monitoring weather, soil and water conditions."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.info(
    "📌 This page provides a risk-based estimate using the entered "
    "agricultural and weather conditions. It is intended as a "
    "decision-support tool, not a guarantee of actual crop loss."
)