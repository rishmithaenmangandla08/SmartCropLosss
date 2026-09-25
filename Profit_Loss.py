import streamlit as st
import pandas as pd
import plotly.express as px


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Profit / Loss Estimation",
    page_icon="💰",
    layout="wide"
)


# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("💰 Profit / Loss Estimation")

st.markdown("""
### 🌾 Smart Farming Financial Analysis

This module estimates the expected production, revenue,
cultivation cost and possible profit or loss for a farming activity.

> **Note:** Results are estimates based on the values entered by the user.
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
        placeholder="Enter farmer name"
    )

    state = st.text_input(
        "State",
        placeholder="Enter state"
    )


with col2:

    district = st.text_input(
        "District",
        placeholder="Enter district"
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
        ]
    )


st.divider()


# ==========================================================
# PRODUCTION INPUTS
# ==========================================================

st.header("🌱 Production Details")

col1, col2, col3 = st.columns(3)

with col1:

    cultivation_area = st.number_input(
        "Cultivation Area (Acres)",
        min_value=0.1,
        value=1.0,
        step=0.1
    )


with col2:

    expected_yield = st.number_input(
        "Expected Yield (kg/acre)",
        min_value=0.0,
        value=2000.0,
        step=100.0
    )


with col3:

    selling_price = st.number_input(
        "Expected Selling Price (₹/kg)",
        min_value=0.0,
        value=25.0,
        step=1.0
    )


st.divider()


# ==========================================================
# COST DETAILS
# ==========================================================

st.header("💸 Cultivation Cost Details")

col1, col2, col3 = st.columns(3)

with col1:

    seed_cost = st.number_input(
        "Seed Cost (₹/acre)",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )


with col2:

    fertilizer_cost = st.number_input(
        "Fertilizer Cost (₹/acre)",
        min_value=0.0,
        value=5000.0,
        step=500.0
    )


with col3:

    labor_cost = st.number_input(
        "Labor Cost (₹/acre)",
        min_value=0.0,
        value=8000.0,
        step=500.0
    )


col4, col5, col6 = st.columns(3)

with col4:

    irrigation_cost = st.number_input(
        "Irrigation Cost (₹/acre)",
        min_value=0.0,
        value=4000.0,
        step=500.0
    )


with col5:

    pesticide_cost = st.number_input(
        "Pesticide Cost (₹/acre)",
        min_value=0.0,
        value=3000.0,
        step=500.0
    )


with col6:

    other_cost = st.number_input(
        "Other Costs (₹/acre)",
        min_value=0.0,
        value=2000.0,
        step=500.0
    )


st.divider()


# ==========================================================
# RISK / LOSS INPUT
# ==========================================================

st.header("⚠️ Expected Crop Loss")

expected_loss_percentage = st.slider(
    "Expected Crop Loss (%)",
    min_value=0,
    max_value=100,
    value=0,
    step=5
)

st.caption(
    "Enter an expected crop-loss percentage based on your "
    "risk assessment, weather conditions or historical data."
)


# ==========================================================
# CALCULATION BUTTON
# ==========================================================

if st.button(
    "📊 Calculate Profit / Loss",
    key="profit_loss_calculate_button"
):

    # ------------------------------------------------------
    # TOTAL COST PER ACRE
    # ------------------------------------------------------

    cost_per_acre = (
        seed_cost
        + fertilizer_cost
        + labor_cost
        + irrigation_cost
        + pesticide_cost
        + other_cost
    )


    # ------------------------------------------------------
    # TOTAL CULTIVATION COST
    # ------------------------------------------------------

    total_cost = (
        cost_per_acre
        * cultivation_area
    )


    # ------------------------------------------------------
    # EXPECTED PRODUCTION BEFORE LOSS
    # ------------------------------------------------------

    production_before_loss = (
        expected_yield
        * cultivation_area
    )


    # ------------------------------------------------------
    # PRODUCTION LOST
    # ------------------------------------------------------

    production_loss = (
        production_before_loss
        * expected_loss_percentage
        / 100
    )


    # ------------------------------------------------------
    # ACTUAL EXPECTED PRODUCTION
    # ------------------------------------------------------

    actual_expected_production = (
        production_before_loss
        - production_loss
    )


    # ------------------------------------------------------
    # EXPECTED REVENUE
    # ------------------------------------------------------

    expected_revenue = (
        actual_expected_production
        * selling_price
    )


    # ------------------------------------------------------
    # PROFIT / LOSS
    # ------------------------------------------------------

    profit_loss = (
        expected_revenue
        - total_cost
    )


    # ------------------------------------------------------
    # BREAK-EVEN PRICE
    # ------------------------------------------------------

    if actual_expected_production > 0:

        break_even_price = (
            total_cost
            / actual_expected_production
        )

    else:

        break_even_price = 0


    # ------------------------------------------------------
    # BREAK-EVEN YIELD PER ACRE
    # ------------------------------------------------------

    if selling_price > 0:

        break_even_total_yield = (
            total_cost
            / selling_price
        )

        break_even_yield_per_acre = (
            break_even_total_yield
            / cultivation_area
        )

    else:

        break_even_total_yield = 0
        break_even_yield_per_acre = 0


    # ------------------------------------------------------
    # ROI
    # ------------------------------------------------------

    if total_cost > 0:

        roi = (
            profit_loss
            / total_cost
            * 100
        )

    else:

        roi = 0


    # ======================================================
    # RESULT HEADER
    # ======================================================

    st.divider()

    st.subheader(
        f"📋 Financial Analysis for {crop_name}"
    )


    if farmer_name:

        st.write(
            f"**Farmer:** {farmer_name}"
        )

    if state:

        st.write(
            f"**State:** {state}"
        )

    if district:

        st.write(
            f"**District:** {district}"
        )


    # ======================================================
    # MAIN METRICS
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🌾 Expected Production",
            f"{actual_expected_production:,.2f} kg"
        )


    with col2:

        st.metric(
            "💵 Expected Revenue",
            f"₹{expected_revenue:,.2f}"
        )


    with col3:

        st.metric(
            "💸 Total Cost",
            f"₹{total_cost:,.2f}"
        )


    with col4:

        st.metric(
            "📈 ROI",
            f"{roi:.2f}%"
        )


    st.divider()


    # ======================================================
    # PROFIT / LOSS RESULT
    # ======================================================

    if profit_loss > 0:

        st.success(
            f"✅ Estimated Profit: ₹{profit_loss:,.2f}"
        )

    elif profit_loss < 0:

        st.error(
            f"⚠️ Estimated Loss: ₹{abs(profit_loss):,.2f}"
        )

    else:

        st.warning(
            "⚖️ Estimated Result: Break-even"
        )


    # ======================================================
    # BREAK-EVEN INFORMATION
    # ======================================================

    st.subheader(
        "⚖️ Break-Even Analysis"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Break-Even Selling Price",
            f"₹{break_even_price:,.2f}/kg"
        )


    with col2:

        st.metric(
            "Break-Even Yield",
            f"{break_even_yield_per_acre:,.2f} kg/acre"
        )


    # ======================================================
    # PRODUCTION SUMMARY
    # ======================================================

    st.subheader(
        "🌾 Production Summary"
    )

    st.write(
        f"**Production before expected loss:** "
        f"{production_before_loss:,.2f} kg"
    )

    st.write(
        f"**Expected crop loss:** "
        f"{production_loss:,.2f} kg "
        f"({expected_loss_percentage}%)"
    )

    st.write(
        f"**Expected final production:** "
        f"{actual_expected_production:,.2f} kg"
    )


    # ======================================================
    # COST BREAKDOWN
    # ======================================================

    st.subheader(
        "💸 Cost Breakdown"
    )

    cost_data = pd.DataFrame({

        "Cost Type": [
            "Seed",
            "Fertilizer",
            "Labor",
            "Irrigation",
            "Pesticide",
            "Other"
        ],

        "Cost (₹)": [
            seed_cost * cultivation_area,
            fertilizer_cost * cultivation_area,
            labor_cost * cultivation_area,
            irrigation_cost * cultivation_area,
            pesticide_cost * cultivation_area,
            other_cost * cultivation_area
        ]
    })


    st.dataframe(
        cost_data,
        use_container_width=True
    )


    # ======================================================
    # COST VISUALIZATION
    # ======================================================

    fig = px.bar(
        cost_data,
        x="Cost Type",
        y="Cost (₹)",
        title="Cultivation Cost Breakdown",
        text_auto=".2f"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ======================================================
    # REVENUE VS COST CHART
    # ======================================================

    comparison_data = pd.DataFrame({

        "Category": [
            "Revenue",
            "Cost"
        ],

        "Amount (₹)": [
            expected_revenue,
            total_cost
        ]
    })


    comparison_fig = px.bar(
        comparison_data,
        x="Category",
        y="Amount (₹)",
        title="Revenue vs Cultivation Cost",
        text_auto=".2f"
    )

    st.plotly_chart(
        comparison_fig,
        use_container_width=True
    )


    # ======================================================
    # FINAL INTERPRETATION
    # ======================================================

    st.subheader(
        "📌 Financial Summary"
    )

    st.write(
        f"""
        The selected crop is **{crop_name}**.

        The estimated production is
        **{actual_expected_production:,.2f} kg**.

        The expected revenue is
        **₹{expected_revenue:,.2f}**.

        The total cultivation cost is
        **₹{total_cost:,.2f}**.
        """
    )

    if profit_loss > 0:

        st.success(
            f"""
            Based on the entered assumptions, the estimated
            financial outcome is a **profit of ₹{profit_loss:,.2f}**.
            """
        )

    elif profit_loss < 0:

        st.warning(
            f"""
            Based on the entered assumptions, the estimated
            financial outcome is a **loss of ₹{abs(profit_loss):,.2f}**.
            """
        )

    else:

        st.info(
            """
            Based on the entered assumptions, the estimated
            financial outcome is approximately break-even.
            """
        )

    st.caption(
        "Profit/Loss values are estimates and depend on actual "
        "yield, market price, production cost and crop losses."
    )