import streamlit as st


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Fertilizer Recommendation",
    page_icon="🌿",
    layout="wide"
)


# ==========================================================
# TITLE
# ==========================================================

st.title("🌿 Fertilizer Recommendation")

st.markdown("""
### 🌱 Smart Fertilizer Advisory

This module evaluates soil nutrient values (N, P and K)
along with soil pH and crop information to provide a
basic fertilizer recommendation.

**Note:** Recommendations are intended for academic decision
support. Actual fertilizer quantity should be decided using
a soil test and local agricultural guidance.
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
        key="fertilizer_farmer_name"
    )

    state = st.text_input(
        "State",
        key="fertilizer_state"
    )


with col2:

    district = st.text_input(
        "District",
        key="fertilizer_district"
    )

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
        key="fertilizer_crop"
    )


st.divider()


# ==========================================================
# SOIL PARAMETERS
# ==========================================================

st.header("🧪 Soil Nutrient Information")

col1, col2, col3 = st.columns(3)

with col1:

    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=200.0,
        value=90.0,
        step=1.0,
        key="fertilizer_n"
    )


with col2:

    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=200.0,
        value=42.0,
        step=1.0,
        key="fertilizer_p"
    )


with col3:

    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=300.0,
        value=43.0,
        step=1.0,
        key="fertilizer_k"
    )


soil_ph = st.number_input(
    "Soil pH",
    min_value=0.0,
    max_value=14.0,
    value=6.5,
    step=0.1,
    key="fertilizer_ph"
)


st.divider()


# ==========================================================
# ANALYSIS BUTTON
# ==========================================================

if st.button(
    "🌿 Analyze Soil & Recommend Fertilizer",
    key="fertilizer_analyze_button"
):

    # ======================================================
    # NITROGEN STATUS
    # ======================================================

    if nitrogen < 50:

        nitrogen_status = "Low"

        nitrogen_recommendation = (
            "Use a nitrogen source such as urea or an appropriate "
            "organic nitrogen source."
        )

    elif nitrogen < 100:

        nitrogen_status = "Medium"

        nitrogen_recommendation = (
            "Nitrogen is in a moderate range. Apply nitrogen "
            "according to the crop stage and soil-test recommendation."
        )

    else:

        nitrogen_status = "High"

        nitrogen_recommendation = (
            "Nitrogen is relatively high. Avoid unnecessary "
            "additional nitrogen application."
        )


    # ======================================================
    # PHOSPHORUS STATUS
    # ======================================================

    if phosphorus < 30:

        phosphorus_status = "Low"

        phosphorus_recommendation = (
            "Consider a phosphorus source such as SSP. "
            "DAP may also be used where appropriate, while "
            "accounting for its nitrogen contribution."
        )

    elif phosphorus < 60:

        phosphorus_status = "Medium"

        phosphorus_recommendation = (
            "Phosphorus is in a moderate range. Maintain balanced "
            "fertilization based on crop requirement and soil testing."
        )

    else:

        phosphorus_status = "High"

        phosphorus_recommendation = (
            "Phosphorus is relatively high. Avoid unnecessary "
            "additional phosphorus application."
        )


    # ======================================================
    # POTASSIUM STATUS
    # ======================================================

    if potassium < 40:

        potassium_status = "Low"

        potassium_recommendation = (
            "Consider a potassium source such as muriate of potash "
            "(MOP) where suitable."
        )

    elif potassium < 80:

        potassium_status = "Medium"

        potassium_recommendation = (
            "Potassium is in a moderate range. Maintain a balanced "
            "fertilizer program."
        )

    else:

        potassium_status = "High"

        potassium_recommendation = (
            "Potassium is relatively high. Avoid unnecessary "
            "additional potassium application."
        )


    # ======================================================
    # SOIL pH STATUS
    # ======================================================

    if soil_ph < 5.5:

        ph_status = "Acidic"

        ph_recommendation = (
            "The soil is acidic. Soil testing and suitable "
            "lime-based amendments may be considered under "
            "local agricultural guidance."
        )

    elif soil_ph <= 7.5:

        ph_status = "Suitable Range"

        ph_recommendation = (
            "The soil pH is within a broadly suitable range "
            "for many crops."
        )

    elif soil_ph <= 8.5:

        ph_status = "Alkaline"

        ph_recommendation = (
            "The soil is somewhat alkaline. Use soil-test results "
            "to guide nutrient and soil-management practices."
        )

    else:

        ph_status = "Highly Alkaline"

        ph_recommendation = (
            "The soil is highly alkaline. Soil testing and local "
            "agricultural advice are recommended."
        )


    # ======================================================
    # NPK BALANCE SCORE
    # ======================================================

    nutrient_score = 0

    if nitrogen_status == "Medium":
        nutrient_score += 1

    elif nitrogen_status == "High":
        nutrient_score += 1


    if phosphorus_status == "Medium":
        nutrient_score += 1

    elif phosphorus_status == "High":
        nutrient_score += 1


    if potassium_status == "Medium":
        nutrient_score += 1

    elif potassium_status == "High":
        nutrient_score += 1


    # ======================================================
    # OVERALL NUTRIENT STATUS
    # ======================================================

    low_count = 0

    if nitrogen_status == "Low":
        low_count += 1

    if phosphorus_status == "Low":
        low_count += 1

    if potassium_status == "Low":
        low_count += 1


    if low_count == 0:

        overall_status = "Balanced / No Major Deficiency Detected"

    elif low_count == 1:

        overall_status = "One Major Nutrient Deficiency Detected"

    else:

        overall_status = "Multiple Nutrient Deficiencies Detected"


    # ======================================================
    # DISPLAY RESULTS
    # ======================================================

    st.divider()

    st.subheader(
        f"📊 Fertilizer Analysis for {crop}"
    )


    if farmer_name:
        st.write(f"**Farmer:** {farmer_name}")

    if state:
        st.write(f"**State:** {state}")

    if district:
        st.write(f"**District:** {district}")


    st.write(
        f"**Overall Nutrient Status:** {overall_status}"
    )


    # ======================================================
    # NPK STATUS METRICS
    # ======================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Nitrogen Status",
            nitrogen_status
        )

        st.write(
            f"N = {nitrogen:.2f}"
        )


    with col2:

        st.metric(
            "Phosphorus Status",
            phosphorus_status
        )

        st.write(
            f"P = {phosphorus:.2f}"
        )


    with col3:

        st.metric(
            "Potassium Status",
            potassium_status
        )

        st.write(
            f"K = {potassium:.2f}"
        )


    st.divider()


    # ======================================================
    # RECOMMENDATIONS
    # ======================================================

    st.subheader(
        "🌿 Fertilizer Recommendations"
    )


    st.write(
        "### 🟢 Nitrogen"
    )

    st.write(
        nitrogen_recommendation
    )


    st.write(
        "### 🟡 Phosphorus"
    )

    st.write(
        phosphorus_recommendation
    )


    st.write(
        "### 🔵 Potassium"
    )

    st.write(
        potassium_recommendation
    )


    # ======================================================
    # PH ANALYSIS
    # ======================================================

    st.subheader(
        "🧪 Soil pH Analysis"
    )


    st.write(
        f"**Soil pH:** {soil_ph:.1f}"
    )

    st.write(
        f"**pH Status:** {ph_status}"
    )

    st.info(
        ph_recommendation
    )


    # ======================================================
    # FERTILIZER SUGGESTION
    # ======================================================

    st.subheader(
        "✅ Suggested Fertilizer Approach"
    )


    suggestions = []


    if nitrogen_status == "Low":

        suggestions.append(
            "Nitrogen source recommended"
        )


    if phosphorus_status == "Low":

        suggestions.append(
            "Phosphorus source recommended"
        )


    if potassium_status == "Low":

        suggestions.append(
            "Potassium source recommended"
        )


    if not suggestions:

        suggestions.append(
            "No major NPK deficiency detected from the entered values."
        )


    for suggestion in suggestions:

        st.write(
            f"🔸 {suggestion}"
        )


    # ======================================================
    # SOIL MANAGEMENT ADVICE
    # ======================================================

    st.subheader(
        "💡 Smart Farming Recommendations"
    )


    st.write(
        "🌱 Use soil-test results before deciding actual fertilizer quantity."
    )

    st.write(
        "🌱 Prefer balanced nutrient management rather than applying "
        "large quantities of a single nutrient."
    )

    st.write(
        "🌱 Consider crop stage when planning fertilizer application."
    )

    st.write(
        "🌱 Avoid unnecessary fertilizer use to reduce cost and "
        "minimize nutrient losses."
    )

    st.write(
        "🌱 Organic manure or compost may be incorporated as part "
        "of an integrated nutrient-management approach."
    )


    # ======================================================
    # FINAL RESULT
    # ======================================================

    if low_count == 0:

        st.success(
            "✅ The entered NPK values do not indicate a major nutrient deficiency."
        )

    elif low_count == 1:

        st.warning(
            "⚠️ One major nutrient deficiency was detected. "
            "Review the recommended nutrient source."
        )

    else:

        st.error(
            "⚠️ Multiple nutrient deficiencies were detected. "
            "A balanced nutrient-management plan is recommended."
        )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "🌿 Fertilizer recommendations are estimates based on the "
    "entered soil values. Actual fertilizer application rates "
    "should be determined from soil-test results and local crop guidance."
)