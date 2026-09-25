
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard")
# Load cleaned dataset
crop_df = pd.read_csv("datasets/cleaned/Crop_recommendation_cleaned.csv")


st.title("📊 Dashboard")

st.write("Welcome to Smart Crop Loss Dashboard")

st.divider()

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Datasets","4")

with col2:
    st.metric("Total Records", len(crop_df))

with col3:
    st.metric("Crop Types", crop_df["label"].nunique())

st.divider()

st.subheader("Project Modules")

st.success("🌾 Crop Recommendation")

st.success("🌱 Soil Analysis")

st.success("🌧 Rainfall Analysis")

st.success("💧 Irrigation Analysis")

st.success("📈 Statistics")

st.success("💰 Profit/Loss Prediction")

st.divider()

st.subheader("Dataset Information")

st.write("Number of Rows:", crop_df.shape[0])

st.write("Number of Columns:", crop_df.shape[1])

st.write("Column Names:")

st.write(list(crop_df.columns))

st.divider()

st.subheader("Summary Statistics")

st.dataframe(crop_df.describe())
st.divider()

st.subheader("Missing Values")

st.write(crop_df.isnull().sum())

st.divider()

st.subheader("Temperature Distribution")

st.bar_chart(crop_df["temperature"].head(20))