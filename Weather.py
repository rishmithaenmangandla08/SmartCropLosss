import streamlit as st
from weather import get_weather


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Real-Time Weather",
    page_icon="🌦️",
    layout="wide"
)


# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("🌦️ Real-Time Weather Information")

st.markdown("""
### 🌍 Live Weather Monitoring

Enter a district or city name to retrieve current weather
information using the OpenWeather API.

The system displays:

- 🌡 Temperature
- 💧 Humidity
- 🌧 Rainfall
- 🌡 Feels Like Temperature
- 💨 Wind Speed
- ☁ Cloud Coverage
- 🧭 Atmospheric Pressure
- 🌦 Weather Condition
""")

st.divider()


# ==========================================================
# LOCATION INPUT
# ==========================================================

st.header("📍 Location")

city = st.text_input(
    "Enter District / City Name",
    value="Hyderabad",
    key="weather_page_city"
)


# ==========================================================
# GET WEATHER BUTTON
# ==========================================================

if st.button(
    "🌦️ Get Weather Data",
    key="weather_page_button"
):

    if not city.strip():

        st.warning(
            "Please enter a district or city name."
        )

    else:

        weather_data = get_weather(
            city
        )

        # --------------------------------------------------
        # ERROR HANDLING
        # --------------------------------------------------

        if "error" in weather_data:

            st.error(
                weather_data["error"]
            )

        else:

            # --------------------------------------------------
            # SUCCESS MESSAGE
            # --------------------------------------------------

            st.success(
                f"Weather data retrieved successfully for "
                f"{weather_data['city']}, "
                f"{weather_data['country']}"
            )


            st.divider()


            # ==================================================
            # WEATHER METRICS - ROW 1
            # ==================================================

            st.subheader("🌤️ Current Weather")

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


            # ==================================================
            # WEATHER METRICS - ROW 2
            # ==================================================

            col4, col5, col6 = st.columns(3)


            with col4:

                st.metric(
                    "🌡 Feels Like",
                    f"{weather_data['feels_like']:.2f} °C"
                )


            with col5:

                st.metric(
                    "💨 Wind Speed",
                    f"{weather_data['wind_speed']:.2f} m/s"
                )


            with col6:

                st.metric(
                    "☁ Cloud Coverage",
                    f"{weather_data['clouds']}%"
                )


            st.divider()


            # ==================================================
            # ADDITIONAL WEATHER DETAILS
            # ==================================================

            st.subheader("📋 Weather Details")

            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    f"**📍 Location:** "
                    f"{weather_data['city']}, "
                    f"{weather_data['country']}"
                )

                st.write(
                    f"**🌦 Condition:** "
                    f"{weather_data['condition']}"
                )

                st.write(
                    f"**📝 Description:** "
                    f"{weather_data['description'].title()}"
                )


            with col2:

                st.write(
                    f"**🧭 Pressure:** "
                    f"{weather_data['pressure']} hPa"
                )

                st.write(
                    f"**🌧 Rainfall (3 Hours):** "
                    f"{weather_data['rainfall_3h']:.2f} mm"
                )

                st.write(
                    f"**☁ Cloud Coverage:** "
                    f"{weather_data['clouds']}%"
                )


            st.divider()


            # ==================================================
            # SIMPLE WEATHER RISK ANALYSIS
            # ==================================================

            st.subheader("⚠️ Weather Risk Analysis")

            weather_risk_score = 0

            risk_reasons = []


            # --------------------------------------------------
            # HIGH TEMPERATURE
            # --------------------------------------------------

            if weather_data["temperature"] > 40:

                weather_risk_score += 30

                risk_reasons.append(
                    "Very high temperature may cause heat stress."
                )

            elif weather_data["temperature"] > 35:

                weather_risk_score += 15

                risk_reasons.append(
                    "High temperature may increase crop water demand."
                )


            # --------------------------------------------------
            # LOW HUMIDITY
            # --------------------------------------------------

            if weather_data["humidity"] < 30:

                weather_risk_score += 20

                risk_reasons.append(
                    "Low humidity may increase moisture loss."
                )


            # --------------------------------------------------
            # HIGH HUMIDITY
            # --------------------------------------------------

            elif weather_data["humidity"] > 90:

                weather_risk_score += 15

                risk_reasons.append(
                    "Very high humidity may increase disease risk."
                )


            # --------------------------------------------------
            # LOW RAINFALL
            # --------------------------------------------------

            if weather_data["rainfall_1h"] < 2:

                weather_risk_score += 20

                risk_reasons.append(
                    "Very low recent rainfall may increase water stress."
                )


            # --------------------------------------------------
            # HEAVY RAINFALL
            # --------------------------------------------------

            elif weather_data["rainfall_1h"] > 50:

                weather_risk_score += 30

                risk_reasons.append(
                    "Heavy rainfall may increase waterlogging or flood risk."
                )


            # --------------------------------------------------
            # LIMIT SCORE
            # --------------------------------------------------

            weather_risk_score = min(
                weather_risk_score,
                100
            )


            # ==================================================
            # RISK LEVEL
            # ==================================================

            if weather_risk_score < 30:

                risk_level = "Low Risk"

            elif weather_risk_score < 60:

                risk_level = "Medium Risk"

            elif weather_risk_score < 80:

                risk_level = "High Risk"

            else:

                risk_level = "Critical Risk"


            # ==================================================
            # DISPLAY RISK
            # ==================================================

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Weather Risk Score",
                    f"{weather_risk_score}/100"
                )


            with col2:

                st.metric(
                    "Weather Risk Level",
                    risk_level
                )


            if risk_level == "Low Risk":

                st.success(
                    "✅ Current weather conditions indicate relatively low agricultural weather risk."
                )

            elif risk_level == "Medium Risk":

                st.warning(
                    "⚠️ Current weather conditions indicate moderate agricultural weather risk."
                )

            elif risk_level == "High Risk":

                st.error(
                    "🚨 Current weather conditions indicate high agricultural weather risk."
                )

            else:

                st.error(
                    "🚨 Critical weather conditions detected."
                )


            # ==================================================
            # RISK FACTORS
            # ==================================================

            st.subheader(
                "🧠 Weather Risk Factors"
            )

            if risk_reasons:

                for reason in risk_reasons:

                    st.write(
                        f"🔸 {reason}"
                    )

            else:

                st.write(
                    "✅ No major weather-risk factors were detected."
                )


            # ==================================================
            # FARMER RECOMMENDATIONS
            # ==================================================

            st.subheader(
                "🌱 Weather-Based Farming Suggestions"
            )


            if weather_data["temperature"] > 35:

                st.write(
                    "💧 Monitor soil moisture and provide appropriate irrigation."
                )


            if weather_data["humidity"] > 90:

                st.write(
                    "🍃 Closely monitor the crop for moisture-related diseases."
                )


            if weather_data["rainfall_1h"] < 2:

                st.write(
                    "💧 Monitor water availability because recent rainfall is low."
                )


            if weather_data["rainfall_1h"] > 50:

                st.write(
                    "🌧 Check drainage and monitor fields for excessive water accumulation."
                )


            if (
                weather_data["temperature"] <= 35
                and weather_data["humidity"] <= 90
                and weather_data["rainfall_1h"] <= 50
            ):

                st.write(
                    "✅ Continue monitoring local weather and soil conditions."
                )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🌦️ Real-Time Weather Module | "
    "Weather information is retrieved from the OpenWeather API."
)