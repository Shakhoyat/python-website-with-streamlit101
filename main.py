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
    
    filtered_df = df[df[column_to_filter] == selected_value]
    st.write("Filtered Data:")
    st.write(filtered_df)
    
    st.subheader("Visualize Data")
    plot_type = st.selectbox("Select plot type", ["Line", "Bar", "Histogram"])
    if plot_type == "Line":
        st.line_chart(filtered_df)
    elif plot_type == "Bar":
        st.bar_chart(filtered_df)
    elif plot_type == "Histogram":
        st.write("Histogram of selected column:")
        column_to_plot = st.selectbox("Select column to plot", columns)
        plt.hist(filtered_df[column_to_plot], bins=20)
        st.pyplot(plt)
