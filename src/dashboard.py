import pandas as pd
import streamlit as st

st.set_page_config(page_title="Text Intelligence Dashboard", layout="wide")

st.title("Automated Text Intelligence Dashboard")
st.write("Analyze customer feedback using NLP and transformer-based sentiment models.")

sentiment_df = pd.read_csv("outputs/sentiment_results.csv")
keywords_df = pd.read_csv("outputs/top_keywords.csv")
theme_df = pd.read_csv("outputs/theme_summary.csv")

st.subheader("Sentiment Results")
st.dataframe(
    sentiment_df[
        ["text", "sentiment", "transformer_sentiment", "transformer_score"]
    ],
    use_container_width=True,
)

st.subheader("Top Keywords")
st.bar_chart(keywords_df.set_index("keyword"))

st.subheader("Theme Summary")
st.bar_chart(theme_df.set_index("theme"))

st.subheader("Generated Insights")
with open("outputs/generated_insights.txt", "r") as f:
    insights = f.read()

st.text(insights)
