import streamlit as st
from weather import get_weather


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Irrigation Recommendation",
    page_icon="💧",
    layout="wide"
)


# ==========================================================
# TITLE
# ==========================================================

st.title("💧 Smart Irrigation Recommendation")

st.markdown("""
### 🌱 Intelligent Water Management

This module analyses crop, soil, groundwater and weather
conditions to provide a simple irrigation recommendation.

The system considers:
- Soil type
- Soil moisture
- Groundwater availability
- Rainfall
- Temperature
- Humidity
- Irrigation availability
- Live weather information
""")


st.divider()


# ==========================================================
# FARM INFORMATION
# ==========================================================

st.header("👨‍🌾 Farm Information")

col1, col2 = st.columns(2)

with col1:

    farmer_name = st.text_input(
        "Farmer Name",
        key="irrigation_farmer_name"
    )

    state = st.text_input(
        "State",
        key="irrigation_state"
    )

    district = st.text_input(
        "District",
        key="irrigation_district"
    )


with col2:

    crop = st.selectbox(
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
        key="irrigation_crop"
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
        ],
        key="irrigation_soil"
    )


st.divider()


# ==========================================================
# WATER INFORMATION
# ==========================================================

st.header("💧 Water Availability")

col1, col2, col3 = st.columns(3)

with col1:

    irrigation_available = st.selectbox(
        "Irrigation Available",
        [
            "Yes",
            "No"
        ],
        key="irrigation_available"
    )


with col2:

    groundwater = st.slider(
        "Groundwater Level (%)",
        0,
        100,
        60,
        key="irrigation_groundwater"
    )


with col3:

    soil_moisture = st.slider(
        "Current Soil Moisture (%)",
        0,
        100,
        50,
        key="irrigation_soil_moisture"
    )


st.divider()


# ==========================================================
# WEATHER INPUT
# ==========================================================

st.header("🌦 Weather Information")

use_live_weather = st.checkbox(
    "🌐 Use Real-Time Weather",
    value=True,
    key="irrigation_use_live_weather"
)


# ==========================================================
# LIVE WEATHER
# ==========================================================

if use_live_weather:

    weather_city = st.text_input(
        "Enter District / City Name",
        value="Hyderabad",
        key="irrigation_weather_city"
    )


    if st.button(
        "🌦 Get Live Weather",
        key="irrigation_weather_button"
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
                "irrigation_weather"
            ] = weather_result

            st.success(
                f"Weather data retrieved for "
                f"{weather_result['city']}, "
                f"{weather_result['country']}"
            )


    if "irrigation_weather" in st.session_state:

        weather_data = st.session_state[
            "irrigation_weather"
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
                f"{weather_data['humidity']}%"
            )

        with col3:

            st.metric(
                "🌧 Rainfall (1 Hour)",
                f"{weather_data['rainfall_1h']:.2f} mm"
            )


        temperature = weather_data["temperature"]

        humidity = weather_data["humidity"]

        rainfall = weather_data["rainfall_1h"]


    else:

        st.info(
            "Click 'Get Live Weather' to obtain weather data."
        )

        temperature = st.number_input(
            "Temperature (°C)",
            0.0,
            60.0,
            30.0,
            step=0.1,
            key="irrigation_temp_fallback"
        )

        humidity = st.number_input(
            "Humidity (%)",
            0.0,
            100.0,
            70.0,
            step=0.1,
            key="irrigation_humidity_fallback"
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            0.0,
            500.0,
            5.0,
            step=0.1,
            key="irrigation_rainfall_fallback"
        )


else:

    col1, col2, col3 = st.columns(3)

    with col1:

        temperature = st.number_input(
            "Temperature (°C)",
            0.0,
            60.0,
            30.0,
            step=0.1,
            key="irrigation_manual_temp"
        )


    with col2:

        humidity = st.number_input(
            "Humidity (%)",
            0.0,
            100.0,
            70.0,
            step=0.1,
            key="irrigation_manual_humidity"
        )


    with col3:

        rainfall = st.number_input(
            "Rainfall (mm)",
            0.0,
            500.0,
            5.0,
            step=0.1,
            key="irrigation_manual_rainfall"
        )


