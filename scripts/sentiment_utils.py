from textblob import TextBlob
import pandas as pd

def get_sentiment_score(text):
    """
    Calculate sentiment polarity score for given text.
    - Returns score between -1 (negative) to 1 (positive).
    """
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_sentiment_category(score):
    """
    Categorize sentiment score into Positive, Neutral, or Negative.
    """
    if score > 0.05:
        return 'Positive'
    elif score < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def apply_sentiment_analysis(df, text_column='headline'):
    """
    Apply sentiment analysis to a DataFrame column containing text.
    Adds two new columns:
    - sentiment_score: Polarity score.
    - sentiment_category: Positive, Neutral, or Negative.
    """
    df['sentiment_score'] = df[text_column].apply(get_sentiment_score)
    df['sentiment_category'] = df['sentiment_score'].apply(get_sentiment_category)
    return df
