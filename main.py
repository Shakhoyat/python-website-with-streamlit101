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
    
