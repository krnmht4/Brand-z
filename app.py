import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV data
@st.cache_data
def load_data():
    return pd.read_csv("brand_selection_list.csv")

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
industries = df["Industry"].unique().tolist()
regions = df["Region"].unique().tolist()

selected_industries = st.sidebar.multiselect("Industry", industries, default=industries)
selected_regions    = st.sidebar.multiselect("Region", regions, default=regions)
search_brand        = st.sidebar.text_input("Search Brand")

# Filter dataframe
mask = (
    df["Industry"].isin(selected_industries) &
    df["Region"].isin(selected_regions) &
    df["Brand"].str.contains(search_brand, case=False, regex=False)
)
filtered = df[mask]

# Main layout
st.title("Brand Selection Dashboard")
st.markdown("Filter and explore brands by Industry and Region.")

# Summary cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Brands", len(filtered))
col2.metric("Industries", filtered["Industry"].nunique())
col3.metric("Regions",  filtered["Region"].nunique())

# Table view
st.subheader("Filtered Brands")
st.dataframe(filtered.reset_index(drop=True), use_container_width=True)

# Bar chart: brands per industry
st.subheader("Brands by Industry")
fig1 = px.bar(
    filtered.groupby("Industry").size().reset_index(name="Count"),
    x="Industry", y="Count",
    color="Count",
    labels={"Count":"# Brands"},
    title="Brands per Industry"
)
st.plotly_chart(fig1, use_container_width=True)

# Pie chart: region distribution
st.subheader("Region Distribution")
fig2 = px.pie(
    filtered["Region"].value_counts().reset_index().rename(columns={"index":"Region","Region":"Count"}),
    names="Region", values="Count",
    title="Global vs India Brands"
)
st.plotly_chart(fig2, use_container_width=True)
