from collections import Counter

from src.preprocessing.clean_text import clean_text


def extract_top_keywords(texts, top_n=10):
    all_words = []

    for text in texts:
        cleaned = clean_text(text)
        all_words.extend(cleaned.split())

    word_counts = Counter(all_words)
    return word_counts.most_common(top_n)
