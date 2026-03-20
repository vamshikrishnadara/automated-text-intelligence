from collections import Counter

from src.preprocessing.clean_text import clean_text

THEME_KEYWORDS = {
    "Support Issues": {"support", "unhelpful", "service"},
    "Delivery Problems": {"delivery", "shipping", "delayed"},
    "UI/UX Friction": {"app", "interface", "login", "confusing", "slow", "crash"},
    "Refund Issues": {"refund", "process"},
    "Product Quality": {"product", "quality", "packaging", "value"},
    "Positive Experience": {"happy", "great", "satisfied", "smooth", "excellent"},
}


def extract_top_keywords(texts, top_n=10):
    all_words = []

    for text in texts:
        cleaned = clean_text(text)
        all_words.extend(cleaned.split())

    word_counts = Counter(all_words)
    return word_counts.most_common(top_n)


def detect_themes(text: str):
    cleaned_words = set(clean_text(text).split())
    matched_themes = []

    for theme, keywords in THEME_KEYWORDS.items():
        if cleaned_words.intersection(keywords):
            matched_themes.append(theme)

    if not matched_themes:
        matched_themes.append("Other")

    return matched_themes


def summarize_themes(texts):
    theme_counter = Counter()

    for text in texts:
        themes = detect_themes(text)
        theme_counter.update(themes)

    return theme_counter
