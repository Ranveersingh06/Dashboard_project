import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st
import functions


# Set up the page configuration
st.set_page_config(page_title="Data Analysis and Visualization Dashboard",layout="wide")

#st.image("", use_column_width=True)


df = pd.read_csv('Investment_df_cleaned.csv.csv')


date_columns = ['founded_at', 'first_funding_at', 'last_funding_at']
df = functions.convert_dates(df, date_columns)

# Ensure 'founded_year' is numeric
df['founded_year'] = pd.to_numeric(df['founded_year'], errors='coerce').astype(int)


mini = df['founded_year'].min()
maxm = df['founded_year'].max()


# Use Markdown to center the title
st.markdown("<h1 style='text-align: center;'>📊Investment Data Analysis</h1>", unsafe_allow_html=True)


# Use markdown to render a custom-styled horizontal line (divider)
st.markdown("<hr style='border-top: 2px solid #2F4F4F;'>", unsafe_allow_html=True)


# Title and Sidebar
st.sidebar.title("Filters")


# Filters
selected_country = functions.multiselect('Select Country', df['country_code'].unique())
selected_sector = functions.multiselect('Select Sectors', df['market'].unique())
selected_status = functions.multiselect('Select Status', df['status'].unique())
selected_year_range = st.sidebar.slider('Select Year Range', df['founded_year'].min(), df['founded_year'].max(), (mini, maxm))


filtered_data = df[
        (df['country_code'].isin(selected_country)) &
        (df['market'].isin(selected_sector)) &
        (df['status'].isin(selected_status)) &
        (df['founded_year'].between(selected_year_range[0], selected_year_range[1]))]





# KPI - Key Performance Indicator
# colums for displaying KPIs
col1, col2, col3, col4 = st.columns(4)

# Total funding
with col1:
    st.metric(label='Total Funding (in Millions)', value=f'${filtered_data["funding_total_usd"].sum() / 1000000:.2f}M')

# Total Number of Sectors
with col2:
    st.metric(label = 'Total Sectors', value = len(set(filtered_data['market'])))

# Total Number of Companies
with col3:
    st.metric(label = 'Total Companies', value = len(set(filtered_data['name'])))

# Average Funding Per Company
with col4:
    st.metric(label = 'Average Funding(in Millions)', value = f'${filtered_data["funding_total_usd"].mean() / 1000000:.2f}M')





#1
# Funding Trends Over Time
st.subheader(' Funding Trends Over Time ')

funding_by_year = filtered_data.groupby('founded_year')["funding_total_usd"].sum().reset_index()

st.line_chart(data=funding_by_year, x='founded_year', y='funding_total_usd')





# Create two columns for side-by-side layout
col1, col2 = st.columns([1.1 , 0.9])  # Equal width for both columns

# 2. Top 10 Companies by Funding (Categorized by Market)
with col1:
    st.subheader('Top 10 Companies by Funding ')

    top_10 = filtered_data.groupby(["market", "name", "status"])[["funding_total_usd"]].sum().reset_index()
    top_10 = top_10.sort_values(by='funding_total_usd', ascending=False).head(10)

    st.bar_chart(data=top_10, x='name', y='funding_total_usd', color='market', height=500)  # Adjust height to avoid too much space
    


# 3. Top 10 Markets by Total Funding (USD)
with col2:
    st.subheader('Top 10 Markets by Total Funding ')

    top_10_markets = filtered_data.groupby("market")["funding_total_usd"].sum().nlargest(10).reset_index()

    fig = px.pie(top_10_markets, values='funding_total_usd', names='market')

    st.plotly_chart(fig, use_container_width=True)  # Ensure pie chart fits container width



# Create two columns for side-by-side layout
col3, col4 = st.columns([1,1])
#4
# Distribution of Funding Rounds
with col3:
    st.subheader(" Distribution of Funding Rounds for Multi-Round Companies ")
    
    multi_round_companies =filtered_data[filtered_data['funding_rounds'] > 1]
    
    st.bar_chart(multi_round_companies['funding_rounds'].value_counts(), height=500)



#5
# Timeline of Funding Rounds for Fast-Growing Companies
with col4 : 
    st.subheader(" Timeline of Funding Rounds for Fast-Growing Companies ")
    
    filtered_data['funding_duration'] = (filtered_data['last_funding_at'] - filtered_data['first_funding_at']).dt.days
    fast_growing_companies = filtered_data[(filtered_data['funding_rounds'] >= 3) & (filtered_data['funding_duration'] <= 730)]
    
    st.scatter_chart(data=fast_growing_companies, x='first_funding_at', y='funding_rounds', size='funding_duration', color='funding_duration', height=550)







#6
# Top 20 Companies with Recent Funding (Last 3 Years from 2014)
st.subheader(' Top 50 Companies with Recent Funding (From 2012 to 2014) ')

current_date = pd.to_datetime('2014-12-31')
cutoff_date = current_date - pd.DateOffset(years=3)
# filtered_data['last_funding_at'] = pd.to_datetime(filtered_data['last_funding_at'], errors='coerce')
recent_funding_companies = filtered_data[filtered_data['last_funding_at'] > cutoff_date]
recent_funding_count = recent_funding_companies.groupby(["name","market"])["last_funding_at"].count().nlargest(50).reset_index()

st.bar_chart(data=recent_funding_count, x='name', y='last_funding_at',color='market', height=500)


############
col5, col6 = st.columns([1,1])

#7

with col5:
    st.subheader("Geographical Distribution of Investments by City")
    
    # Grouping the data by city and summing the total funding
    city_funding = filtered_data.groupby('city')['funding_total_usd'].sum().reset_index()
    
    # Creating a bar chart for city-wise funding
    fig_city = px.bar(
        city_funding.sort_values('funding_total_usd', ascending=False).head(20),  # Top 20 cities
        x='city',
        y='funding_total_usd',
        color='funding_total_usd',
        title='Top 20 Cities by Total Funding',
        labels={'funding_total_usd': 'Total Funding (USD)', 'city': 'City'},
        color_continuous_scale=px.colors.sequential.Plasma
    )
    st.plotly_chart(fig_city, use_container_width=True)


with col6:
# 8
# Grouping the data by region and summing the total funding
    st.subheader("Geographical Distribution of Investments by Region")
    
    if 'region' in filtered_data.columns:
        region_funding = filtered_data.groupby('region')['funding_total_usd'].sum().reset_index()
    
        # Creating a bar chart for region-wise funding
        fig_region = px.bar(
            region_funding.sort_values('funding_total_usd', ascending=False).head(20),  # Top 20 regions
            x='region',
            y='funding_total_usd',
            color='funding_total_usd',
            title='Top 20 Regions by Total Funding',
            labels={'funding_total_usd': 'Total Funding (USD)', 'region': 'Region'},
            color_continuous_scale=px.colors.sequential.Plasma
        )
        st.plotly_chart(fig_region, use_container_width=True)
    else:
        st.warning("Region data not available in the dataset.")




