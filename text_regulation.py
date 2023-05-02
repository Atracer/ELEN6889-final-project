import re
import pandas as pd


def preprocess_tweet(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\@\w+|\#', '', text)
    text = text.lower()

    # Remove emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r'', text)

    # Remove emojis
    # text = demojize(text)

    return text



def get_clean_text(texts):
    data = pd.read_excel(texts)
    data['cleaned_text'] = data['tweet_text'].apply(preprocess_tweet)

    # Filter tweets for Google and Amazon
    keywords = ['google', 'amazon', 'goog', 'amzn', 'AMAZON', 'AMZN', 'GOOGLE', 'GOOG', 'APPLE', 'apple', 'APPL', 'appl']
    data = data[data['cleaned_text'].str.contains('|'.join(keywords))]

    return data
