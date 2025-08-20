import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import requests
from pytrends.request import TrendReq
from datetime import datetime
import random

@st.cache_data
def load_data():
    """Load the merged brand dataset without dropping any rows."""
    df = pd.read_csv("brand_selection_list.csv")
    # Keep all rows, even if Industry/Region is missing
    return df

def main():
    st.set_page_config(page_title="Megalithic Brand Intelligence", layout="wide")

    # Load your CSV
    df = load_data()
    st.sidebar.markdown(f"**Total Brands in CSV:** {len(df)}")  # Should show 80

    # Sidebar filters but default to “all” with no filtering
    st.sidebar.header("🔍 Filters")
    industries = df["Industry"].dropna().unique().tolist()
    selected_industries = st.sidebar.multiselect(
        "Industry", industries, default=industries
    )

    if "Region" in df.columns:
        regions = df["Region"].dropna().unique().tolist()
        selected_regions = st.sidebar.multiselect(
            "Region", regions, default=regions
        )
    else:
        selected_regions = None

    # Apply filters only if user changes them
    filtered_df = df.copy()
    if selected_industries:
        filtered_df = filtered_df[filtered_df["Industry"].isin(selected_industries)]
    if selected_regions:
        filtered_df = filtered_df[filtered_df["Region"].isin(selected_regions)]

    # Show count after filtering
    st.sidebar.markdown(f"**Displaying:** {len(filtered_df)} Brands")

    # Main content
    st.title("🏢 Indian Brand Intelligence Dashboard")
    st.markdown("*Comprehensive analysis of Indian brands, campaigns, and celebrity endorsements*")

    # Display table with all selected columns
    display_cols = ["Brand"]
    if "Industry" in df.columns: display_cols.append("Industry")
    if "Region" in df.columns: display_cols.append("Region")
    if "Website" in df.columns: display_cols.append("Website")

    st.subheader(f"📊 Showing {len(filtered_df)} Brands")
    st.dataframe(filtered_df[display_cols], use_container_width=True, height=400)

    # Quick Stats
    st.subheader("📈 Quick Stats")
    if not filtered_df.empty:
        counts = filtered_df["Industry"].value_counts()
        fig = px.pie(values=counts.values, names=counts.index, title="Brands by Industry")
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

        st.write("**Top Industries:**")
        for ind, cnt in counts.head(5).items():
            st.write(f"• {ind}: {cnt}")

    # Brand Deep Dive placeholder
    st.markdown("---")
    st.subheader("🔍 Brand Deep Dive")
    st.info("👆 Please select a brand above to view detailed insights.")

if __name__ == "__main__":
    main()
