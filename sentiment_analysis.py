from nltk.sentiment import SentimentIntensityAnalyzer


def get_sentiment_score(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment['compound']

class SentimentAnalyzer:
    def get_sentiment_scores(self, texts):
        return [get_sentiment_score(text) for text in texts]
