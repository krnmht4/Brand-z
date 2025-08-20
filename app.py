import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Comprehensive Brand Dashboard", layout="wide")

@st.cache_data
def load_data():
    # Load merged CSV you’ll place beside this script
    return pd.read_csv("indian_brands_merged_full.csv")

df = load_data()

st.title("Comprehensive Brand Selection & Campaign Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
industries = sorted(df["Industry"].dropna().unique())
regions    = sorted(df["Region"].dropna().unique())

selected_industries = st.sidebar.multiselect("Industry", options=industries, default=industries)
selected_regions    = st.sidebar.multiselect("Region",   options=regions,    default=regions)
search_term         = st.sidebar.text_input("Search Brand")

# Filter brands
filtered = df[
    df["Industry"].isin(selected_industries) &
    df["Region"].isin(selected_regions) &
    df["Brand"].str.contains(search_term, case=False, na=False)
]

st.markdown(f"### {len(filtered)} Brands Found")
st.dataframe(
    filtered[["Brand","Industry","Region","Website","Parent Company"]],
    use_container_width=True
)

# Brand detail selector
selected = st.selectbox("Select a Brand for Details", [""] + filtered["Brand"].tolist())
if selected:
    info = filtered[filtered["Brand"] == selected].iloc[0]
    tabs = st.tabs([
        "Summary",
        "Social Media",
        "Campaigns & Celebrities",
        "Advertising Metrics",
        "Visualizations"
    ])

    with tabs[0]:
        st.subheader(f"{selected} — Summary")
        st.write(f"**Industry:** {info['Industry']}")
        st.write(f"**Region:** {info.get('Region','N/A')}")
        st.write(f"**Website:** {info.get('Website','N/A')}")
        st.write(f"**Parent Company:** {info.get('Parent Company','N/A')}")

    with tabs[1]:
        st.subheader("Social Media Links")
        st.write(f"Twitter: {info.get('Twitter','N/A')}")
        st.write(f"Facebook: {info.get('Facebook','N/A')}")
        st.write(f"Instagram: {info.get('Instagram','N/A')}")

    with tabs[2]:
        st.subheader("Major Campaigns (Past 5 Years)")
        st.write(info.get("Major Campaigns (Past 5 Years)","N/A"))
        st.subheader("Celebrity Endorsements")
        st.write(info.get("Celebrity Endorsements","N/A"))

    with tabs[3]:
        st.subheader("Advertising & Media Metrics")
        st.write("Placeholder—add ad spend, impressions, reach, etc.")

    with tabs[4]:
        st.subheader("Brand Distribution by Region")
        counts = filtered["Region"].value_counts().reset_index()
        counts.columns = ["Region","Count"]
        fig = px.pie(counts, names="Region", values="Count")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Select a brand above to view its details.")
