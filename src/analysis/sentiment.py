from nltk.sentiment import SentimentIntensityAnalyzer
from transformers import pipeline

sia = SentimentIntensityAnalyzer()
hf_sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def get_vader_sentiment(text: str) -> dict:
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


def get_transformer_sentiment(text: str) -> dict:
    result = hf_sentiment_pipeline(text)[0]
    label = result["label"].lower()
    score = result["score"]

    return {
        "text": text,
        "transformer_sentiment": label,
        "transformer_score": score,
    }


def get_sentiment(text: str) -> dict:
    vader_result = get_vader_sentiment(text)
    transformer_result = get_transformer_sentiment(text)

    return {
        **vader_result,
        **transformer_result,
    }
