from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


def get_sentiment(text: str) -> dict:
    scores = sia.polarity_scores(text)

    if scores["compound"] >= 0.05:
        label = "positive"
    elif scores["compound"] <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return {
        "text": text,
        "negative": scores["neg"],
        "neutral": scores["neu"],
        "positive": scores["pos"],
        "compound": scores["compound"],
        "sentiment": label,
    }
