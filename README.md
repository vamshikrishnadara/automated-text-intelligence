# Automated Text Intelligence & Insight Generation using NLP and LLMs

An AI-powered text analytics system that transforms unstructured customer feedback into actionable business insights using natural language processing and transformer-based language models.

## Project Overview

This project analyzes customer review text to extract meaningful intelligence for business decision-making. It combines traditional NLP techniques with modern transformer-based sentiment analysis to identify sentiment, recurring themes, and high-level business insights.

The system processes raw text data and generates:
- sentiment predictions using both VADER and a transformer model
- top keyword extraction
- business theme detection
- generated insight summaries
- exportable output files for analysis and reporting

## Features

- **Text Preprocessing**
  - lowercasing
  - punctuation removal
  - stopword filtering
  - lemmatization

- **Dual Sentiment Analysis**
  - lexicon-based sentiment using VADER
  - transformer-based sentiment using Hugging Face DistilBERT

- **Keyword Extraction**
  - identifies the most frequently discussed terms

- **Theme Detection**
  - categorizes text into business-relevant themes such as:
    - Support Issues
    - Delivery Problems
    - UI/UX Friction
    - Refund Issues
    - Product Quality
    - Positive Experience

- **Insight Generation**
  - summarizes major findings from sentiment and theme analysis
  - highlights disagreement between traditional and transformer-based models

- **Exported Results**
  - sentiment results CSV
  - keyword summary CSV
  - theme summary CSV
  - generated insights text file

## Tech Stack

- Python
- Pandas
- NLTK
- Scikit-learn
- Hugging Face Transformers
- PyTorch

## Project Structure

```bash
automated-text-intelligence/
│
├── data/
│   └── sample_reviews.csv
├── outputs/
│   ├── generated_insights.txt
│   ├── sentiment_results.csv
│   ├── theme_summary.csv
│   └── top_keywords.csv
├── src/
│   ├── analysis/
│   │   ├── sentiment.py
│   │   └── topics.py
│   ├── llm/
│   │   └── insights.py
│   ├── preprocessing/
│   │   └── clean_text.py
│   └── main.py
├── requirements.txt
└── README.md
