import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page configuration for better layout
st.set_page_config(page_title="Bike Sharing Data Analysis", layout="wide")

# Sidebar for user interaction
st.sidebar.header("Dashboard Navigation")
options = st.sidebar.radio("Select an option", 
                            ["Home", "Data Overview", "Visualizations", "Key Insights"])

# Set up the title and description of the app
st.title("🚴‍♂️ Bike Sharing Data Analysis Dashboard")
st.write("This dashboard presents insights from the bike sharing dataset.")
st.write("Analyzing seasonal effects, weather impacts, and user demographics.")

# Load the dataset
data_day = pd.read_csv('data_1.csv')
data_hour = pd.read_csv('data_2.csv')

# Home Section
if options == "Home":
    st.header("Welcome to the Bike Sharing Data Analysis Dashboard")
    st.write("""
        This interactive dashboard allows you to explore various aspects of bike sharing data.
        The data is segmented into daily and hourly records, providing insights into user behavior,
        seasonal trends, and the impact of weather conditions on bike rentals.
        
        Use the navigation panel on the left to explore the **Data Overview**, **Visualizations**, 
        and **Key Insights** sections for a comprehensive understanding of the dataset.
    """)

# Data Overview with Pagination
if options == "Data Overview":
    st.subheader('Daily Data Overview')
    st.write("""
        The daily data overview presents a sample of bike sharing records over the course of the dataset.
        Each record includes information such as the date, season, weather conditions, and the count of bike rentals.
        You can navigate through the dataset using the pagination controls below.
    """)
    daily_data_page = st.number_input('Select Page', min_value=1, 
                                        max_value=int(len(data_day)/10) + 1, value=1)
    daily_data_start = (daily_data_page - 1) * 10
    daily_data_end = daily_data_start + 10
    st.write(data_day[daily_data_start:daily_data_end])

    st.subheader('Hourly Data Overview')
    st.write("""
        The hourly data overview shows bike rentals broken down by hour, providing insights into 
        peak usage times throughout the day. This helps in understanding the demand for bikes at different hours.
    """)
    hourly_data_page = st.number_input('Select Page', min_value=1, 
                                        max_value=int(len(data_hour)/10) + 1, value=1)
    hourly_data_start = (hourly_data_page - 1) * 10
    hourly_data_end = hourly_data_start + 10
    st.write(data_hour[hourly_data_start:hourly_data_end])

    # Display the shape of the datasets for context
    st.write(f"Total Daily Records: {data_day.shape[0]}")
    st.write(f"Total Hourly Records: {data_hour.shape[0]}")
    st.write("Columns in Daily Data:", data_day.columns.tolist())
    st.write("Columns in Hourly Data:", data_hour.columns.tolist())

# Data Visualization Section
if options == "Visualizations":
    st.header("📊 Visualizations")
    st.write("""
        This section visualizes key aspects of the bike sharing dataset using various types of charts. 
        Understanding these visualizations helps to identify patterns and correlations in bike rental behavior.
    """)

    # Seasonal Effect on Bike Rentals
    st.subheader("Seasonal Effect on Rentals")
    st.write("""
        The following bar chart displays the average number of bike rentals for each season.
        It highlights seasonal trends, indicating which seasons see the most usage.
    """)
    seasonal_data = data_day.groupby('season')['cnt'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='season', y='cnt', data=seasonal_data, palette='viridis')
    plt.title("Average Bike Rentals per Season", fontsize=16)
    plt.xlabel("Season", fontsize=12)
    plt.ylabel("Average Rentals", fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Weather Impact on Rentals
    st.subheader("Weather Impact on Rentals")
    st.write("""
        This chart shows the average bike rentals based on different weather conditions. 
        It helps to understand how weather impacts bike rental behavior.
    """)
    weather_data = data_day.groupby('weathersit')['cnt'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='weathersit', y='cnt', data=weather_data, palette='coolwarm')
    plt.title("Average Bike Rentals by Weather Situation", fontsize=16)
    plt.xlabel("Weather Situation", fontsize=12)
    plt.ylabel("Average Rentals", fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # User Types Analysis
    st.subheader("User Types Analysis")
    st.write("""
        This analysis focuses on the average counts of different user types, including casual and registered users.
        Understanding user demographics is crucial for targeted marketing strategies.
    """)
    user_types_data = data_day[['casual', 'registered', 'cnt']].mean().reset_index()
    user_types_data = user_types_data.melt(id_vars='index', var_name='User Type', value_name='Count')
    plt.figure(figsize=(12, 6))
    sns.barplot(x='User Type', y='Count', data=user_types_data, palette='crest')
    plt.title("Average Count of User Types", fontsize=16)
    plt.ylabel("Average Count", fontsize=12)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Hourly Usage Pattern
    st.subheader("Hourly Usage Pattern")
    st.write("""
        This line chart illustrates the average bike rentals by hour of the day. 
        It shows peak hours for bike rentals, helping to optimize bike availability.
    """)
    hourly_usage = data_hour.groupby('hr')['cnt'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='hr', y='cnt', data=hourly_usage, marker='o', color='orange', linewidth=2)
    plt.title("Average Bike Rentals by Hour", fontsize=16)
    plt.xlabel("Hour of Day", fontsize=12)
    plt.ylabel("Average Rentals", fontsize=12)
    plt.xticks(np.arange(0, 25, step=1))
    st.pyplot(plt)

# Key Insights Section
if options == "Key Insights":
    st.header("🔑 Key Insights")
    st.write("""
        In this section, we summarize the key insights derived from the analysis of the bike sharing dataset.
        These insights can inform decision-making and strategy development.
    """)
    st.write(""" 
    - **Seasonal Influence**: The average bike rentals peak in the summer and fall seasons, indicating higher usage during warmer months.
    - **Weather Conditions**: Rentals significantly decrease during poor weather conditions, especially rain, underscoring the need for better weather forecasting and adjustments in bike availability.
    - **User Types**: Registered users contribute to approximately 60% of total rentals, emphasizing the importance of converting casual users into registered members through targeted marketing strategies.
    - **Hourly Patterns**: Peak rental hours are between 5 PM and 7 PM, suggesting that bike availability should be optimized during these times to meet user demand.
    - **Further Analysis**: Additional insights can be derived by integrating external datasets, such as public events or holidays, to assess their impact on rental patterns.
    """)

# Footer
st.sidebar.subheader("Contact")
st.sidebar.write("Project by I Komang Gede Jefri Suparjana")
st.sidebar.write("Email: jefrisuparjanaa@gmail.com")
st.sidebar.write("Dicoding ID: jefrisuparjana")

# Adding a footer for the main content
st.markdown("---")
st.write("© 2024 Jefri Suparjana. All rights reserved.")
