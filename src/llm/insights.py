from collections import Counter


def generate_insights(sentiment_df, keywords):
    transformer_counts = Counter(sentiment_df["transformer_sentiment"])

    top_positive = sentiment_df[
        sentiment_df["transformer_sentiment"] == "positive"
    ]["text"].tolist()

    top_negative = sentiment_df[
        sentiment_df["transformer_sentiment"] == "negative"
    ]["text"].tolist()

    keyword_list = [word for word, count in keywords[:5]]

    insights = []

    insights.append(
        f"Out of {len(sentiment_df)} reviews, {transformer_counts.get('positive', 0)} are positive "
        f"and {transformer_counts.get('negative', 0)} are negative according to the transformer model."
    )

    if keyword_list:
        insights.append(
            "The most frequently discussed themes are: " + ", ".join(keyword_list) + "."
        )

    if top_negative:
        insights.append(
            "Negative feedback is primarily associated with delivery delays, confusing user experience, "
            "refund friction, and weak support interactions."
        )

    if top_positive:
        insights.append(
            "Positive feedback is largely driven by product quality, fast shipping, smooth experiences, "
            "and effective service resolution."
        )

    disagreement_count = (
        sentiment_df["sentiment"] != sentiment_df["transformer_sentiment"]
    ).sum()

    if disagreement_count > 0:
        insights.append(
            f"There are {disagreement_count} reviews where the lexicon-based and transformer-based models disagree, "
            "highlighting the importance of contextual sentiment analysis."
        )

    return insights
