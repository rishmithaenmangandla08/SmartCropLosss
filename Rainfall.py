import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Rainfall Analysis", page_icon="🌧")

st.title("🌧 Rainfall Analysis")

# Load Dataset
rain_df = pd.read_csv("datasets/cleaned/Rainfall_cleaned.csv")

# Remove extra spaces from column names
rain_df.columns = rain_df.columns.str.strip()

# Dataset Information
st.subheader("📋 Dataset Information")

st.write("Rows:", rain_df.shape[0])
st.write("Columns:", rain_df.shape[1])

st.divider()

# Display Column Names
st.subheader("📌 Column Names")

for col in rain_df.columns:
    st.write("✅", col)

st.divider()

# Preview Dataset
st.subheader("📄 First 10 Records")
st.dataframe(rain_df.head(10))

st.divider()

# Summary Statistics
st.subheader("📊 Summary Statistics")
st.dataframe(rain_df.describe())

st.divider()

# Missing Values
st.subheader("❌ Missing Values")
st.write(rain_df.isnull().sum())

st.divider()

# Average Rainfall Graph
st.subheader("🌧 Average Rainfall")
st.bar_chart(rain_df["Avg_rainfall"])

st.divider()

st.success("✅ Rainfall Analysis Completed Successfully")