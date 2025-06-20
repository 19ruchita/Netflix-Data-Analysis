import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Setup
st.set_page_config(page_title="Netflix Data Analysis", layout="wide")
st.title("📺 Netflix Data Analytics Dashboard")

# Load Data
data = pd.read_csv("Netflix Dataset.csv")
data['Date_N'] = pd.to_datetime(data['Release_Date'], errors='coerce')
data['Year'] = data['Date_N'].dt.year
data.drop_duplicates(inplace=True)

st.sidebar.header("🎯 Filters")

min_date = data['Date_N'].min()
max_date = data['Date_N'].max()

date_range = st.sidebar.date_input("📅 Select Release Date Range", [min_date, max_date])

if len(date_range) == 2:
    data = data[(data['Date_N'] >= pd.to_datetime(date_range[0])) & 
                (data['Date_N'] <= pd.to_datetime(date_range[1]))]


# Sidebar Filters
with st.sidebar:
    st.header("🔍 Filter Options")
    category = st.multiselect("Category", options=data['Category'].dropna().unique(), default=data['Category'].dropna().unique())
    country = st.multiselect("Country", options=data['Country'].dropna().unique(), default=data['Country'].dropna().unique()[:5])
    year_range = st.slider("Release Year Range", int(data['Year'].min()), int(data['Year'].max()), (2010, 2020))

search_term = st.text_input("🔎 Search by Title")
if search_term:
    filtered = filtered[filtered['Title'].str.contains(search_term, case=False, na=False)]


# Apply Filters
filtered = data[
    (data['Category'].isin(category)) &
    (data['Country'].isin(country)) &
    (data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])
]
csv = filtered.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_netflix_data.csv',
    mime='text/csv',
)


# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Titles", len(filtered))
col2.metric("Countries", filtered['Country'].nunique())
col3.metric("Years", filtered['Year'].nunique())

# Category Distribution
st.subheader("📊 Distribution by Category")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered, x='Category', palette='Set2', ax=ax1)
st.pyplot(fig1)

# Release Year Trend
st.subheader("📈 Releases Over Years")
year_trend = filtered['Year'].value_counts().sort_index()
fig2, ax2 = plt.subplots()
year_trend.plot(kind='bar', ax=ax2, color='lightgreen')
ax2.set_ylabel("Number of Releases")
st.pyplot(fig2)

# Top Directors
st.subheader("🎬 Top 10 Directors")
top_directors = filtered['Director'].value_counts().head(10)
fig3, ax3 = plt.subplots()
sns.barplot(y=top_directors.index, x=top_directors.values, ax=ax3, palette="coolwarm")
ax3.set_xlabel("Number of Titles")
st.pyplot(fig3)

st.subheader("🎬 Top Directors on Netflix")

top_n = st.slider("Select number of top directors to display", min_value=5, max_value=20, value=10)

top_directors = data['Director'].value_counts().dropna().head(top_n)

st.bar_chart(top_directors)


# 🔍 Custom Analysis
st.subheader("🔎 Custom Insights")

with st.expander("House of Cards Info"):
    hoc = data[data['Title'].str.contains('House of Cards', na=False)]
    st.dataframe(hoc[['Title', 'Show_Id', 'Director']])

with st.expander("Highest Number of Titles by Year"):
    st.bar_chart(data['Year'].value_counts().sort_index())

with st.expander("Movies Released in 2000"):
    st.dataframe(data[(data['Category'] == 'Movie') & (data['Year'] == 2000)][['Title', 'Director']])

with st.expander("TV Shows from India"):
    st.dataframe(data[(data['Category'] == 'TV Show') & (data['Country'] == 'India')][['Title', 'Director']])

import plotly.express as px

st.subheader("🌍 Netflix Content Distribution by Country")

country_counts = data['Country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']

fig = px.choropleth(country_counts, 
                    locations='Country',
                    locationmode='country names',
                    color='Count',
                    title='Netflix Content by Country',
                    color_continuous_scale='reds')

st.plotly_chart(fig)


with st.expander("Tom Cruise Movies/Shows"):
    tom_cruise = data.dropna(subset=['Cast'])
    tom_cruise = tom_cruise[tom_cruise['Cast'].str.contains('Tom Cruise')]
    st.dataframe(tom_cruise[['Title', 'Cast', 'Director']])

with st.expander("Max Duration Movie/Show"):
    data[['Minutes', 'Unit']] = data['Duration'].str.split(' ', expand=True)
    st.write("Max Duration:", data['Minutes'].dropna().astype('int').max(), "minutes")

st.subheader("🎯 Ratings Distribution")
rating_counts = filtered['Rating'].value_counts()
fig4, ax4 = plt.subplots()
ax4.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=140)
ax4.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig4)


# Data Preview
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered[['Title', 'Category', 'Country', 'Release_Date', 'Rating', 'Duration']])


