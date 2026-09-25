import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Soil Analysis", page_icon="🌱")

st.title("🌱 Soil Analysis")

st.write("Analysis of Soil Nutrients and pH")

st.divider()

# -----------------------------
# Load Dataset
# -----------------------------
soil_df = pd.read_csv("datasets/cleaned/Soil_data_cleaned.csv")

# Remove extra spaces from column names
soil_df.columns = soil_df.columns.str.strip()

# -----------------------------
# Dataset Information
# -----------------------------
st.subheader("📋 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", soil_df.shape[0])

with col2:
    st.metric("Columns", soil_df.shape[1])

st.divider()

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📄 First 10 Records")

st.dataframe(soil_df.head(10))

st.divider()

# -----------------------------
# Summary Statistics
# -----------------------------
st.subheader("📊 Summary Statistics")

st.dataframe(soil_df.describe())

st.divider()

# -----------------------------
# Missing Values
# -----------------------------
st.subheader("❌ Missing Values")

st.write(soil_df.isnull().sum())

st.divider()

# -----------------------------
# Nitrogen Graph
# -----------------------------
st.subheader("🟢 Nitrogen Value")

st.bar_chart(soil_df["Nitrogen Value"])

# -----------------------------
# Phosphorous Graph
# -----------------------------
st.subheader("🟡 Phosphorous Value")

st.line_chart(soil_df["Phosphorous value"])

# -----------------------------
# Potassium Graph
# -----------------------------
st.subheader("🟠 Potassium Value")

st.area_chart(soil_df["Potassium value"])

# -----------------------------
# Soil pH Graph
# -----------------------------
st.subheader("🟣 Soil pH")

st.bar_chart(soil_df["pH"])

st.divider()

st.success("✅ Soil Analysis Completed Successfully")
