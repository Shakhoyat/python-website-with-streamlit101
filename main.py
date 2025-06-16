import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Analysis App")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
