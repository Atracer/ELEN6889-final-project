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
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r'', text)

    return text


file_name = 'tweeter.csv'
data = pd.read_csv(file_name)
print(data.columns)
data['cleaned_text'] = data['tweet_text'].apply(preprocess_tweet)
print(data['cleaned_text'])

output_file_name = 'cleaned_tweets.csv'
data.to_csv(output_file_name, index=False)

