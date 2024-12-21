import pandas as pd
import streamlit as st

#Loads the CSV data into a pandas DataFrame.
def load_data(file):
    return pd.read_csv(file)



#Converts specified columns to datetime format.
def convert_dates(df, date_columns):
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    return df



# Function to create filter multiselect option in stramlit
def multiselect(title, options_list):
    selected = st.sidebar.multiselect(title, options_list)
    select_all = st.sidebar.checkbox("Select all", value=True, key=title)
    if select_all:
        selected_options = options_list
    else:
        selected_options = selected
    return selected_options





