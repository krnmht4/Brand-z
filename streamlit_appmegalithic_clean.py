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
    df = pd.read_csv("brand_selection_list.csv")
    df = df.dropna(subset=['Brand'])
    return df

def fetch_trends(keywords, geo='IN', timeframe='now 7-d'):
    pytrends = TrendReq()
    pytrends.build_payload(keywords, geo=geo, timeframe=timeframe)
    data = pytrends.interest_over_time()
    return data.drop(columns=['isPartial'])

def fetch_news_sentiment(query):
    key = st.secrets["NEWSAPI_KEY"]
    resp = requests.get(
        f"https://newsapi.org/v2/everything?q={query}&pageSize=20&apiKey={key}"
    ).json().get("articles", [])
    score = sum(1 if ("rise" in a["title"].lower() or "gain" in a["title"].lower())
                else -1 if ("drop" in a["title"].lower() or "decline" in a["title"].lower())
                else 0 for a in resp) / max(len(resp), 1)
    return score, len(resp)

def fetch_weather(city="New Delhi"):
    key = st.secrets["OPENWEATHER_KEY"]
    data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}"
    ).json()
    main = data.get("main", {})
    weather = data.get("weather", [{}])[0]
    return main.get("temp", "N/A"), main.get("humidity", "N/A"), weather.get("main", "N/A")

def main():
    st.set_page_config(page_title="Megalithic Brand Intelligence", layout="wide")
    df = load_data()
    st.title("🚀 Megalithic Brand Intelligence Platform")
    st.sidebar.markdown(f"**Total Brands:** {len(df)}")

    tab1, tab2, tab3 = st.tabs(["Real-Time", "Analytics", "Trends & News"])
    with tab1:
        st.header("🎯 Real-Time Metrics")
        c1, c2, c3 = st.columns(3)
        for col, label in zip([c1, c2, c3], ["Events/sec", "Active Campaigns", "Conversion Rate"]):
            col.metric(label, random.randint(2000, 3000))
    with tab2:
        st.header("📊 Brand Analytics")
        industries = df["Industry"].unique()
        sel = st.multiselect("Industry", industries, industries)
        sub = df[df["Industry"].isin(sel)]
        fig = px.scatter(sub, x="Brand", y="Engagement_Rate", size="Brand_Score")
        st.plotly_chart(fig, use_container_width=True)
    with tab3:
        st.header("📈 Google Trends & News Sentiment")
        tr = fetch_trends(["brand intelligence"])
        st.line_chart(tr)
        sent_score, count = fetch_news_sentiment("brand intelligence")
        st.metric("News Sentiment", f"{sent_score:.2f}", delta=f"{count} articles")
        temp, hum, cond = fetch_weather("Bengaluru")
        st.write(f"☁️ Weather in Bengaluru: {temp}°C, {hum}%, {cond}")

if __name__ == "__main__":
    main()
