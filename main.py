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
    column_to_filter = st.selectbox("Select column to filter", df.columns)
    filter_value = st.text_input("Enter value to filter")
    filtered_data = df[df[column_to_filter] == filter_value]
    st.write("Filtered Data:")
    st.write(filtered_data)
