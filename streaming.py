import faust
from typing import List
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from text_regulation import preprocess_tweet

# Define the Faust app and Kafka configuration
app = faust.App('twitter_stream_app', broker='kafka://localhost:9092')


# Define a schema for the tweet stream
class Tweet(faust.Record):
    created_at: str
    tweet_text: str


# Define a schema for the sentiment stream
class Sentiment(faust.Record):
    created_at: str
    sentiment_score: float


# Define a Kafka topic for the tweet stream
tweet_topic = app.topic('tweets', value_type=Tweet)

# Define a Kafka topic for the sentiment stream
sentiment_topic = app.topic('sentiments', value_type=Sentiment)

# Create a SentimentIntensityAnalyzer instance
sia = SentimentIntensityAnalyzer()


# Define the Faust agent that processes tweets
@app.agent(tweet_topic)
async def process_tweet(tweets: faust.Stream[Tweet]) -> None:
    async for tweet in tweets:
        # Preprocess and analyze the tweet
        cleaned_text = preprocess_tweet(tweet.tweet_text)
        sentiment_score = sia.polarity_scores(cleaned_text)['compound']

        # Create a Sentiment object and send it to the sentiment_topic
        sentiment = Sentiment(created_at=tweet.created_at, sentiment_score=sentiment_score)
        await sentiment_topic.send(value=sentiment)


# Add the preprocess_tweet function here (from your previous code)

if __name__ == '__main__':
    app.main()