st.divider()


# ==========================================================
# IRRIGATION ANALYSIS
# ==========================================================

if st.button(
    "💧 Analyze Irrigation Requirement",
    key="irrigation_analyze_button"
):

    irrigation_score = 0

    reasons = []


    # ======================================================
    # SOIL MOISTURE
    # ======================================================

    if soil_moisture < 20:

        irrigation_score += 35

        reasons.append(
            "Soil moisture is very low."
        )

    elif soil_moisture < 40:

        irrigation_score += 20

        reasons.append(
            "Soil moisture is below the preferred range."
        )

    elif soil_moisture < 60:

        irrigation_score += 10

        reasons.append(
            "Soil moisture is moderately low."
        )


    # ======================================================
    # TEMPERATURE
    # ======================================================

    if temperature > 40:

        irrigation_score += 25

        reasons.append(
            "Very high temperature may increase water demand."
        )

    elif temperature > 35:

        irrigation_score += 15

        reasons.append(
            "High temperature may increase crop water demand."
        )


    # ======================================================
    # HUMIDITY
    # ======================================================

    if humidity < 30:

        irrigation_score += 15

        reasons.append(
            "Low humidity can increase moisture loss."
        )

    elif humidity > 90:

        irrigation_score -= 10

        reasons.append(
            "High humidity may reduce immediate irrigation demand."
        )


    # ======================================================
    # RAINFALL
    # ======================================================

    if rainfall < 2:

        irrigation_score += 25

        reasons.append(
            "Very low recent rainfall indicates limited natural water availability."
        )

    elif rainfall < 5:

        irrigation_score += 10

        reasons.append(
            "Recent rainfall is low."
        )

    elif rainfall > 30:

        irrigation_score -= 20

        reasons.append(
            "Recent rainfall may temporarily reduce irrigation requirement."
        )


    # ======================================================
    # GROUNDWATER
    # ======================================================

    if groundwater < 25:

        irrigation_score += 10

        reasons.append(
            "Groundwater availability is very low, so water must be used carefully."
        )

    elif groundwater < 40:

        irrigation_score += 5

        reasons.append(
            "Groundwater availability is relatively low."
        )


    # ======================================================
    # IRRIGATION AVAILABILITY
    # ======================================================

    if irrigation_available == "No":

        reasons.append(
            "No irrigation source is currently available."
        )


    # ======================================================
    # SOIL TYPE
    # ======================================================

    if soil_type == "Sandy":

        irrigation_score += 5

        reasons.append(
            "Sandy soil generally loses moisture faster."
        )

    elif soil_type == "Clay":

        if rainfall > 20:

            irrigation_score -= 5

            reasons.append(
                "Clay soil can retain water longer under adequate rainfall."
            )


    # ======================================================
    # LIMIT SCORE
    # ======================================================

    irrigation_score = max(
        0,
        min(irrigation_score, 100)
    )


    # ======================================================
    # IRRIGATION LEVEL
    # ======================================================

    if irrigation_available == "No":

        irrigation_level = "No Irrigation Source"

    elif irrigation_score < 25:

        irrigation_level = "Low Requirement"

    elif irrigation_score < 50:

        irrigation_level = "Moderate Requirement"

    elif irrigation_score < 75:

        irrigation_level = "High Requirement"

    else:

        irrigation_level = "Very High Requirement"


    # ======================================================
    # RECOMMENDED ACTION
    # ======================================================

    if irrigation_available == "No":

        recommendation = (
            "No irrigation source is available. "
            "Monitor soil moisture and consider water-conservation "
            "measures. Rainwater harvesting or other appropriate "
            "water-management options may be considered."
        )

    elif irrigation_score < 25:

        recommendation = (
            "Immediate irrigation may not be necessary. "
            "Continue monitoring soil moisture and weather conditions."
        )

    elif irrigation_score < 50:

        recommendation = (
            "Moderate irrigation may be required. "
            "Monitor soil moisture before the next irrigation cycle."
        )

    elif irrigation_score < 75:

        recommendation = (
            "Higher irrigation attention is required. "
            "Provide water according to crop stage and soil moisture."
        )

    else:

        recommendation = (
            "Very high irrigation requirement detected. "
            "Check soil moisture and ensure adequate water availability."
        )


    # ======================================================
    # DISPLAY RESULT
    # ======================================================

    st.divider()

    st.subheader(
        "📊 Irrigation Analysis Result"
    )


    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Irrigation Score",
            f"{irrigation_score}/100"
        )


    with col2:

        st.metric(
            "Requirement",
            irrigation_level
        )


    with col3:

        st.metric(
            "Soil Moisture",
            f"{soil_moisture}%"
        )


    # ======================================================
    # RECOMMENDATION
    # ======================================================

    st.subheader(
        "💧 Irrigation Recommendation"
    )

    if irrigation_score < 25:

        st.success(
            recommendation
        )

    elif irrigation_score < 50:

        st.info(
            recommendation
        )

    elif irrigation_score < 75:

        st.warning(
            recommendation
        )

    else:

        st.error(
            recommendation
        )


    # ======================================================
    # FACTOR EXPLANATION
    # ======================================================

    st.subheader(
        "🧠 Factors Affecting Irrigation Requirement"
    )


    if reasons:

        for reason in reasons:

            st.write(
                f"🔸 {reason}"
            )

    else:

        st.write(
            "No major irrigation-risk factors were detected."
        )


    # ======================================================
    # INPUT SUMMARY
    # ======================================================

    st.subheader(
        "📋 Current Farm Conditions"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Crop:** {crop}"
        )

        st.write(
            f"**Soil Type:** {soil_type}"
        )

        st.write(
            f"**Soil Moisture:** {soil_moisture}%"
        )

        st.write(
            f"**Groundwater:** {groundwater}%"
        )


    with col2:

        st.write(
            f"**Temperature:** {temperature:.2f} °C"
        )

        st.write(
            f"**Humidity:** {humidity:.2f}%"
        )

        st.write(
            f"**Rainfall:** {rainfall:.2f} mm"
        )

        st.write(
            f"**Irrigation Available:** {irrigation_available}"
        )


    # ======================================================
    # WATER-SAVING RECOMMENDATIONS
    # ======================================================

    st.subheader(
        "🌱 Water-Saving Recommendations"
    )


    st.write(
        "💧 Monitor soil moisture before irrigation instead of "
        "watering on a fixed schedule."
    )

    st.write(
        "💧 Avoid unnecessary irrigation immediately after "
        "significant rainfall."
    )

    st.write(
        "💧 Consider efficient irrigation systems such as drip "
        "or sprinkler irrigation where suitable."
    )

    st.write(
        "💧 Maintain soil moisture using appropriate mulching "
        "and soil-management practices."
    )

    st.write(
        "💧 Conserve groundwater, especially when groundwater "
        "availability is low."
    )


    # ======================================================
    # FINAL STATUS
    # ======================================================

    if irrigation_available == "No":

        st.error(
            "⚠️ Irrigation source unavailable."
        )

    elif irrigation_score >= 75:

        st.error(
            "🚨 Very high irrigation requirement detected."
        )

    elif irrigation_score >= 50:

        st.warning(
            "⚠️ High irrigation attention required."
        )

    elif irrigation_score >= 25:

        st.info(
            "ℹ️ Moderate irrigation requirement detected."
        )

    else:

        st.success(
            "✅ Current conditions indicate low immediate irrigation requirement."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "💧 Smart Irrigation Recommendation | "
    "Recommendations are estimates based on the entered "
    "farm and weather conditions. Actual irrigation scheduling "
    "should consider crop stage, soil testing, local conditions "
    "and agricultural guidance."
)