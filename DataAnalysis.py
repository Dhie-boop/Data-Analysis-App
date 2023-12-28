# Imports
import streamlit as st
import pandas as pd
import seaborn as sns
from io import BytesIO

st.set_option('deprecation.showPyplotGlobalUse', False)

# Title and sub-header
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

# Upload Data set
upload = st.file_uploader("Upload your dataset (in CSV or Excel format)")
if upload is not None:
    if upload.name.endswith('.csv'):
        data = pd.read_csv(upload)
    elif upload.name.endswith(('.xls', '.xlsx')):
        data = pd.read_excel(upload)

    # Show the dataset
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

    # Check the datatype of each column
    if st.checkbox("Data type of each column."):
        st.text("Datatypes")
        st.write(data.dtypes)

    # Find the shape of the dataset (number of rows and columns)
    data_shape = st.radio("What dimension do you want to check?", ('Rows', 'Columns'))
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of columns")
        st.write(data.shape[1])

    # Finding Null values in the dataset
    test = data.isnull().values.any()
    if test:
        if st.checkbox("Null values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!!!, No Missing Values")

    # Find Duplicate Values in the Data Set
    test = data.duplicated().any()
    if test:
        st.warning("This Dataset contains some duplicate values.")
        dup = st.selectbox("Do you want to remove duplicated values?", ("Select One", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values were Removed")
        if dup == "No":
            st.text("Okay, No problem")

    # Get the overall statistics about the dataset
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include='all'))

    # Generate a report
    if st.button("Generate Report"):
        # Create a simple report, you can customize this based on your needs
        report = f"# Data Analysis Report\n\n"
        report += f"## Dataset Preview\n{data.head()}\n\n"
        report += f"## Data Types\n{data.dtypes}\n\n"
        report += f"## Number of Rows\n{data.shape[0]}\n\n"
        report += f"## Number of Columns\n{data.shape[1]}\n\n"
        report += f"## Null Values\n{data.isnull().sum()}\n\n"
        report += f"## Duplicate Values\n{data.duplicated().sum()}\n\n"
        report += f"## Summary\n{data.describe(include='all')}\n\n"

        # Display the report
        st.text_area("Data Analysis Report", report)

# About Section
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Made with love by Dhieu.")

if st.checkbox("By"):
    st.success("Dhieu David.")
