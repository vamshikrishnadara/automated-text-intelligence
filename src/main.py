import os
import pandas as pd

from src.analysis.sentiment import get_sentiment
from src.analysis.topics import extract_top_keywords, summarize_themes
from src.llm.insights import generate_insights


def main():
    os.makedirs("outputs", exist_ok=True)

    df = pd.read_csv("data/sample_reviews.csv")

    sentiment_results = df["text"].apply(get_sentiment)
    sentiment_df = pd.DataFrame(sentiment_results.tolist())

    print("\n=== Sentiment Analysis Results ===")
    print(
        sentiment_df[
            [
                "text",
                "sentiment",
                "compound",
                "transformer_sentiment",
                "transformer_score",
            ]
        ]
    )

    print("\n=== Top Keywords ===")
    keywords = extract_top_keywords(df["text"], top_n=10)
    keywords_df = pd.DataFrame(keywords, columns=["keyword", "count"])
    for word, count in keywords:
        print(f"{word}: {count}")

    print("\n=== Theme Summary ===")
    theme_counts = summarize_themes(df["text"])
    theme_df = pd.DataFrame(theme_counts.items(), columns=["theme", "count"])
    for theme, count in theme_counts.items():
        print(f"{theme}: {count}")

    print("\n=== Generated Insights ===")
    insights = generate_insights(sentiment_df, keywords, theme_counts)
    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")

    sentiment_df.to_csv("outputs/sentiment_results.csv", index=False)
    keywords_df.to_csv("outputs/top_keywords.csv", index=False)
    theme_df.to_csv("outputs/theme_summary.csv", index=False)

    with open("outputs/generated_insights.txt", "w") as f:
        for i, insight in enumerate(insights, start=1):
            f.write(f"{i}. {insight}\n")

    print("\n=== Files Saved ===")
    print("outputs/sentiment_results.csv")
    print("outputs/top_keywords.csv")
    print("outputs/theme_summary.csv")
    print("outputs/generated_insights.txt")


if __name__ == "__main__":
    main()
