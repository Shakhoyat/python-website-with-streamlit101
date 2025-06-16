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
    plot_type = st.selectbox("Select plot type", ["Line", "Bar", "Histogram", "Scatter"])

    if plot_type == "Histogram":
        numeric_columns = filtered_df.select_dtypes(include='number').columns.tolist()
        if numeric_columns:
            column_to_plot = st.selectbox("Select column to plot", numeric_columns)
            if st.button("Generate Plot"):
                fig, ax = plt.subplots()
                ax.hist(filtered_df[column_to_plot].dropna(), bins=20, color='skyblue', edgecolor='black')
                ax.set_xlabel(column_to_plot)
                ax.set_ylabel("Frequency")
                ax.set_title(f"Histogram of {column_to_plot}")
                st.pyplot(fig)
        else:
            st.warning("No numeric columns available for histogram.")
    else:
        numeric_columns = filtered_df.select_dtypes(include='number').columns.tolist()
        if len(numeric_columns) < 1:
            st.warning("No numeric columns available for plotting.")
        else:
            x_column = st.selectbox("Select X-axis column", filtered_df.columns, key="x_axis")
            y_column = st.selectbox("Select Y-axis column", numeric_columns, key="y_axis")
            if st.button("Generate Plot"):
                fig, ax = plt.subplots()
                if plot_type == "Line":
                    ax.plot(filtered_df[x_column], filtered_df[y_column], marker='o')
                    ax.set_title(f"Line Plot of {y_column} vs {x_column}")
                elif plot_type == "Bar":
                    ax.bar(filtered_df[x_column], filtered_df[y_column])
                    ax.set_title(f"Bar Plot of {y_column} vs {x_column}")
                elif plot_type == "Scatter":
                    ax.scatter(filtered_df[x_column], filtered_df[y_column])
                    ax.set_title(f"Scatter Plot of {y_column} vs {x_column}")
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                plt.xticks(rotation=45)
                st.pyplot(fig)
else:
    st.write("Please upload a CSV file to start.")