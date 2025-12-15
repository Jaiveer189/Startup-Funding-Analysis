import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 

st.set_page_config(page_title='Startup Funding Analysis', layout='wide')

st.title('Startup Funding Analysis Dashboard')
st.markdown('Interactive analysis of Startup funding trends,industries, and locations.')


@st.cache_data #cache data improve performance
def load_data():
    data = {
        'Startup Name': ['OYO', 'Paytm', "Byju's", 'Zomato', 'Flipkart', 'Swiggy', 'Ola', 'PhonePe', 'Delhivery', 'Lenskart'],
        'Industry': ['Hospitality', 'Fintech', 'EdTech', 'FoodTech', 'E-Commerce', 'FoodTech', 'Logistics', 'Fintech', 'Logistics', 'E-Commerce'],
        'Investors': ['SoftBank', 'Alibaba', 'Tencent', 'Sequoia', 'Tiger Global', 'Naspers', 'SoftBank', 'Walmart', 'Tiger Global', 'SoftBank'],
        'Funding Amount (Cr)': [1500, 1200, 1000, 800, 950, 700, 1100, 1300, 600, 500],
        'Location': ['Bangalore', 'Noida', 'Bangalore', 'Gurgaon', 'Bangalore', 'Bangalore', 'Bangalore', 'Bangalore', 'Gurgaon', 'Delhi'],
        'Date': ['2019-06-15', '2020-01-20', '2018-09-10', '2021-03-12', '2019-11-30', '2020-05-15', '2018-12-01', '2021-08-22', '2019-04-10', '2020-10-05']
    }
    df = pd.DataFrame(data)

    #preprocessing(from notebook)
    df['Funding Amount (Cr)'] = pd.to_numeric(df['Funding Amount (Cr)'], errors='coerce')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    return df
df = load_data()

st.sidebar.header("Filter data")

#Year filter
years = sorted(df['Year'].unique())
selected_years = st.sidebar.multiselect("Select Years",years, default=years)

#Industry filter 
industries = sorted(df['Industry'].unique())
selected_industries = st.sidebar.multiselect("Select Industries",industries, default=industries)

#Filter the dataframe
filtered_df = df[(df['Year'].isin(selected_years)) & (df['Industry'].isin(selected_industries))]

#---KPI Cards---
col1, col2, col3 = st.columns(3)
col1.metric("Total Funding", f"{filtered_df['Funding Amount (Cr)'].sum()} Cr")
avg_funding = filtered_df['Funding Amount (Cr)'].mean()
col2.metric("Average Funding", f"{round(avg_funding, 2) if pd.notna(avg_funding) else 0} Cr")
col3.metric("Number of Startups", len(filtered_df))

st.markdown("____")

#---visulizations----
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("💰 Top Funded Industries")
    industry_funding = filtered_df.groupby('Industry')['Funding Amount (Cr)'].sum().sort_values(ascending=False)
    
    # Using Plotly for interactivity
    fig_ind = px.bar(
        industry_funding, 
        x=industry_funding.index, 
        y=industry_funding.values,
        labels={'y': 'Funding Amount (Cr)', 'Industry': 'Industry'},
        color=industry_funding.values,
        color_continuous_scale='Viridis'
    )
    st.plotly_chart(fig_ind, use_container_width=True)

with col_chart2:
    st.subheader("📅 Year-wise Funding Trend")
    yearly_funding = filtered_df.groupby('Year')['Funding Amount (Cr)'].sum()
    
    fig_year = px.line(
        yearly_funding, 
        x=yearly_funding.index, 
        y=yearly_funding.values,
        labels={'y': 'Funding Amount (Cr)', 'Year': 'Year'},
        markers=True
    )
    st.plotly_chart(fig_year, use_container_width=True)

st.markdown("---")

# Row 2: Top Investors & Location Analysis
col_chart3, col_chart4 = st.columns(2)

with col_chart3:
    st.subheader("🤝 Top Investors")
    investor_funding = filtered_df.groupby('Investors')['Funding Amount (Cr)'].sum().sort_values(ascending=False)
    
    fig_inv = px.bar(
        investor_funding, 
        x=investor_funding.index, 
        y=investor_funding.values,
        labels={'y': 'Funding Amount (Cr)', 'Investors': 'Investor'},
        color_discrete_sequence=['#FF6692']
    )
    st.plotly_chart(fig_inv, use_container_width=True)

with col_chart4:
    st.subheader("📍 Funding by Location")
    location_funding = filtered_df.groupby('Location')['Funding Amount (Cr)'].sum()
    
    fig_loc = px.pie(
        values=location_funding.values, 
        names=location_funding.index,
        hole=0.4
        )
    st.plotly_chart(fig_loc, use_container_width=True)

    #---data table---
    st.markdown("___")
    st.subheader("Deatiled data view")
    st.dataframe(filtered_df)

    from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading


