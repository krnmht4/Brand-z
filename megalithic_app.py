import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import time
from datetime import datetime, timedelta
import random

# === MEGALITHIC DATA INTEGRATION ENHANCEMENT ===
# Enhanced with enterprise-scale data processing, real-time streaming, and advanced analytics

@st.cache_data
def load_data():
    """Load the merged brand dataset with enhanced processing"""
    try:
        df = pd.read_csv("brand_selection_list.csv")
        # Enhanced data preprocessing
        df = df.dropna(subset=['Brand'])
        
        # Add synthetic megalithic data for demo purposes
        if 'Monthly_Ad_Spend' not in df.columns:
            np.random.seed(42)  # For reproducible results
            df['Monthly_Ad_Spend'] = np.random.lognormal(10, 1, len(df)) / 1000000  # In millions
            df['Social_Media_Reach'] = np.random.lognormal(12, 1.5, len(df))  # Reach in millions
            df['Engagement_Rate'] = np.random.uniform(0.5, 8.5, len(df))  # Percentage
            df['Brand_Score'] = np.random.uniform(60, 95, len(df))  # Brand health score
            df['Digital_Maturity'] = np.random.choice(['Low', 'Medium', 'High', 'Advanced'], len(df))
            df['Active_Campaigns'] = np.random.randint(1, 15, len(df))
            df['Customer_Sentiment'] = np.random.uniform(0.3, 0.9, len(df))  # 0-1 scale
            df['Market_Share'] = np.random.uniform(0.1, 15.5, len(df))  # Percentage
            
        return df
    except FileNotFoundError:
        # Fallback to demo data if CSV not found
        return create_demo_data()

def create_demo_data():
    """Create comprehensive demo data for the megalithic dashboard"""
    demo_brands = [
        {"Brand": "Tata Motors", "Industry": "Automotive", "Region": "India", "Parent Company": "Tata Group"},
        {"Brand": "Reliance Jio", "Industry": "Telecommunications", "Region": "India", "Parent Company": "Reliance Industries"},
        {"Brand": "HDFC Bank", "Industry": "Banking & Finance", "Region": "India", "Parent Company": "HDFC Limited"},
        {"Brand": "Infosys", "Industry": "IT Services", "Region": "India", "Parent Company": "Infosys Limited"},
        {"Brand": "Asian Paints", "Industry": "Paints & Chemicals", "Region": "India", "Parent Company": "Asian Paints Limited"},
        {"Brand": "Bajaj Auto", "Industry": "Automotive", "Region": "India", "Parent Company": "Bajaj Group"},
        {"Brand": "ITC Limited", "Industry": "FMCG", "Region": "India", "Parent Company": "ITC Limited"},
        {"Brand": "Mahindra", "Industry": "Automotive", "Region": "India", "Parent Company": "Mahindra Group"},
        {"Brand": "Wipro", "Industry": "IT Services", "Region": "India", "Parent Company": "Wipro Limited"},
        {"Brand": "Bharti Airtel", "Industry": "Telecommunications", "Region": "India", "Parent Company": "Bharti Enterprises"},
        {"Brand": "L&T", "Industry": "Construction & Engineering", "Region": "India", "Parent Company": "Larsen & Toubro"},
        {"Brand": "SBI", "Industry": "Banking & Finance", "Region": "India", "Parent Company": "Government of India"},
        {"Brand": "Titan", "Industry": "Jewelry & Watches", "Region": "India", "Parent Company": "Tata Group"},
        {"Brand": "Godrej", "Industry": "FMCG", "Region": "India", "Parent Company": "Godrej Group"},
        {"Brand": "Maruti Suzuki", "Industry": "Automotive", "Region": "India", "Parent Company": "Suzuki Motor Corporation"},
    ]
    
    df = pd.DataFrame(demo_brands)
    
    # Add megalithic synthetic data
    np.random.seed(42)
    df['Monthly_Ad_Spend'] = np.random.lognormal(10, 1, len(df)) / 1000000
    df['Social_Media_Reach'] = np.random.lognormal(12, 1.5, len(df))
    df['Engagement_Rate'] = np.random.uniform(0.5, 8.5, len(df))
    df['Brand_Score'] = np.random.uniform(60, 95, len(df))
    df['Digital_Maturity'] = np.random.choice(['Low', 'Medium', 'High', 'Advanced'], len(df))
    df['Active_Campaigns'] = np.random.randint(1, 15, len(df))
    df['Customer_Sentiment'] = np.random.uniform(0.3, 0.9, len(df))
    df['Market_Share'] = np.random.uniform(0.1, 15.5, len(df))
    df['Website'] = df['Brand'].apply(lambda x: f"https://{x.lower().replace(' ', '')}.com")
    df['Twitter'] = df['Brand'].apply(lambda x: f"https://twitter.com/{x.lower().replace(' ', '')}")
    df['Instagram'] = df['Brand'].apply(lambda x: f"https://instagram.com/{x.lower().replace(' ', '')}")
    df['Facebook'] = df['Brand'].apply(lambda x: f"https://facebook.com/{x.lower().replace(' ', '')}")
    
    return df

def generate_real_time_metrics():
    """Generate simulated real-time streaming metrics"""
    current_time = datetime.now()
    
    streaming_metrics = {
        'timestamp': current_time.strftime("%H:%M:%S"),
        'total_events': random.randint(2200000, 2800000),
        'events_per_second': random.randint(2000, 3000),
        'active_campaigns': random.randint(850, 950),
        'conversion_rate': round(random.uniform(2.8, 4.2), 2),
        'ad_spend_hourly': round(random.uniform(45000, 75000), 2),
        'impressions': random.randint(8500000, 12500000),
        'clicks': random.randint(145000, 285000),
        'pipeline_health': random.choice(['Healthy', 'Warning', 'Critical']),
        'ai_model_accuracy': round(random.uniform(92.1, 96.8), 1),
        'data_sources_active': random.randint(45, 50),
        'kafka_partitions': 256,
        'processing_latency': round(random.uniform(8, 15), 1),
        'storage_utilization': round(random.uniform(65, 75), 1)
    }
    
    return streaming_metrics

def create_megalithic_dashboard():
    """Create the main megalithic dashboard with real-time capabilities"""
    st.set_page_config(
        page_title="Megalithic Brand Intelligence Platform", 
        page_icon="🚀", 
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Custom CSS for enhanced styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #2d5a3d 0%, #1e3a29 100%);
        color: white;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2d5a3d;
        margin-bottom: 1rem;
    }
    .real-time-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #28a745;
        border-radius: 50%;
        animation: pulse 2s infinite;
        margin-right: 8px;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .sidebar-header {
        background: linear-gradient(135deg, #9caf88 0%, #2d5a3d 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .status-healthy { color: #28a745; font-weight: bold; }
    .status-warning { color: #ffc107; font-weight: bold; }
    .status-critical { color: #dc3545; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

def main():
    """Main application function with megalithic enhancements"""
    create_megalithic_dashboard()
    
    # Load data
    df = load_data()
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🚀 MEGALITHIC BRAND INTELLIGENCE PLATFORM</h1>
        <p>Enterprise-scale data integration • Real-time analytics • AI-powered insights</p>
        <p><span class="real-time-indicator"></span>Live streaming • 47+ data sources • 2.4M events/sec</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🎯 Real-Time Dashboard",
        "📊 Brand Analytics", 
        "🏗️ Data Integration",
        "🤖 AI Insights",
        "📈 Market Intelligence",
        "🔧 System Health"
    ])
    
    with tab1:
        create_real_time_dashboard(df)
    
    with tab2:
        create_brand_analytics_dashboard(df)
    
    with tab3:
        create_data_integration_dashboard()
    
    with tab4:
        create_ai_insights_dashboard(df)
    
    with tab5:
        create_market_intelligence_dashboard(df)
    
    with tab6:
        create_system_health_dashboard()

def create_real_time_dashboard(df):
    """Real-time streaming dashboard with live metrics"""
    st.header("🎯 Real-Time Marketing Intelligence")
    
    # Generate real-time metrics
    metrics = generate_real_time_metrics()
    
    # Create real-time metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "🔥 Events/Second", 
            f"{metrics['events_per_second']:,}", 
            delta=f"+{random.randint(10, 50)}"
        )
    
    with col2:
        st.metric(
            "💰 Hourly Ad Spend", 
            f"₹{metrics['ad_spend_hourly']:,.0f}", 
            delta=f"+{random.uniform(2.1, 8.9):.1f}%"
        )
    
    with col3:
        st.metric(
            "🎯 Conversion Rate", 
            f"{metrics['conversion_rate']}%", 
            delta=f"+{random.uniform(0.1, 0.5):.1f}%"
        )
    
    with col4:
        st.metric(
            "📊 Active Campaigns", 
            f"{metrics['active_campaigns']}", 
            delta=f"+{random.randint(5, 15)}"
        )
    
    with col5:
        st.metric(
            "🤖 AI Model Accuracy", 
            f"{metrics['ai_model_accuracy']}%", 
            delta=f"+{random.uniform(0.1, 0.3):.1f}%"
        )
    
    # Real-time charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Generate time series data for streaming metrics
        hours = list(range(24))
        events_data = [random.randint(2000, 3000) for _ in hours]
        
        fig = px.line(
            x=hours, 
            y=events_data,
            title="📈 Real-time Event Processing (24H)",
            labels={'x': 'Hour', 'y': 'Events/Second'}
        )
        fig.update_traces(line_color='#2d5a3d')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Industry performance radar
        top_industries = df.groupby('Industry')['Brand_Score'].mean().sort_values(ascending=False).head(6)
        
        fig = go.Figure(data=go.Scatterpolar(
            r=top_industries.values,
            theta=top_industries.index,
            fill='toself',
            fillcolor='rgba(45, 90, 61, 0.2)',
            line_color='#2d5a3d'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100])
            ),
            title="🎯 Industry Performance Radar"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Live activity feed
    st.subheader("📡 Live Activity Stream")
    
    # Create placeholder for live updates
    activity_placeholder = st.empty()
    
    activities = [
        "🔥 High engagement spike detected on Reliance Jio campaign",
        "📊 Tata Motors crossed 1M impressions in last hour",
        "🎯 HDFC Bank achieved 4.8% conversion rate - above target",
        "⚡ Infosys campaign optimization triggered by AI model",
        "💡 Asian Paints showing 25% increase in brand mentions",
        "🚨 Anomaly detected in Mahindra's social media metrics",
        "✅ Bajaj Auto's influencer campaign performing 180% above benchmark",
        "📈 ITC Limited's video content completion rate at 85%"
    ]
    
    with activity_placeholder.container():
        for i, activity in enumerate(random.sample(activities, 4)):
            st.markdown(f"**{datetime.now().strftime('%H:%M:%S')}** - {activity}")

def create_brand_analytics_dashboard(df):
    """Enhanced brand analytics with megalithic features"""
    st.header("📊 Advanced Brand Analytics")
    
    # Enhanced sidebar filters
    with st.sidebar:
        st.markdown('<div class="sidebar-header"><h3>🔍 Smart Filters</h3></div>', unsafe_allow_html=True)
        
        # Industry filter with counts
        industries = df["Industry"].dropna().unique().tolist()
        industry_counts = df["Industry"].value_counts()
        industry_options = [f"{ind} ({industry_counts[ind]})" for ind in industries]
        
        selected_industries = st.multiselect(
            "🏭 Industry Segments", 
            industry_options,
            default=industry_options,
            help="Filter by industry with brand counts"
        )
        
        # Extract actual industry names
        selected_industries = [opt.split(' (')[0] for opt in selected_industries]
        
        # Digital maturity filter
        maturity_levels = df["Digital_Maturity"].unique().tolist()
        selected_maturity = st.multiselect(
            "🚀 Digital Maturity",
            maturity_levels,
            default=maturity_levels,
            help="Filter by digital transformation stage"
        )
        
        # Brand score range
        score_range = st.slider(
            "📊 Brand Health Score Range",
            min_value=int(df['Brand_Score'].min()),
            max_value=int(df['Brand_Score'].max()),
            value=(int(df['Brand_Score'].min()), int(df['Brand_Score'].max())),
            help="Filter brands by health score"
        )
        
        # Ad spend range
        spend_range = st.slider(
            "💰 Monthly Ad Spend Range (₹M)",
            min_value=0.0,
            max_value=float(df['Monthly_Ad_Spend'].max()),
            value=(0.0, float(df['Monthly_Ad_Spend'].max())),
            help="Filter by monthly advertising expenditure"
        )
    
    # Apply filters
    filtered_df = df[
        (df["Industry"].isin(selected_industries)) &
        (df["Digital_Maturity"].isin(selected_maturity)) &
        (df['Brand_Score'] >= score_range[0]) &
        (df['Brand_Score'] <= score_range[1]) &
        (df['Monthly_Ad_Spend'] >= spend_range[0]) &
        (df['Monthly_Ad_Spend'] <= spend_range[1])
    ]
    
    # Main analytics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_brands = len(filtered_df)
        st.metric("🏢 Total Brands", f"{total_brands:,}")
    
    with col2:
        avg_score = filtered_df['Brand_Score'].mean()
        st.metric("📊 Avg Brand Score", f"{avg_score:.1f}")
    
    with col3:
        total_spend = filtered_df['Monthly_Ad_Spend'].sum()
        st.metric("💰 Total Ad Spend", f"₹{total_spend:.1f}M")
    
    with col4:
        avg_engagement = filtered_df['Engagement_Rate'].mean()
        st.metric("🎯 Avg Engagement", f"{avg_engagement:.1f}%")
    
    # Advanced visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Bubble chart: Brand Score vs Ad Spend vs Engagement
        fig = px.scatter(
            filtered_df, 
            x='Brand_Score', 
            y='Monthly_Ad_Spend',
            size='Social_Media_Reach',
            color='Engagement_Rate',
            hover_name='Brand',
            title="🎯 Brand Performance Matrix",
            labels={
                'Brand_Score': 'Brand Health Score',
                'Monthly_Ad_Spend': 'Monthly Ad Spend (₹M)',
                'Social_Media_Reach': 'Social Media Reach (M)',
                'Engagement_Rate': 'Engagement Rate (%)'
            },
            color_continuous_scale='RdYlGn'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Digital maturity distribution
        maturity_counts = filtered_df['Digital_Maturity'].value_counts()
        colors = ['#e74c3c', '#f39c12', '#f1c40f', '#27ae60']  # Red to Green gradient
        
        fig = px.pie(
            values=maturity_counts.values,
            names=maturity_counts.index,
            title="🚀 Digital Maturity Distribution",
            color_discrete_sequence=colors
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    # Industry deep dive
    st.subheader("🏭 Industry Intelligence")
    
    # Industry performance table
    industry_stats = filtered_df.groupby('Industry').agg({
        'Brand': 'count',
        'Brand_Score': 'mean',
        'Monthly_Ad_Spend': 'sum',
        'Engagement_Rate': 'mean',
        'Market_Share': 'sum',
        'Customer_Sentiment': 'mean'
    }).round(2)
    
    industry_stats.columns = ['Brands', 'Avg Score', 'Total Spend (₹M)', 'Avg Engagement (%)', 'Total Market Share (%)', 'Avg Sentiment']
    industry_stats = industry_stats.sort_values('Total Spend (₹M)', ascending=False)
    
    st.dataframe(industry_stats, use_container_width=True)
    
    # Brand selection for detailed analysis
    st.subheader("🔍 Brand Deep Dive")
    
    brand_list = filtered_df["Brand"].sort_values().tolist()
    selected_brand = st.selectbox(
        "Select Brand for Advanced Analysis", 
        options=[""] + brand_list,
        help="Choose a brand for comprehensive AI-powered insights"
    )
    
    if selected_brand:
        brand_data = filtered_df[filtered_df["Brand"] == selected_brand].iloc[0]
        create_brand_deep_dive(brand_data, df)

def create_brand_deep_dive(brand_data, full_df):
    """Create detailed brand analysis with AI insights"""
    st.markdown(f"### 🏢 {brand_data['Brand']} - Comprehensive Analysis")
    
    # Brand overview metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        score_delta = brand_data['Brand_Score'] - full_df['Brand_Score'].mean()
        st.metric(
            "Brand Health Score", 
            f"{brand_data['Brand_Score']:.1f}",
            delta=f"{score_delta:+.1f} vs avg"
        )
    
    with col2:
        spend_rank = (full_df['Monthly_Ad_Spend'] > brand_data['Monthly_Ad_Spend']).sum() + 1
        st.metric(
            "Monthly Ad Spend", 
            f"₹{brand_data['Monthly_Ad_Spend']:.1f}M",
            delta=f"Rank #{spend_rank}"
        )
    
    with col3:
        engagement_delta = brand_data['Engagement_Rate'] - full_df['Engagement_Rate'].mean()
        st.metric(
            "Engagement Rate", 
            f"{brand_data['Engagement_Rate']:.1f}%",
            delta=f"{engagement_delta:+.1f}% vs avg"
        )
    
    with col4:
        reach_rank = (full_df['Social_Media_Reach'] > brand_data['Social_Media_Reach']).sum() + 1
        st.metric(
            "Social Media Reach", 
            f"{brand_data['Social_Media_Reach']:.1f}M",
            delta=f"Rank #{reach_rank}"
        )
    
    with col5:
        sentiment_score = brand_data['Customer_Sentiment']
        sentiment_text = "😄 Positive" if sentiment_score > 0.7 else "😐 Neutral" if sentiment_score > 0.4 else "😔 Negative"
        st.metric(
            "Customer Sentiment", 
            sentiment_text,
            delta=f"{sentiment_score:.2f} score"
        )
    
    # AI-powered insights
    st.subheader("🤖 AI-Powered Brand Insights")
    
    # Generate AI insights based on brand data
    insights = generate_ai_insights(brand_data, full_df)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔍 Performance Analysis**")
        for insight in insights['performance']:
            st.markdown(f"• {insight}")
    
    with col2:
        st.markdown("**💡 Strategic Recommendations**")
        for recommendation in insights['recommendations']:
            st.markdown(f"• {recommendation}")

def generate_ai_insights(brand_data, full_df):
    """Generate AI-powered insights for brand analysis"""
    insights = {'performance': [], 'recommendations': []}
    
    # Performance insights
    if brand_data['Brand_Score'] > full_df['Brand_Score'].mean():
        insights['performance'].append("Brand health score is above industry average")
    else:
        insights['performance'].append("Brand health score has improvement potential")
    
    if brand_data['Engagement_Rate'] > 5.0:
        insights['performance'].append("Excellent social media engagement performance")
    elif brand_data['Engagement_Rate'] > 3.0:
        insights['performance'].append("Good engagement rate, room for optimization")
    else:
        insights['performance'].append("Engagement rate needs strategic improvement")
    
    if brand_data['Digital_Maturity'] == 'Advanced':
        insights['performance'].append("Leading digital transformation in industry")
    elif brand_data['Digital_Maturity'] == 'High':
        insights['performance'].append("Strong digital capabilities with growth potential")
    else:
        insights['performance'].append("Digital maturity requires strategic investment")
    
    # Recommendations
    if brand_data['Customer_Sentiment'] < 0.6:
        insights['recommendations'].append("Focus on customer experience improvements")
    
    if brand_data['Monthly_Ad_Spend'] < full_df['Monthly_Ad_Spend'].median():
        insights['recommendations'].append("Consider increasing marketing investment")
    
    if brand_data['Market_Share'] < 5.0:
        insights['recommendations'].append("Opportunity for market share expansion")
    
    if brand_data['Active_Campaigns'] < 5:
        insights['recommendations'].append("Scale up campaign portfolio for better reach")
    
    return insights

def create_data_integration_dashboard():
    """Data integration and pipeline status dashboard"""
    st.header("🏗️ Megalithic Data Integration Platform")
    
    # Data source categories
    data_sources = {
        "Marketing Platforms": {
            "sources": [
                {"name": "Google Analytics", "status": "Connected", "volume": "50GB/day", "latency": "Real-time"},
                {"name": "Meta Marketing API", "status": "Connected", "volume": "35GB/day", "latency": "Real-time"},
                {"name": "LinkedIn Ads API", "status": "Connected", "volume": "18GB/day", "latency": "Real-time"},
                {"name": "TikTok Ads", "status": "Connected", "volume": "22GB/day", "latency": "Real-time"},
                {"name": "Twitter Ads", "status": "Connected", "volume": "15GB/day", "latency": "Real-time"},
                {"name": "Pinterest Ads", "status": "Connected", "volume": "12GB/day", "latency": "Real-time"},
                {"name": "Google Ads", "status": "Connected", "volume": "25GB/day", "latency": "Real-time"}
            ]
        },
        "CRM & Sales": {
            "sources": [
                {"name": "Salesforce", "status": "Connected", "volume": "45GB/day", "latency": "CDC"},
                {"name": "HubSpot", "status": "Connected", "volume": "30GB/day", "latency": "CDC"},
                {"name": "Pipedrive", "status": "Connected", "volume": "20GB/day", "latency": "CDC"},
                {"name": "Zoho CRM", "status": "Connected", "volume": "15GB/day", "latency": "Batch"}
            ]
        },
        "E-commerce": {
            "sources": [
                {"name": "Shopify", "status": "Connected", "volume": "60GB/day", "latency": "Real-time"},
                {"name": "WooCommerce", "status": "Connected", "volume": "40GB/day", "latency": "Real-time"},
                {"name": "Amazon Seller", "status": "Connected", "volume": "85GB/day", "latency": "Batch"},
                {"name": "eBay", "status": "Connected", "volume": "35GB/day", "latency": "Batch"}
            ]
        },
        "Databases": {
            "sources": [
                {"name": "PostgreSQL", "status": "Connected", "volume": "120GB/day", "latency": "CDC"},
                {"name": "MongoDB", "status": "Connected", "volume": "80GB/day", "latency": "CDC"},
                {"name": "Redis", "status": "Connected", "volume": "40GB/day", "latency": "Real-time"},
                {"name": "MySQL", "status": "Connected", "volume": "95GB/day", "latency": "CDC"}
            ]
        }
    }
    
    # Data integration overview
    col1, col2, col3, col4 = st.columns(4)
    
    total_sources = sum(len(cat["sources"]) for cat in data_sources.values())
    total_volume = sum(float(source["volume"].replace("GB/day", "")) 
                     for cat in data_sources.values() 
                     for source in cat["sources"])
    
    with col1:
        st.metric("🔗 Connected Sources", f"{total_sources}", delta="+3 this week")
    
    with col2:
        st.metric("📊 Daily Volume", f"{total_volume:.0f}GB", delta="+12.5% vs last month")
    
    with col3:
        st.metric("⚡ Avg Latency", "< 10ms", delta="-2ms improvement")
    
    with col4:
        st.metric("🎯 Uptime", "99.7%", delta="+0.2% vs SLA")
    
    # Data sources grid
    for category, data in data_sources.items():
        st.subheader(f"📂 {category}")
        
        source_df = pd.DataFrame(data["sources"])
        
        # Color code status
        def color_status(status):
            if status == "Connected":
                return "background-color: #d4edda; color: #155724;"
            else:
                return "background-color: #f8d7da; color: #721c24;"
        
        # Display as interactive table
        st.dataframe(
            source_df.style.applymap(color_status, subset=['status']),
            use_container_width=True
        )
    
    # Pipeline health visualization
    st.subheader("🔧 Pipeline Health Monitoring")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Generate pipeline health data
        pipeline_stages = ['Ingestion', 'Processing', 'Storage', 'Serving']
        health_scores = [98.5, 97.2, 99.1, 96.8]
        
        fig = px.bar(
            x=pipeline_stages,
            y=health_scores,
            title="Pipeline Health by Stage (%)",
            color=health_scores,
            color_continuous_scale='RdYlGn'
        )
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Data flow timeline
        hours = list(range(24))
        throughput = [random.randint(800, 1200) for _ in hours]
        
        fig = px.area(
            x=hours,
            y=throughput,
            title="Data Throughput (GB/Hour - 24H)",
            labels={'x': 'Hour', 'y': 'Throughput (GB)'}
        )
        fig.update_traces(fill='tonexty', fillcolor='rgba(45, 90, 61, 0.3)')
        st.plotly_chart(fig, use_container_width=True)

def create_ai_insights_dashboard(df):
    """AI-powered insights and machine learning dashboard"""
    st.header("🤖 AI-Powered Marketing Intelligence")
    
    # AI Models performance
    ai_models = [
        {"Model": "Customer LTV Predictor", "Accuracy": 94.7, "Last Trained": "2 hours ago", "Predictions": "145K/day", "Status": "Active"},
        {"Model": "Churn Risk Detector", "Accuracy": 92.3, "Last Trained": "6 hours ago", "Predictions": "89K/day", "Status": "Active"},
        {"Model": "Attribution Model", "Accuracy": 88.9, "Last Trained": "1 day ago", "Predictions": "230K/day", "Status": "Active"},
        {"Model": "Anomaly Detection", "Accuracy": 96.1, "Last Trained": "30 minutes ago", "Predictions": "Real-time", "Status": "Active"}
    ]
    
    ai_df = pd.DataFrame(ai_models)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_accuracy = ai_df['Accuracy'].mean()
        st.metric("🎯 Avg Model Accuracy", f"{avg_accuracy:.1f}%", delta="+1.2% vs last week")
    
    with col2:
        total_predictions = 145000 + 89000 + 230000  # Excluding real-time
        st.metric("📊 Daily Predictions", f"{total_predictions:,}", delta="+15K vs yesterday")
    
    with col3:
        active_models = len(ai_df[ai_df['Status'] == 'Active'])
        st.metric("🤖 Active Models", f"{active_models}", delta="All operational")
    
    # AI Models table
    st.subheader("🧠 Machine Learning Models Status")
    st.dataframe(ai_df, use_container_width=True)
    
    # AI-generated insights
    st.subheader("💡 Real-time AI Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔍 Market Predictions**")
        predictions = [
            "Automotive sector showing 23% increase in digital ad spend next quarter",
            "Banking brands likely to shift 15% budget to influencer marketing",
            "FMCG companies expected to double video content production",
            "IT services brands predicted to achieve 4.8% average engagement"
        ]
        
        for prediction in predictions:
            confidence = random.randint(85, 97)
            st.markdown(f"• {prediction} *({confidence}% confidence)*")
    
    with col2:
        st.markdown("**⚠️ Risk Alerts**")
        alerts = [
            "Reliance Jio campaign showing declining CTR - optimization needed",
            "HDFC Bank's customer sentiment dropped 8% this week",
            "Tata Motors facing increased competitive pressure in digital space",
            "Infosys video completion rates below industry benchmark"
        ]
        
        for alert in alerts:
            urgency = random.choice(["Low", "Medium", "High"])
            color = {"Low": "🟢", "Medium": "🟡", "High": "🔴"}[urgency]
            st.markdown(f"• {color} {alert} *({urgency} priority)*")
    
    # Predictive analytics
    st.subheader("📈 Predictive Brand Performance")
    
    # Generate future performance predictions
    top_brands = df.nlargest(8, 'Brand_Score')[['Brand', 'Brand_Score', 'Engagement_Rate']]
    
    # Add predicted values
    top_brands['Predicted_Score_Next_Quarter'] = top_brands['Brand_Score'] * random.uniform(1.02, 1.15)
    top_brands['Predicted_Engagement_Next_Quarter'] = top_brands['Engagement_Rate'] * random.uniform(1.05, 1.25)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Current vs predicted brand scores
    fig.add_trace(
        go.Bar(
            name="Current Score",
            x=top_brands['Brand'],
            y=top_brands['Brand_Score'],
            marker_color='#2d5a3d'
        ),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Bar(
            name="Predicted Score",
            x=top_brands['Brand'],
            y=top_brands['Predicted_Score_Next_Quarter'],
            marker_color='#9caf88'
        ),
        secondary_y=False,
    )
    
    fig.update_layout(
        title="Current vs Predicted Brand Scores (Next Quarter)",
        barmode='group'
    )
    
    fig.update_xaxes(tickangle=45)
    
    st.plotly_chart(fig, use_container_width=True)

def create_market_intelligence_dashboard(df):
    """Market intelligence and competitive analysis"""
    st.header("📈 Market Intelligence & Competitive Analysis")
    
    # Market overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_market_value = 4280  # USD Million
        st.metric("💰 Market Size (2024)", f"${total_market_value}M", delta="+7.8% CAGR")
    
    with col2:
        projected_value = 6720  # USD Million 2030
        st.metric("📊 2030 Projection", f"${projected_value}M", delta="57% growth")
    
    with col3:
        active_brands = len(df)
        st.metric("🏢 Tracked Brands", f"{active_brands}", delta="+12 this month")
    
    with col4:
        avg_digital_maturity = (df['Digital_Maturity'] == 'Advanced').sum() / len(df) * 100
        st.metric("🚀 Advanced Digital %", f"{avg_digital_maturity:.1f}%", delta="+5.2% YoY")
    
    # Market segment analysis
    st.subheader("🎯 Market Segment Analysis")
    
    segments = {
        "Landscaping Services": {"value": 5260, "projection": 8930, "cagr": 6.8},
        "Indoor Plants": {"value": 250, "projection": 406, "cagr": 8.45},
        "Online Nursery": {"value": 387, "projection": 498, "cagr": 4.27},
        "Corporate Gifting": {"value": 1450, "projection": 2160, "cagr": 8.4}
    }
    
    segment_df = pd.DataFrame.from_dict(segments, orient='index').reset_index()
    segment_df.columns = ['Segment', '2024 Value (USD M)', '2030 Projection (USD M)', 'CAGR (%)']
    
    st.dataframe(segment_df, use_container_width=True)
    
    # Competitive landscape
    col1, col2 = st.columns(2)
    
    with col1:
        # Industry concentration
        industry_concentration = df.groupby('Industry')['Market_Share'].sum().sort_values(ascending=False)
        
        fig = px.pie(
            values=industry_concentration.values,
            names=industry_concentration.index,
            title="Market Share by Industry"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Digital maturity by industry
        maturity_by_industry = df.groupby(['Industry', 'Digital_Maturity']).size().unstack(fill_value=0)
        
        fig = px.bar(
            maturity_by_industry,
            title="Digital Maturity Distribution by Industry",
            barmode='stack'
        )
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
    
    # Competitive benchmarking
    st.subheader("⚔️ Competitive Benchmarking")
    
    # Top performers analysis
    top_performers = df.nlargest(10, 'Brand_Score')[
        ['Brand', 'Industry', 'Brand_Score', 'Monthly_Ad_Spend', 'Engagement_Rate', 'Digital_Maturity']
    ].reset_index(drop=True)
    
    top_performers.index += 1  # Start ranking from 1
    
    st.markdown("**🏆 Top 10 Brand Performance Leaders**")
    st.dataframe(top_performers, use_container_width=True)
    
    # Industry benchmarks
    st.subheader("📊 Industry Benchmarks")
    
    benchmarks = df.groupby('Industry').agg({
        'Brand_Score': ['mean', 'std'],
        'Engagement_Rate': ['mean', 'std'],
        'Monthly_Ad_Spend': ['mean', 'std'],
        'Customer_Sentiment': ['mean', 'std']
    }).round(2)
    
    benchmarks.columns = ['Brand Score Avg', 'Brand Score Std', 'Engagement Avg', 'Engagement Std',
                         'Ad Spend Avg', 'Ad Spend Std', 'Sentiment Avg', 'Sentiment Std']
    
    st.dataframe(benchmarks, use_container_width=True)

def create_system_health_dashboard():
    """System health and infrastructure monitoring"""
    st.header("🔧 System Health & Infrastructure Monitoring")
    
    # Generate current system metrics
    metrics = generate_real_time_metrics()
    
    # System overview
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        pipeline_status = metrics['pipeline_health']
        status_color = {
            'Healthy': 'status-healthy',
            'Warning': 'status-warning', 
            'Critical': 'status-critical'
        }[pipeline_status]
        st.markdown(f'**Pipeline Status:** <span class="{status_color}">{pipeline_status}</span>', unsafe_allow_html=True)
    
    with col2:
        st.metric("⚡ Processing Latency", f"{metrics['processing_latency']}ms", delta="-2ms")
    
    with col3:
        st.metric("💾 Storage Utilization", f"{metrics['storage_utilization']}%", delta="+2.1%")
    
    with col4:
        st.metric("🔗 Active Sources", f"{metrics['data_sources_active']}/50", delta="+2")
    
    # Infrastructure components
    st.subheader("🏗️ Infrastructure Components")
    
    components = [
        {"Component": "Apache Kafka", "Status": "Healthy", "Partitions": "256", "Throughput": "2.4M msg/sec", "Uptime": "99.9%"},
        {"Component": "Apache Spark", "Status": "Healthy", "Active Jobs": "45", "Avg Processing": "2.3s", "Uptime": "99.7%"},
        {"Component": "PostgreSQL", "Status": "Healthy", "Connections": "284/500", "Query Latency": "< 5ms", "Uptime": "99.8%"},
        {"Component": "Redis Cache", "Status": "Warning", "Memory Usage": "78%", "Hit Rate": "94.2%", "Uptime": "99.5%"},
        {"Component": "AI/ML Pipeline", "Status": "Healthy", "Models Active": "4/4", "Accuracy": "94.7%", "Uptime": "99.6%"}
    ]
    
    components_df = pd.DataFrame(components)
    st.dataframe(components_df, use_container_width=True)
    
    # Performance charts
    col1, col2 = st.columns(2)
    
    with col1:
        # CPU and memory usage over time
        hours = list(range(24))
        cpu_usage = [random.uniform(20, 80) for _ in hours]
        memory_usage = [random.uniform(40, 85) for _ in hours]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=hours, y=cpu_usage, mode='lines', name='CPU Usage (%)', line=dict(color='#e74c3c')))
        fig.add_trace(go.Scatter(x=hours, y=memory_usage, mode='lines', name='Memory Usage (%)', line=dict(color='#3498db')))
        
        fig.update_layout(
            title="System Resource Usage (24H)",
            xaxis_title="Hour",
            yaxis_title="Usage (%)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Error rates by component
        error_data = {
            'Component': ['Kafka', 'Spark', 'PostgreSQL', 'Redis', 'AI Pipeline'],
            'Error Rate (%)': [0.001, 0.003, 0.002, 0.015, 0.001]
        }
        
        fig = px.bar(
            x=error_data['Component'],
            y=error_data['Error Rate (%)'],
            title="Error Rates by Component",
            color=error_data['Error Rate (%)'],
            color_continuous_scale='RdYlGn_r'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Alert system
    st.subheader("🚨 Active Alerts & Notifications")
    
    alerts = [
        {"Time": "2 min ago", "Level": "Warning", "Component": "Redis", "Message": "Memory usage above 75% threshold"},
        {"Time": "15 min ago", "Level": "Info", "Component": "Kafka", "Message": "Successfully scaled partition count"},
        {"Time": "1 hour ago", "Level": "Resolved", "Component": "AI Pipeline", "Message": "Model retraining completed successfully"},
        {"Time": "3 hours ago", "Level": "Info", "Component": "Data Ingestion", "Message": "New data source 'TikTok Ads' connected"}
    ]
    
    for alert in alerts:
        level_colors = {
            "Critical": "🔴",
            "Warning": "🟡", 
            "Info": "🔵",
            "Resolved": "🟢"
        }
        
        icon = level_colors.get(alert["Level"], "⚪")
        st.markdown(f"{icon} **{alert['Time']}** - {alert['Component']}: {alert['Message']}")
    
    # System recommendations
    st.subheader("💡 System Optimization Recommendations")
    
    recommendations = [
        "Consider Redis memory optimization - current usage at 78%",
        "Kafka partition rebalancing scheduled for optimal performance", 
        "AI model accuracy trending upward - consider production deployment",
        "Data pipeline latency within SLA - no action required"
    ]
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"{i}. {rec}")

if __name__ == "__main__":
    main()