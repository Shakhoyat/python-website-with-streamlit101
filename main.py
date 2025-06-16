from enum import unique
import select
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    
    st.write("Data Preview:")
    st.write(df.head())
    
    st.write("Data Summary:")
    st.write(df.describe())
    
    st.subheader("Filter Data ")
    columns=df.columns.tolist()
    column_to_filter = st.selectbox("Select column to filter by",columns)
    unique_values = df[column_to_filter].unique()
    selected_value = st.selectbox("Select value to filter by", unique_values)
    
