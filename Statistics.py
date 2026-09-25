import streamlit as st
import pandas as pd

st.set_page_config(page_title="Statistics")

st.title("📊 Statistics")

st.write("Crop Recommendation Dataset Statistics")

# Load Dataset
crop_df = pd.read_csv("datasets/cleaned/Crop_recommendation_cleaned.csv")

st.divider()

# Basic Information
st.subheader("Dataset Information")

st.write("Total Rows:", crop_df.shape[0])

st.write("Total Columns:", crop_df.shape[1])

st.write("Crop Types:", crop_df["label"].nunique())

st.divider()

# Dataset Preview
st.subheader("Dataset Preview")

st.dataframe(crop_df.head())

st.divider()

# Summary Statistics
st.subheader("Summary Statistics")

st.dataframe(crop_df.describe())

st.divider()

# Crop Distribution
st.subheader("Temperature Distribution")

st.bar_chart(crop_df["temperature"])