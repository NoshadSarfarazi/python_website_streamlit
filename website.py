import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt  


st.title("My Website")
st.header("Project # 09")

upload_file = st.file_uploader("choose a CSV file ", type = "csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select Columns", columns)
    unique_values = df[selected_columns].unique()
    selected_value = st.selectbox("Select Value", unique_values)

    filtered_df = df[df[selected_columns] == selected_value]
    st.subheader("Filtered Data")
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df[[x_axis, y_axis]])

else:
    st.warning("Please upload a CSV file.")



   