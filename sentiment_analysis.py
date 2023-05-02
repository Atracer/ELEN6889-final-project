from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd


# nltk.download('vader_lexicon')
def get_sentiment_score(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']


def sentiment_text(data):
    # Perform sentiment analysis
    sia = SentimentIntensityAnalyzer()
    data['sentiment_score'] = data['cleaned_text'].apply(lambda x: sia.polarity_scores(x)['compound'])

    # Convert the 'created_at' column to a datetime object
    data['created_at'] = pd.to_datetime(data['created_at'])

    # Summarize and analyze sentiment scores every 15 minutes
    summary = data.groupby(pd.Grouper(key='created_at', freq='15T'))['sentiment_score'].mean().reset_index()

    # Replace NaN values with 0
    summary['sentiment_score'] = summary['sentiment_score'].fillna(0)

    return summary
