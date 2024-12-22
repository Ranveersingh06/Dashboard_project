# Investment Data Analysis and Visualization Dashboard

This project is an interactive dashboard built with Streamlit for exploring and analyzing cleaned investment data. The application leverages various Python libraries and functionalities to deliver intuitive insights and powerful visualizations.

## Features

### 1. **Interactive Filters:**
   - Filter data by **Country**, **Sector**, **Company Status**, and a customizable **Year Range**.
   - Multiselect options and a "Select All" checkbox provide flexibility in filtering.

### 2. **Key Performance Indicators (KPIs):**
   - **Total Funding:** Displays the total funding in millions.
   - **Total Sectors:** Number of unique sectors represented.
   - **Total Companies:** Number of unique companies.
   - **Average Funding:** Average funding per company in millions.

### 3. **Visualizations:**
   - **Funding Trends Over Time:** Line chart showing total funding by year.
   - **Top 10 Companies by Funding:** Bar chart with categorical segmentation by market.
   - **Top 10 Markets by Total Funding:** Interactive pie chart.
   - **Distribution of Funding Rounds:** Bar chart for companies with multiple funding rounds.
   - **Timeline of Fast-Growing Companies:** Scatter chart highlighting companies with rapid growth.
   - **Top 50 Companies with Recent Funding:** Bar chart for companies with funding from 2012 to 2014.
   - **Geographical Distribution:**
     - **By City:** Bar chart showing top 20 cities by total funding.
     - **By Region:** Bar chart showing top 20 regions by total funding (if available).

## Libraries and Technologies Used

- **Streamlit:** For creating the interactive dashboard.
- **Pandas:** Data cleaning and manipulation.
- **Matplotlib & Seaborn:** For static data visualizations.
- **Plotly:** For dynamic and interactive charts.

## Dataset Information

The dataset used for this project is **Investment_df_cleaned.csv**, which was preprocessed to ensure data quality. Specific cleaning steps included:

- Conversion of date columns (**founded_at**, **first_funding_at**, **last_funding_at**) to datetime format.
- Handling missing and non-numeric values in **founded_year**.
- Ensuring columns like **funding_rounds** and **funding_total_usd** are in usable formats.

## How to Run the Dashboard

1. Install the required libraries:
   ```bash
   pip install pandas matplotlib seaborn plotly streamlit
   ```

2. Place the cleaned dataset (**Investment_df_cleaned.csv**) in the project directory.

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

4. Access the dashboard in your browser at `http://localhost:8501`.

## Project Architecture

### Core Scripts:
- **app.py:** Main script for the Streamlit application.
- **functions.py:** Contains utility functions for:
  - Loading the dataset.
  - Converting date columns.
  - Implementing custom multiselect filters.

### Key Design Decisions:
- **Wide Layout:** Optimized for displaying multiple KPIs and visualizations simultaneously.
- **Interactive Elements:** Provides an engaging user experience for exploring the dataset.

## Insights Delivered

- Trends in funding over time for companies across various markets and regions.
- Identification of top-performing companies and sectors.
- Analysis of funding patterns for companies with multiple or rapid funding rounds.
- Geographical analysis of investments by city and region.



## Acknowledgments
Special thanks to the open-source community for the development of powerful tools like Streamlit, Pandas, Matplotlib, Seaborn, and Plotly.

