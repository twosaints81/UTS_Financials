# UTS Financial Report using Streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


def load_data(uploaded_file):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df

# Upload CSV file for the net income, clinical pay, and profit margin data
st.subheader('Upload your CSV data file')
uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

data = load_data(uploaded_file)
if data is not None:
    st.image('./images/UTS_Logo.png')
    st.subheader('Admin Dashboard')

    fig = px.line(data, x='start_date', y='net_income', title='Weekly Net Income Chart')
    st.plotly_chart(fig)

    fig2 = px.line(data, x='start_date', y='total_clinical_pay', title='Weekly Total Clinical Pay Chart')
    st.plotly_chart(fig2)

    fig3 = px.bar(data, x='start_date', y='profit_margin', title='Weekly Profit Margin Chart')
    st.plotly_chart(fig3)

    # Download button
    st.markdown("### Download CSV file ###")
    st.dataframe(data)
    st.download_button("Click here to download the data as CSV file", data.to_csv(index=False), "UTS_Financial_Data.csv", "text/csv")

# Upload CSV file for invoice total data
st.subheader('Upload your Invoice CSV file')
uploaded_invoice_file = st.file_uploader("Choose an Invoice CSV file", type='csv')

data_invoice = load_data(uploaded_invoice_file)
if data_invoice is not None:
    st.subheader('Weekly Invoice Total')
    fig4 = px.line(data_invoice, x='start_date', y='invoice_total', title='Weekly Invoice Total Chart')
    st.plotly_chart(fig4)
    st.dataframe(data_invoice)
    st.download_button("Click here to download the data as CSV file", data_invoice.to_csv(index=False), "UTS_Invoice_Data.csv", "text/csv")

st.write('---')
st.subheader('I plan to incorporate Batchgeo Here')

# Upload CSV file for map data
st.subheader('Upload your Map CSV file')
uploaded_map_file = st.file_uploader("Choose a Map CSV file", type='csv')

data_map = load_data(uploaded_map_file)
if data_map is not None:
    st.map(data_map)
