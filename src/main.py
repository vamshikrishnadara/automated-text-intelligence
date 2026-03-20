import pandas as pd

from src.analysis.sentiment import get_sentiment
from src.analysis.topics import extract_top_keywords, summarize_themes
from src.llm.insights import generate_insights


def main():
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
    for word, count in keywords:
        print(f"{word}: {count}")

    print("\n=== Theme Summary ===")
    theme_counts = summarize_themes(df["text"])
    for theme, count in theme_counts.items():
        print(f"{theme}: {count}")

    print("\n=== Generated Insights ===")
    insights = generate_insights(sentiment_df, keywords, theme_counts)
    for i, insight in enumerate(insights, start=1):
        print(f"{i}. {insight}")


if __name__ == "__main__":
    main()
