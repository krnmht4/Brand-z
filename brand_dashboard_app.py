
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Unified Brand Management Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1f4e79;
        margin-bottom: 30px;
    }
    .brand-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f4e79;
        margin: 10px 0;
    }
    .metric-card {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        margin: 5px;
    }
    .insight-box {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 15px;
        margin: 20px 0;
        border-radius: 5px;
    }
    .trend-item {
        background-color: #d1ecf1;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        border-left: 3px solid #17a2b8;
    }
</style>
""", unsafe_allow_html=True)

# Brand data
BRAND_DATA = {
    "SpaceXec": {
        "category": "Commercial Real Estate",
        "color": "#1f4e79",
        "social_urls": {
            "website": "https://spacexec.com/",
            "linkedin": "https://www.linkedin.com/company/spacexec/"
        },
        "metrics": {
            "website_traffic": 250000,
            "primary_social_platform": "LinkedIn",
            "social_followers": 18000,
            "engagement_rate": 2.5,
            "leads": 2100,
            "operational_metric": "New listings acquired from digital channels",
            "operational_value": 125
        },
        "trends": [
            "Hybrid work driving suburban CRE demand; urban vacancies remain elevated",
            "AI platforms streamlining search and lead gen",
            "ESG-certified spaces attracting premium tenants"
        ],
        "insight": "Strong website and LinkedIn performance indicate effective capture of suburban and flexible workspace markets"
    },
    "Aashi Realty": {
        "category": "Residential Brokerage",
        "color": "#e74c3c",
        "social_urls": {
            "website": "https://aashirealty.com/",
            "linkedin": "https://www.linkedin.com/company/aashirealty/",
            "instagram": "https://www.instagram.com/aashi_realty/",
            "facebook": "https://www.facebook.com/AashiRealty"
        },
        "metrics": {
            "website_traffic": 380000,
            "primary_social_platform": "Instagram",
            "social_followers": 45000,
            "engagement_rate": 3.1,
            "leads": 5500,
            "operational_metric": "Lead-to-appointment rate (%)",
            "operational_value": 15
        },
        "trends": [
            "Elevated interest rates influencing buyer behavior, leading to longer decision processes",
            "Inventory levels slowly increasing, shifting to more balanced market dynamics",
            "Digital tools like AI chatbots and virtual tours becoming standard for customer journey"
        ],
        "insight": "Strong social media presence and effective lead conversion are key differentiators in interest rate volatile market"
    },
    "TravelXec": {
        "category": "Online Travel Services",
        "color": "#2ecc71",
        "social_urls": {
            "website": "https://travelxec.com/",
            "linkedin": "https://www.linkedin.com/company/travelxec/",
            "instagram": "https://www.instagram.com/travel.xec/",
            "facebook": "https://www.facebook.com/people/TravelXec/61571932697689/"
        },
        "metrics": {
            "website_traffic": 1800000,
            "primary_social_platform": "TikTok",
            "social_followers": 120000,
            "engagement_rate": 4.5,
            "leads": 1800000,
            "operational_metric": "Bookings count",
            "operational_value": 320000
        },
        "trends": [
            "Consumers seeking unique, experience-driven travel rather than standardized packages",
            "AI-powered platforms providing hyper-personalized recommendations and dynamic pricing",
            "Bleisure trend combining business and leisure travel, leading to longer bookings"
        ],
        "insight": "High social engagement and website traffic directly correlate to large booking volume, capturing post-pandemic travel and bleisure markets"
    },
    "Schmooze Media": {
        "category": "Digital Marketing Agency",
        "color": "#9b59b6",
        "social_urls": {
            "website": "https://schmoozemedia.com/",
            "instagram": "https://www.instagram.com/schmoozemedia/",
            "facebook": "https://www.facebook.com/SchmoozeMedia",
            "linkedin": "https://www.linkedin.com/company/schmooze-media/"
        },
        "metrics": {
            "website_traffic": 15000,
            "primary_social_platform": "LinkedIn",
            "social_followers": 8500,
            "engagement_rate": None,
            "leads": None,
            "operational_metric": "Campaigns delivered",
            "operational_value": 450,
            "additional_metric": "Average CTR (%)",
            "additional_value": 2.1
        },
        "trends": [
            "AI revolutionizing marketing automation from content creation to campaign optimization",
            "Stricter data privacy regulations driving pivot toward contextual advertising",
            "Brands shifting investment toward micro- and nano-influencers for higher engagement"
        ],
        "insight": "High campaign volume with above-average CTR demonstrates ability to execute effective digital strategies"
    },
    "AutoXec": {
        "category": "Automotive Retail",
        "color": "#f39c12",
        "social_urls": {
            "instagram": "https://www.instagram.com/autoxec"
        },
        "metrics": {
            "website_traffic": 45000,
            "primary_social_platform": "Instagram",
            "social_followers": 32000,
            "engagement_rate": None,
            "leads": None,
            "operational_metric": "Test drives booked",
            "operational_value": 950,
            "additional_metric": "Conversion from test drive (%)",
            "additional_value": 22
        },
        "trends": [
            "EV adoption growing alongside significant rise in hybrid demand due to charging infrastructure concerns",
            "Car-buying process heavily digital with customers expecting seamless omnichannel experience",
            "Supply chain stabilization leading to normalized inventory and more competitive pricing"
        ],
        "insight": "Digital presence successfully drives high-intent leads with strong test drive bookings and conversion rates"
    }
}

def create_portfolio_overview():
    """Create portfolio overview metrics"""
    total_traffic = sum([brand["metrics"]["website_traffic"] for brand in BRAND_DATA.values()])
    total_followers = sum([brand["metrics"]["social_followers"] for brand in BRAND_DATA.values()])
    avg_engagement = sum([brand["metrics"]["engagement_rate"] for brand in BRAND_DATA.values() if brand["metrics"]["engagement_rate"]])

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Website Traffic</h3>
            <h2 style="color: #1f4e79;">{:,}</h2>
            <small>Monthly Unique Visitors</small>
        </div>
        """.format(total_traffic), unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Total Social Followers</h3>
            <h2 style="color: #e74c3c;">{:,}</h2>
            <small>Across All Platforms</small>
        </div>
        """.format(total_followers), unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Avg Engagement Rate</h3>
            <h2 style="color: #2ecc71;">{:.1f}%</h2>
            <small>Social Media Engagement</small>
        </div>
        """.format(avg_engagement/3), unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Active Brands</h3>
            <h2 style="color: #9b59b6;">{}</h2>
            <small>In Portfolio</small>
        </div>
        """.format(len(BRAND_DATA)), unsafe_allow_html=True)

def create_traffic_chart():
    """Create website traffic comparison chart"""
    brands = list(BRAND_DATA.keys())
    traffic = [BRAND_DATA[brand]["metrics"]["website_traffic"] for brand in brands]
    colors = [BRAND_DATA[brand]["color"] for brand in brands]

    fig = go.Figure(data=[
        go.Bar(
            y=brands,
            x=traffic,
            orientation='h',
            marker_color=colors,
            text=[f'{t:,}' for t in traffic],
            textposition='outside'
        )
    ])

    fig.update_layout(
        title="Website Traffic by Brand (Q3 2025)",
        xaxis_title="Monthly Unique Visitors",
        yaxis_title="Brands",
        height=400,
        showlegend=False
    )

    return fig

def create_social_engagement_chart():
    """Create social media engagement scatter plot"""
    brands = []
    followers = []
    engagement = []
    colors = []

    for brand_name, brand_data in BRAND_DATA.items():
        if brand_data["metrics"]["engagement_rate"] is not None:
            brands.append(brand_name)
            followers.append(brand_data["metrics"]["social_followers"])
            engagement.append(brand_data["metrics"]["engagement_rate"])
            colors.append(brand_data["color"])

    fig = go.Figure()

    for i, brand in enumerate(brands):
        fig.add_trace(go.Scatter(
            x=[followers[i]],
            y=[engagement[i]],
            mode='markers+text',
            text=[brand],
            textposition='top center',
            marker=dict(size=15, color=colors[i]),
            name=brand
        ))

    fig.update_layout(
        title="Social Media Performance: Followers vs Engagement Rate",
        xaxis_title="Social Media Followers",
        yaxis_title="Engagement Rate (%)",
        height=400,
        showlegend=False
    )

    return fig

def display_brand_details(brand_name):
    """Display detailed brand information"""
    brand = BRAND_DATA[brand_name]

    st.markdown(f"""
    <div class="brand-card">
        <h2 style="color: {brand['color']};">{brand_name}</h2>
        <h4>{brand['category']}</h4>
    </div>
    """, unsafe_allow_html=True)

    # Digital Footprint Section
    st.subheader("🌐 Digital Footprint")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Website Traffic", f"{brand['metrics']['website_traffic']:,}", "Monthly Visitors")

    with col2:
        st.metric("Social Followers", f"{brand['metrics']['social_followers']:,}", brand['metrics']['primary_social_platform'])

    with col3:
        if brand['metrics']['engagement_rate']:
            st.metric("Engagement Rate", f"{brand['metrics']['engagement_rate']}%", "Social Media")
        else:
            st.metric("Engagement Rate", "N/A", "Data Not Available")

    # Operational Metrics Section
    st.subheader("📈 Operational Metrics")
    col1, col2 = st.columns(2)

    with col1:
        if brand['metrics']['leads']:
            st.metric("Leads Generated", f"{brand['metrics']['leads']:,}", "Q3 2025")

    with col2:
        st.metric(brand['metrics']['operational_metric'], f"{brand['metrics']['operational_value']:,}")

    if 'additional_metric' in brand['metrics']:
        st.metric(brand['metrics']['additional_metric'], f"{brand['metrics']['additional_value']}%")

    # Market Trends Section
    st.subheader("📊 Market Trends")
    for i, trend in enumerate(brand['trends'], 1):
        st.markdown(f"""
        <div class="trend-item">
            <strong>{i}.</strong> {trend}
        </div>
        """, unsafe_allow_html=True)

    # Strategic Insight
    st.subheader("💡 Strategic Insight")
    st.markdown(f"""
    <div class="insight-box">
        <strong>Key Insight:</strong> {brand['insight']}
    </div>
    """, unsafe_allow_html=True)

    # Social Media Links
    st.subheader("🔗 Brand Links")
    links_html = ""
    for platform, url in brand['social_urls'].items():
        links_html += f'<a href="{url}" target="_blank" style="margin-right: 15px; text-decoration: none; color: {brand["color"]}; font-weight: bold;">{platform.title()}</a>'

    st.markdown(links_html, unsafe_allow_html=True)

def main():
    """Main application function"""
    # Header
    st.markdown('<h1 class="main-header">🚀 Unified Brand Management Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666; font-size: 1.2rem;">Q3 2025 Performance Overview</p>', unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Select View", ["Master Overview"] + list(BRAND_DATA.keys()))

    # Data refresh info
    st.sidebar.info("🔄 Last Updated: Aug 28, 2025, 11:40 PM IST")

    # Integration status
    st.sidebar.subheader("🔧 Integration Status")
    st.sidebar.success("✅ Data-Tracker Repository")
    st.sidebar.warning("⚠️ Social Media APIs (Setup Required)")
    st.sidebar.info("ℹ️ Notion Database (Ready for Sync)")
    st.sidebar.error("❌ Workflow Automation (Pending)")

    if page == "Master Overview":
        # Portfolio Overview
        st.header("📊 Portfolio Overview")
        create_portfolio_overview()

        st.markdown("---")

        # Charts
        col1, col2 = st.columns(2)

        with col1:
            st.plotly_chart(create_traffic_chart(), use_container_width=True)

        with col2:
            st.plotly_chart(create_social_engagement_chart(), use_container_width=True)

        st.markdown("---")

        # Brand Comparison Table
        st.header("📋 Brand Comparison")

        comparison_data = []
        for brand_name, brand_data in BRAND_DATA.items():
            comparison_data.append({
                "Brand": brand_name,
                "Category": brand_data["category"],
                "Website Traffic": f"{brand_data['metrics']['website_traffic']:,}",
                "Social Platform": brand_data["metrics"]["primary_social_platform"],
                "Followers": f"{brand_data['metrics']['social_followers']:,}",
                "Engagement Rate": f"{brand_data['metrics']['engagement_rate']}%" if brand_data['metrics']['engagement_rate'] else "N/A",
                "Operational Metric": brand_data["metrics"]["operational_value"]
            })

        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)

    else:
        # Brand-specific page
        display_brand_details(page)

        # Back to overview button
        if st.button("← Back to Master Overview"):
            st.experimental_rerun()

if __name__ == "__main__":
    main()
