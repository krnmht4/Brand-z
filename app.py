import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_csv():
    return pd.read_csv("indian_brands_comprehensive.csv")

@st.cache_data
def load_excel():
    return pd.read_excel("indian_brands_phase2_with_celebrities.xlsx")

csv_df = load_csv()
excel_df = load_excel().rename(columns={"Brand Name": "Brand", "Industry/Category": "Industry"})

# Merge datasets on Brand & Industry to keep all info
df = pd.merge(csv_df, excel_df, on=["Brand", "Industry"], how="left")

st.set_page_config(page_title="Comprehensive Brand Dashboard", layout="wide")
st.title("Comprehensive Brand Selection & Campaign Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
all_industries = df["Industry"].dropna().unique().tolist()
all_regions = df["Region"].dropna().unique().tolist()

selected_industries = st.sidebar.multiselect("Industry", options=all_industries, default=all_industries)
selected_regions = st.sidebar.multiselect("Region", options=all_regions, default=all_regions)
search_text = st.sidebar.text_input("Search Brand")

filtered = df[
    (df["Industry"].isin(selected_industries)) &
    (df["Region"].isin(selected_regions)) &
    (df["Brand"].str.contains(search_text, case=False, regex=False))
]

st.markdown(f"### {len(filtered)} Brands Found")

# Brand Table
st.dataframe(filtered[["Brand", "Industry", "Region", "Website", "Parent Company"]], use_container_width=True)

# Brand Selection
brands_available = filtered["Brand"].unique().tolist()
selected_brand = st.selectbox("Select a Brand to View Details", [""] + brands_available)

if selected_brand:
    brand_info = filtered[filtered["Brand"] == selected_brand].iloc[0]

    tabs = st.tabs(["Summary", "Social Media", "Campaigns & Celebrities", "Advertising Metrics", "Visualizations"])

    with tabs:
        st.subheader(f"{selected_brand} Summary")
        st.write(f"**Industry:** {brand_info['Industry']}")
        st.write(f"**Region:** {brand_info.get('Region', 'N/A')}")
        st.write(f"**Website:** {brand_info.get('Website', 'N/A')}")
        st.write(f"**Parent Company:** {brand_info.get('Parent Company', 'N/A')}")

    with tabs[1]:
        st.subheader("Social Media Links")
        st.write(f"Twitter: {brand_info.get('Twitter', 'N/A')}")
        st.write(f"Facebook: {brand_info.get('Facebook', 'N/A')}")
        st.write(f"Instagram: {brand_info.get('Instagram', 'N/A')}")

    with tabs:
        st.subheader("Major Campaigns (Past 5 Years)")
        st.write(brand_info.get("Major Campaigns (Past 5 Years)", "N/A"))
        st.subheader("Celebrity Endorsements")
        st.write(brand_info.get("Celebrity Endorsements", "N/A"))

    with tabs:
        st.subheader("Advertising & Media Metrics")
        st.write("Add campaign ad spend, impressions, reach data here if available.")

    with tabs:
        st.subheader("Interactive Visualizations")
        # Example plot: Brand counts per region for selected industry
        region_counts = filtered["Region"].value_counts().reset_index()
        region_counts.columns = ["Region", "Count"]
        fig = px.pie(region_counts, names='Region', values='Count', title='Brand Distribution by Region')
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Select a brand above to explore detailed information, campaigns, and analytics.")
