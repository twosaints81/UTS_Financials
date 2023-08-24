import streamlit as st
import pandas as pd
import plotly.express as px


def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df


st.image("./images/UTS_LOGO.png")

# Upload CSV file for net income, clinical pay, and profit margin data
st.subheader("Upload your CSV data file")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = load_data(uploaded_file)
    fig = px.line(data, x="start_date", y="net_income", title="Weekly Net Income Chart")
    st.plotly_chart(fig)

    fig = px.line(
        data, x="start_date", y="total_clinical_pay", title="Weekly Clinical Pay Chart"
    )
    st.plotly_chart(fig)


# Upload CSV file for invoice total data
uploaded_invoice_file = st.file_uploader("Choose an Invoice CSV file", type="csv")

if uploaded_invoice_file is not None:
    data_invoice = load_data(uploaded_invoice_file)
    fig_invoice = px.line(
        data_invoice,
        x="start_date",
        y="invoice_total",
        title="Weekly Invoice Total Chart",
    )
    st.plotly_chart(fig_invoice)

# Upload Employees Profile CSV file
uploaded_employee_profile = st.file_uploader(
    "Choose the Employee Profile file", type="csv"
)

if uploaded_employee_profile is not None:
    data_employee_profile = load_data(uploaded_employee_profile)
    st.dataframe(data_employee_profile)

    # Filter the data based on your needs
    filtered_data = data_employee_profile

    # Interactive Details
    st.title("Employee Details")
    selected_employee = st.selectbox(
        "Select Employee", options=filtered_data["Provider_Last"].unique().tolist()
    )
    employee_details = filtered_data[
        filtered_data["Provider_Last"] == selected_employee
    ]
    st.bar_chart(employee_details[["Total_Compensation"]])

    # You can add more specific visualizations based on the data and needs
    st.area_chart(employee_details[["Total_Compensation"]])
