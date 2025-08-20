import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    """Load the merged brand dataset"""
    return pd.read_csv("brand_selection_list.csv")

# Load the data
df = load_data()

# Remove rows where Brand is NaN (if any)
df = df.dropna(subset=['Brand'])

st.title("🏢 Indian Brand Intelligence Dashboard")
st.markdown("*Comprehensive analysis of Indian brands, campaigns, and celebrity endorsements*")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Industry filter
industries = df["Industry"].dropna().unique().tolist()
selected_industries = st.sidebar.multiselect(
    "Industry", 
    industries, 
    default=industries,
    help="Select one or more industries"
)

# Region filter (if available)
if 'Region' in df.columns:
    regions = df["Region"].dropna().unique().tolist()
    selected_regions = st.sidebar.multiselect(
        "Region", 
        regions, 
        default=regions,
        help="Select one or more regions"
    )
else:
    selected_regions = ['India']  # Default if no region column

# Search brand
search_term = st.sidebar.text_input(
    "Search Brand", 
    placeholder="Type brand name...",
    help="Search for specific brand names"
)

# Apply filters
filtered_df = df.copy()

if selected_industries:
    filtered_df = filtered_df[filtered_df["Industry"].isin(selected_industries)]

if 'Region' in df.columns and selected_regions:
    filtered_df = filtered_df[filtered_df["Region"].isin(selected_regions)]

if search_term:
    filtered_df = filtered_df[
        filtered_df["Brand"].str.contains(search_term, case=False, na=False)
    ]

# Main dashboard
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📊 Showing {len(filtered_df)} Brands")
    
    # Display filtered brands
    if len(filtered_df) > 0:
        display_columns = ["Brand", "Industry"]
        if 'Region' in df.columns:
            display_columns.append("Region")
        if 'Website' in df.columns:
            display_columns.append("Website")
            
        st.dataframe(
            filtered_df[display_columns], 
            use_container_width=True,
            height=400
        )
    else:
        st.warning("No brands match your current filters.")

with col2:
    st.subheader("📈 Quick Stats")
    
    # Industry distribution
    if len(filtered_df) > 0:
        industry_counts = filtered_df['Industry'].value_counts()
        
        # Create pie chart for industry distribution
        fig = px.pie(
            values=industry_counts.values,
            names=industry_counts.index,
            title="Brands by Industry"
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
        
        # Show top industries
        st.write("**Top Industries:**")
        for industry, count in industry_counts.head(5).items():
            st.write(f"• {industry}: {count}")

# Brand selection for detailed view
st.markdown("---")
st.subheader("🔍 Brand Deep Dive")

brand_list = filtered_df["Brand"].tolist()
selected_brand = st.selectbox(
    "Select a Brand for Detailed Analysis", 
    options=[""] + brand_list,
    help="Choose a brand to see comprehensive details"
)

if selected_brand:
    brand_data = filtered_df[filtered_df["Brand"] == selected_brand].iloc[0]

    # Create tabs for different information sections
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Summary", 
        "📱 Social Media", 
        "📊 Advertising Metrics", 
        "🎬 Campaigns & Celebrities"
    ])

    with tab1:
        st.header(f"🏢 {selected_brand} - Company Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Industry:**", brand_data.get("Industry", "N/A"))
            st.write("**Parent Company:**", brand_data.get("Parent Company", "N/A"))
            
        with col2:
            if 'Region' in brand_data:
                st.write("**Region:**", brand_data.get("Region", "N/A"))
            if 'Website' in brand_data and pd.notna(brand_data.get("Website")):
                st.write("**Website:**", f"[Visit Website]({brand_data.get('Website')})")

    with tab2:
        st.header("📱 Social Media Presence")
        
        social_platforms = ['Twitter', 'Facebook', 'Instagram']
        social_links = {}
        
        for platform in social_platforms:
            if platform in brand_data and pd.notna(brand_data[platform]):
                social_links[platform] = brand_data[platform]
        
        if social_links:
            cols = st.columns(len(social_links))
            for i, (platform, link) in enumerate(social_links.items()):
                with cols[i]:
                    st.write(f"**{platform}:**")
                    st.write(f"[Follow on {platform}]({link})")
        else:
            st.info("No social media links available for this brand.")

    with tab3:
        st.header("📊 Advertising & Media Metrics")
        st.info("📍 **Coming Soon:** Ad spend, impressions, reach metrics will be added here.")
        
        # Placeholder for future metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Ad Spend", "₹X.X Cr", help="Annual advertising expenditure")
        with col2:
            st.metric("Reach", "X.X M", help="Monthly social media reach")
        with col3:
            st.metric("Campaigns", "XX", help="Active campaigns this year")

    with tab4:
        st.header("🎬 Marketing Campaigns & Celebrity Endorsements")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📢 Major Campaigns")
            campaigns = brand_data.get("Major Campaigns (Past 5 Years)", "N/A")
            if campaigns and campaigns != "N/A":
                st.write(campaigns)
            else:
                st.info("No recent campaign information available.")
        
        with col2:
            st.subheader("⭐ Celebrity Endorsements")
            endorsements = brand_data.get("Celebrity Endorsements", "N/A")
            if endorsements and endorsements != "N/A":
                # Split multiple celebrities and display as list
                if ";" in endorsements or "," in endorsements:
                    celebrities = endorsements.replace(";", ",").split(",")
                    for celeb in celebrities:
                        st.write(f"• {celeb.strip()}")
                else:
                    st.write(f"• {endorsements}")
            else:
                st.info("No celebrity endorsements information available.")

else:
    st.info("👆 Please select a brand from the dropdown above to view detailed insights.")

# Footer
st.markdown("---")
st.markdown("**Indian Brand Intelligence Dashboard** | Built with Streamlit")