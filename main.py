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
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)
    
    plot_type = st.selectbox("Select plot type", ["Line", "Bar", "Histogram", "Scatter"])
    plt.figure(figsize=(10, 5))
    if plot_type == "Line":
       st.line_chart(filtered_df.set_index(x_column)[y_column])
    elif plot_type == "Bar":
       st.bar_chart(filtered_df.set_index(x_column)[y_column])
    elif plot_type == "Histogram":
       column_to_plot = st.selectbox("Select column to plot", columns)
       plt.figure()
       plt.hist(filtered_df[column_to_plot].dropna(), bins=20)
       plt.xlabel(column_to_plot)
       plt.ylabel("Frequency")
       st.pyplot(plt)
    elif plot_type == "Scatter":
       plt.figure()
       plt.scatter(filtered_df[x_column], filtered_df[y_column])
       plt.xlabel(x_column)
       plt.ylabel(y_column)
       st.pyplot(plt)
else:
    st.write("Please upload a CSV file to start.")