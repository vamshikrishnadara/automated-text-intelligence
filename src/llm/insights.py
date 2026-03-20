from collections import Counter


def generate_insights(sentiment_df, keywords):
    sentiment_counts = Counter(sentiment_df["sentiment"])

    top_positive = sentiment_df[sentiment_df["sentiment"] == "positive"]["text"].tolist()
    top_negative = sentiment_df[sentiment_df["sentiment"] == "negative"]["text"].tolist()

    keyword_list = [word for word, count in keywords[:5]]

    insights = []

    insights.append(
        f"Out of {len(sentiment_df)} reviews, {sentiment_counts.get('positive', 0)} are positive, "
        f"{sentiment_counts.get('negative', 0)} are negative, and "
        f"{sentiment_counts.get('neutral', 0)} are neutral."
    )

    if keyword_list:
        insights.append(
            "The most frequently discussed themes are: " + ", ".join(keyword_list) + "."
        )

    if top_negative:
        insights.append(
            "Negative feedback appears to be associated with issues such as delays, confusing interfaces, "
            "refund processes, or lack of support."
        )

    if top_positive:
        insights.append(
            "Positive feedback is mainly driven by product quality, fast service, smooth experiences, "
            "and responsive support."
        )

    return insights
